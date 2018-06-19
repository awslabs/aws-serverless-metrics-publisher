"""Lambda function entrypoint handlers."""

from jsonschema import ValidationError
import schema


def log_event(event, context):
    """Log event.

    Parameters:
        event (dict): the user input

    Returns:
        (str) message upon successful execution

    """
    try:
        schema.validate_log_event_request(event)
    except ValidationError as err:
        return _error_response(err)


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
