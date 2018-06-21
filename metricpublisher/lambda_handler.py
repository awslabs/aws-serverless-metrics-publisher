"""Lambda function entrypoint handlers."""

from jsonschema import ValidationError
import schema
import boto3
import config
import time

LOG_GROUP_NAME = config.LOG_GROUP_NAME_TEMP
CLIENT = boto3.client('logs')
NAMESPACE = config.NAMESPACE_PARAM_TEMP
CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000


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
    new_log_stream_name = '_'.join((NAMESPACE, request_id))
    CLIENT.create_log_stream(
        logGroupName=LOG_GROUP_NAME,
        logStreamName=new_log_stream_name
    )
    CLIENT.put_log_events(
        logGroupName=LOG_GROUP_NAME,
        logStreamName=new_log_stream_name,
        logEvents=[
            {
                'timestamp': int(time.time()*CONVERT_SECONDS_TO_MILLIS_FACTOR),
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
