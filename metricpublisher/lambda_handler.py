"""Lambda function entrypoint handlers."""

from jsonschema import ValidationError
import schema
import boto3
import config
import time
import ast

CLIENT = boto3.client('logs')
CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000


def get_LOG_GROUP_NAME():
    """Get the log group name."""
    return config.LOG_GROUP_NAME


def get_NAMESPACE():
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
    new_log_stream_name = '_'.join((get_NAMESPACE(), request_id))
    CLIENT.create_log_stream(
        logGroupName=get_LOG_GROUP_NAME(),
        logStreamName=new_log_stream_name
    )
    CLIENT.put_log_events(
        logGroupName=get_LOG_GROUP_NAME(),
        logStreamName=new_log_stream_name,
        logEvents=[
            {
                'timestamp': get_current_time(),
                'message': event
            },
        ],
    )


def batch_metrics(log_stream_names):
    """Batch together metrics.

    Parameters:
        log_stream_names (list): A list of
        log streams containing log events
        whose 'message' field contains metrics.

    Returns:
        metrics (list): A list of metrics to
        be put to cloudwatch.

    """
    metrics_list = []
    if len(log_stream_names) == 0:
        return metrics_list
    for stream in log_stream_names:
        log_event = CLIENT.get_log_events(
            logGroupName=get_LOG_GROUP_NAME(),
            logStreamName=stream
        )
        while len(log_event['events']) == 0:
            time.sleep(1)  # Events will not show if put recently
            log_event = CLIENT.get_log_events(
                logGroupName=get_LOG_GROUP_NAME(),
                logStreamName=stream
            )
        event_message = ast.literal_eval(log_event['events'][0]['message'])
        for metric in event_message['metric_data']:
            metrics_list.append(metric)
    return metrics_list


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
