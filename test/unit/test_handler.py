import json
from unit import events
from pytest_mock import mocker
import time
import itertools
from metricpublisher import logger_handler
from metricpublisher import publisher_handler
from metricpublisher import schema

CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000


def test_standard_valid_input():
    """Test to make sure a standard valid input passes the JSON schema"""
    data = events.standard_valid_input()
    assert schema._validate(data,"log_event.json") == None

def test_basic_valid_input():
    """Test to make sure a minimalistic input passes the JSON schema"""
    data = events.basic_valid_input()
    assert schema._validate(data,"log_event.json") == None

def test_multiple_metrics_input():
    """Test to validate that the option to input multiple metrics simultaneously is available."""
    data = events.multiple_metrics_input()
    assert schema._validate(data,"log_event.json") == None

def test_value_and_statistic_values_both_included():
    """Test to assert that customer cannot pass in both 'value' and
    'statistic_values' in the input. (They are mutually exclusive)."""
    data = events.value_and_statistic_values_both_included()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_missing_value_and_statistic_values():
    """Test to make sure at least one of 'value' or 'statistic_values' is present"""
    data = events.missing_value_and_statistic_values()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_missing_request_id():
    """Test to make sure a request_id is passed in by the customer"""
    data = events.missing_request_id()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_missing_metric_name():
    """Test to make sure a metric name is passed in by the customer"""
    data = events.missing_metric_name()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_statistic_values_missing_sum():
    """Test to make sure that 'Sum' is present when 'statistic_values' is"""
    data = events.statistic_values_missing_sum()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_unit_type_not_available():
    """Test to make sure that customer must pass in a valid unit type"""
    data = events.unit_type_not_available()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_storage_resolution_type_invalid():
    """Test to make sure the input type of 'storage_resolution' is valid"""
    data = events.storage_resolution_type_invalid()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_dimension_type_invalid():
    """Test to make sure the input type of 'dimension' is valid"""
    data = events.dimension_type_invalid()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_dimension_item_type_invalid():
    """Test to make sure the input type of each item in
    the 'dimension' Array is valid."""
    data = events.dimension_item_type_invalid()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_dimension_item_wrong_property():
    """Test to make sure the input type of each item in
    the 'dimension' Array is valid."""
    data = events.dimension_item_wrong_property()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_empty_request_id():
    """Test to make sure request_id is nonempty."""
    data = events.empty_request_id()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_empty_dimension_name():
    """Test to make sure request_id is nonempty."""
    data = events.empty_dimension_name()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_empty_metric_name():
    """Test to make sure request_id is nonempty."""
    data = events.empty_metric_name()
    _assert_error_response(
        logger_handler.log_event(data,None),"ValidationError"
    )

def test_log_event_client_function_calls(mocker):
    """Test to ensure that create_log_stream and put_log_events are called with the correct parameters."""
    mocker.patch.object(logger_handler, 'get_current_time')
    current_time = int(time.time()*CONVERT_SECONDS_TO_MILLIS_FACTOR)
    logger_handler.get_current_time.return_value = current_time
    mocker.patch.object(logger_handler,'LOG_CLIENT')
    mocker.patch.object(logger_handler, 'get_log_group_name')
    mocker.patch.object(logger_handler, 'get_namespace')
    logger_handler.get_log_group_name.return_value = 'metricPublisherAppLogGroup'
    logger_handler.get_namespace.return_value = 'metricPublisherAppNamespace'
    data = events.standard_valid_input()
    event = str(data)
    log_events = [
        {
            'timestamp': current_time,
            'message': event
        },
    ]
    log_stream_name = '_'.join(('metricPublisherAppNamespace', data["request_id"]))
    log_group_name = 'metricPublisherAppLogGroup'
    assert logger_handler.log_event(data, None) == None
    logger_handler.LOG_CLIENT.create_log_stream.assert_called_with(logGroupName=log_group_name, logStreamName=log_stream_name)
    logger_handler.LOG_CLIENT.put_log_events.assert_called_with(logGroupName=log_group_name, logStreamName=log_stream_name,logEvents = log_events)

def test_format_metric_simple_case():
    """Test that the format_metric function works for a basic metric."""
    metric_before = events.simple_metric_log_event_format()
    metric_expected = events.simple_metric_put_data_format()
    result = publisher_handler.format_metric(metric_before)
    assert result == metric_expected

