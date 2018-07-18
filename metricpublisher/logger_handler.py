"""Metric Logger lambda function entrypoint and helper functions."""

import config
import schema
from jsonschema.exceptions import ValidationError
import boto3
import time


LOG_CLIENT = boto3.client('logs')
CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000


def get_log_group_name():
    """Get the log group name."""
    return config.LOG_GROUP_NAME


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
