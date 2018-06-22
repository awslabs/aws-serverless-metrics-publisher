"""Lambda function entrypoint handlers."""

from jsonschema import ValidationError
import schema
import boto3
import config
import time

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
        (str) message upon successful execution

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
