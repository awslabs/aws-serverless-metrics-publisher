"""Lambda function entrypoint handlers."""

from jsonschema import ValidationError
import schema
import boto3
import config
import time
import ast
import uuid


LOG_CLIENT = boto3.client('logs')
DYNAMODB_CLIENT = boto3.client('dynamodb')
CLOUDWATCH_CLIENT = boto3.client('cloudwatch')
CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000
CURSOR_KEY = 'cursor_for_next_batch'
MAX_BATCH_SIZE = 25


def get_log_group_name():
    """Get the log group name."""
    return config.LOG_GROUP_NAME


def get_table_name():
    """Get the checkpoint table name."""
    return config.CHECKPOINT_TABLE_NAME


def get_namespace():
    """Get the namespace."""
    return config.NAMESPACE_PARAM


def get_current_time():
    """Get the current time."""
    return int(time.time()*CONVERT_SECONDS_TO_MILLIS_FACTOR)


def log_event(event, context):
    """Log event.

    Parameters:
        event (dict): The metric data that
        the user would like to put to cloudwatch.

    Returns:
        None

    """
    try:
        schema.validate_log_event_request(event)
    except ValidationError as err:
        return _error_response(err)
    request_id = event["request_id"]
    event = str(event)
    new_log_stream_name = '_'.join((get_namespace(), request_id))
    LOG_CLIENT.create_log_stream(
        logGroupName=get_log_group_name(),
        logStreamName=new_log_stream_name
    )
    LOG_CLIENT.put_log_events(
        logGroupName=get_log_group_name(),
        logStreamName=new_log_stream_name,
        logEvents=[
            {
                'timestamp': get_current_time(),
                'message': event
            },
        ],
    )


def batch_metrics(log_events):
    """Batch together metrics.

    Parameters:
        log_events (list): A list of
        log events whose 'message'
        field contains metrics.

    Returns:
        metrics (list): A list of metrics to
        be put to cloudwatch.

    """
    metrics_list = []
    log_streams_set = set()
    for event in log_events:
        log_stream_name = event['logStreamName']
        if log_stream_name not in log_streams_set:
            event_message = ast.literal_eval(event['message'])
            for metric in event_message['metric_data']:
                metrics_list.append(metric)
        log_streams_set.add(log_stream_name)
    return metrics_list


def format_metric(metric):
    """Format a single metric.

    Parameters:
        metric (dict): The metric to format

    Returns:
        metric (dict): The new metric in
        the format needed for the put_metric_data
        API.

    """
    metric_keys = metric.keys()
    metric["MetricName"] = metric.pop("metric_name")
    if "dimensions" in metric_keys:
        for dimension in metric["dimensions"]:
            dimension["Name"] = dimension.pop("name")
            dimension["Value"] = dimension.pop("value")
        metric["Dimensions"] = metric.pop("dimensions")
    if "timestamp" in metric_keys:
        metric["Timestamp"] = metric.pop("timestamp")
    if "value" in metric_keys:
        metric["Value"] = metric.pop("value")
    else:
        metric["statistic_values"]["SampleCount"] =\
            metric["statistic_values"].pop("sample_count")
        metric["statistic_values"]["Sum"] =\
            metric["statistic_values"].pop("sum")
        metric["statistic_values"]["Minimum"] =\
            metric["statistic_values"].pop("minimum")
        metric["statistic_values"]["Maximum"] =\
            metric["statistic_values"].pop("maximum")
        metric["StatisticValues"] = metric.pop("statistic_values")
    if "unit" in metric_keys:
        metric["Unit"] = metric.pop("unit")
    if "storage_resolution" in metric_keys:
        metric["StorageResolution"] = metric.pop("storage_resolution")
    return metric


def unformat_metric(metric):
    """Unformat a single metric.

    Parameters:
        metric (dict): The metric to unformat

    Returns:
        metric (dict): The new metric in
        the format needed for the log_event
        API.

    """
    metric_keys = metric.keys()
    metric["metric_name"] = metric.pop("MetricName")
    if "Dimensions" in metric_keys:
        for dimension in metric["Dimensions"]:
            dimension["name"] = dimension.pop("Name")
            dimension["value"] = dimension.pop("Value")
        metric["dimensions"] = metric.pop("Dimensions")
    if "Timestamp" in metric_keys:
        metric["timestamp"] = metric.pop("Timestamp")
    if "Value" in metric_keys:
        metric["value"] = metric.pop("Value")
    else:
        metric["StatisticValues"]["sample_count"] =\
            metric["StatisticValues"].pop("SampleCount")
        metric["StatisticValues"]["sum"] =\
            metric["StatisticValues"].pop("Sum")
        metric["StatisticValues"]["minimum"] =\
            metric["StatisticValues"].pop("Minimum")
        metric["StatisticValues"]["maximum"] =\
            metric["StatisticValues"].pop("Maximum")
        metric["statistic_values"] = metric.pop("StatisticValues")
    if "Unit" in metric_keys:
        metric["unit"] = metric.pop("Unit")
    if "StorageResolution" in metric_keys:
        metric["storage_resolution"] = metric.pop("StorageResolution")
    return metric


def convert_batch_to_event(batch):
    """Convert a batch of metrics into a log event.

    Parameters:
        batch (list): The batch of metrics to convert

    Returns:
        event (dict): The event ready to be put
        to a new log stream

    """
    request_id = '_'.join(("log_events_retry", str(uuid.uuid4())))
    return {
        "request_id": request_id,
        "metric_data": [unformat_metric(metric) for metric in batch]
    }


def metric_publisher(event, context):
    """Publish metrics to cloudwatch.

    Parameters:
        None

    Returns:
        number_of_metrics (int): number of new
        metrics that were published successfully

    """
    item_data = DYNAMODB_CLIENT.get_item(
        Key={
            'cursor': {
                'S': CURSOR_KEY
            }
        },
        TableName=get_table_name()
    )
    if 'Item' not in item_data:
        start_time = 0
    else:
        start_time = int(item_data['Item']['cursor_timestamp']['N'])
    next_timestamp = get_current_time()
    log_events = LOG_CLIENT.filter_log_events(
        logGroupName=get_log_group_name(),
        startTime=start_time,
        endTime=next_timestamp
    )['events']
    if len(log_events) == 0:
        return 0
    next_batch = batch_metrics(log_events)
    metrics_to_put = [format_metric(metric) for metric in next_batch]
    batches = [metrics_to_put[start:start+MAX_BATCH_SIZE]
               for start in range(0, len(metrics_to_put), MAX_BATCH_SIZE)]
    number_of_metrics = 0
    for batch in batches:
        try:
            CLOUDWATCH_CLIENT.put_metric_data(
                Namespace=get_namespace(),
                MetricData=batch
            )
            number_of_metrics += len(batch)
        except Exception:
            log_event(convert_batch_to_event(batch), None)
    DYNAMODB_CLIENT.put_item(
        TableName=get_table_name(),
        Item={
            'cursor': {
                'S': CURSOR_KEY
            },
            'cursor_timestamp': {
                'N': str(next_timestamp),
            },
        },
        ReturnConsumedCapacity='NONE',
    )
    return number_of_metrics


def _error_response(error):
    error_type = type(error).__name__
    if hasattr(error, 'message'):
        message = error.message
    else:
        message = error.__str__

    return {
        'error': {
            'type': error_type,
            'message': message
        }
    }