def test_format_metric_complex_case():
    """Test that the format_metric function works for a more complicated metric."""
    metric_before = events.complex_metric_log_event_format()
    metric_expected = events.complex_metric_put_data_format()
    result = publisher_handler.format_metric(metric_before)
    assert result == metric_expected

def test_unformat_metric_simple_case():
    """Test that the unformat_metric function works for a basic metric."""
    metric_before = events.simple_metric_put_data_format()
    metric_expected = events.simple_metric_log_event_format()
    result = publisher_handler.unformat_metric(metric_before)
    assert result == metric_expected

def test_unformat_metric_complex_case():
    """Test that the unformat_metric function works for a more complicated metric."""
    metric_before = events.complex_metric_put_data_format()
    metric_expected = events.complex_metric_log_event_format()
    result = publisher_handler.unformat_metric(metric_before)
    assert result == metric_expected

def test_convert_batch_to_event(mocker):
    batch = events.sample_batch()
    expected_request_id_start = "log_events_retry_"
    expected_data = events.unformated_metrics_expected()
    batch_result = publisher_handler.convert_batch_to_event(batch)
    assert batch_result["request_id"].startswith(expected_request_id_start)
    assert batch_result["metric_data"] == expected_data

def test_batch_metrics_normal_case():
    """Test that batch metrics works when there are less than 26 new metrics."""
    sample_log_events = events.log_events_normal()
    expected_response = events.batched_metrics_normal()
    assert publisher_handler.batch_metrics(sample_log_events) == expected_response

def test_batch_metrics_too_many_metrics():
    """Test that batch metrics returns less than 26 metrics
    when there are more than 25 new metrics to publish."""
    too_many_log_events = events.many_log_events()
    expected_response = events.batch_metrics_many_events()
    assert publisher_handler.batch_metrics(too_many_log_events) == expected_response

def test_metric_publisher_client_function_calls(mocker):
    """Test to ensure that metric_publisher functions
    were called with the correct input."""
    log_events_response = events.sample_log_events()
    get_item_response = events.standard_item()
    start_time = int(get_item_response['Item']['cursor_timestamp']['N'])
    batch_metrics_response = events.metrics_before()
    metrics_to_put_expected = events.metrics_to_put_expected()
    log_group_name = 'metricPublisherAppLogGroup'
    table_name = 'metricPublisherAppDynamoDBTable'
    namespace = 'metricPublisherAppNamespace'
    current_time = int(time.time()*CONVERT_SECONDS_TO_MILLIS_FACTOR)
    number_of_metrics_expected = 6
    item_key = {
        'cursor': {
            'S': 'cursor_for_next_batch'
        }
    }
    mocker.patch.object(publisher_handler, 'LOG_CLIENT')
    mocker.patch.object(publisher_handler, 'DYNAMODB_CLIENT')
    mocker.patch.object(publisher_handler, 'CLOUDWATCH_CLIENT')
    mocker.patch.object(publisher_handler, 'get_log_group_name')
    mocker.patch.object(publisher_handler, 'get_table_name')
    mocker.patch.object(publisher_handler, 'get_namespace')
    mocker.patch.object(publisher_handler, 'get_current_time')
    publisher_handler.LOG_CLIENT.filter_log_events.return_value = log_events_response
    publisher_handler.DYNAMODB_CLIENT.get_item.return_value = get_item_response
    publisher_handler.get_log_group_name.return_value = log_group_name
    publisher_handler.get_table_name.return_value = table_name
    publisher_handler.get_namespace.return_value = namespace
    publisher_handler.get_current_time.return_value = current_time
    assert publisher_handler.metric_publisher(None, None) == number_of_metrics_expected
    publisher_handler.LOG_CLIENT.filter_log_events.assert_called_with(logGroupName=log_group_name,startTime=start_time,endTime=current_time)
    publisher_handler.DYNAMODB_CLIENT.get_item.assert_called_with(Key=item_key,TableName=table_name)
    publisher_handler.CLOUDWATCH_CLIENT.put_metric_data.assert_called_with(Namespace=namespace,MetricData=metrics_to_put_expected)

def _assert_error_response(result, error_type):
    """Helper function to assert that the correct type of error was thrown"""
    assert 'error' in result
    assert 'type' in result['error']
    assert result['error']['type'] == error_type
