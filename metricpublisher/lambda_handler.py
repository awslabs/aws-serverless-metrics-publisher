"""Lambda function entrypoint handlers."""

from jsonschema import ValidationError
import schema
import boto3
import config
import time
import ast

LOG_CLIENT = boto3.client('logs')
DYNAMODB_CLIENT = boto3.client('dynamodb')
CLOUDWATCH_CLIENT = boto3.client('cloudwatch')
CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000
CURSOR_KEY = 'cursor_for_next_batch'


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
    for event in log_events:
        event_message = ast.literal_eval(event['message'])
        for metric in event_message['metric_data']:
            metrics_list.append(metric)
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


def metric_publisher(event, context):
    """Publish metrics to cloudwatch.

    Parameters:
        None

    Returns:
        None

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
    metrics_to_put = [format_metric(metric)
                      for metric in batch_metrics(log_events)]
    try:
        CLOUDWATCH_CLIENT.put_metric_data(
            Namespace=get_namespace(),
            MetricData=metrics_to_put
        )
    except Exception:
        next_timestamp = start_time
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
