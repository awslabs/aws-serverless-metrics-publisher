import json
import pytest
import events
from jsonschema import ValidationError
from pytest_mock import mocker
import time
import itertools
import metricpublisher.lambda_handler
import metricpublisher.schema

CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000


def test_standard_valid_input():
    """Test to make sure a standard valid input passes the JSON schema"""
    data = events.standard_valid_input()
    assert metricpublisher.schema._validate(data,"log_event.json") == None

def test_basic_valid_input():
    """Test to make sure a minimalistic input passes the JSON schema"""
    data = events.basic_valid_input()
    assert metricpublisher.schema._validate(data,"log_event.json") == None

def test_multiple_metrics_input():
    """Test to validate that the option to input multiple metrics simultaneously is available."""
    data = events.multiple_metrics_input()
    assert metricpublisher.schema._validate(data,"log_event.json") == None

def test_value_and_statistic_values_both_included():
    """Test to assert that customer cannot pass in both 'value' and
    'statistic_values' in the input. (They are mutually exclusive)."""
    data = events.value_and_statistic_values_both_included()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_missing_value_and_statistic_values():
    """Test to make sure at least one of 'value' or 'statistic_values' is present"""
    data = events.missing_value_and_statistic_values()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_missing_request_id():
    """Test to make sure a request_id is passed in by the customer"""
    data = events.missing_request_id()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_missing_metric_name():
    """Test to make sure a metric name is passed in by the customer"""
    data = events.missing_metric_name()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_statistic_values_missing_sum():
    """Test to make sure that 'Sum' is present when 'statistic_values' is"""
    data = events.statistic_values_missing_sum()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_unit_type_not_available():
    """Test to make sure that customer must pass in a valid unit type"""
    data = events.unit_type_not_available()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_storage_resolution_type_invalid():
    """Test to make sure the input type of 'storage_resolution' is valid"""
    data = events.storage_resolution_type_invalid()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_dimension_type_invalid():
    """Test to make sure the input type of 'dimension' is valid"""
    data = events.dimension_type_invalid()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_dimension_item_type_invalid():
    """Test to make sure the input type of each item in
    the 'dimension' Array is valid."""
    data = events.dimension_item_type_invalid()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_dimension_item_wrong_property():
    """Test to make sure the input type of each item in
    the 'dimension' Array is valid."""
    data = events.dimension_item_wrong_property()
    _assert_error_response(
        metricpublisher.lambda_handler.log_event(data,None),"ValidationError"
    )

def test_log_event_client_function_calls(mocker):
    """Test to ensure that create_log_stream and put_log_events are called with the correct parameters."""
    mocker.patch.object(metricpublisher.lambda_handler, 'get_current_time')
    current_time = int(time.time()*CONVERT_SECONDS_TO_MILLIS_FACTOR)
    metricpublisher.lambda_handler.get_current_time.return_value = current_time
    mocker.patch.object(metricpublisher.lambda_handler,'LOG_CLIENT')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_log_group_name')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_namespace')
    metricpublisher.lambda_handler.get_log_group_name.return_value = 'metricPublisherAppLogGroup'
    metricpublisher.lambda_handler.get_namespace.return_value = 'metricPublisherAppNamespace'
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
    assert metricpublisher.lambda_handler.log_event(data, None) == None
    metricpublisher.lambda_handler.LOG_CLIENT.create_log_stream.assert_called_with(logGroupName=log_group_name, logStreamName=log_stream_name)
    metricpublisher.lambda_handler.LOG_CLIENT.put_log_events.assert_called_with(logGroupName=log_group_name, logStreamName=log_stream_name,logEvents = log_events)

def test_batch_metrics_client_function_call(mocker):
    """Test to ensure that get_log_events was called with the correct input."""
    log_group_name = 'metricPublisherAppLogGroup'
    namespace = 'metricPublisherAppNamespace'
    num_iters = 3
    data = events.basic_valid_input()
    stream_name = '_'.join((namespace, data['request_id']))
    stream_names = list(itertools.repeat(stream_name,num_iters))
    get_log_events_response = {
        'events': [
            {
                'message': str({
                    'metric_data': [
                        {
                            'metric_name': 'theMetricname',
                            'value': 123
                        }
                    ],
                    'request_id': data['request_id']
                })
            }
        ],
    }
    single_metric = {
        "metric_name": "theMetricname",
        "value": 123
    }
    batch_metrics_expected_response = list(itertools.repeat(single_metric,num_iters))
    mocker.patch.object(metricpublisher.lambda_handler, 'LOG_CLIENT')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_log_group_name')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_namespace')
    metricpublisher.lambda_handler.LOG_CLIENT.get_log_events.return_value = get_log_events_response
    metricpublisher.lambda_handler.get_log_group_name.return_value = log_group_name
    metricpublisher.lambda_handler.get_namespace.return_value = namespace
    assert metricpublisher.lambda_handler.batch_metrics(stream_names) == batch_metrics_expected_response
    metricpublisher.lambda_handler.LOG_CLIENT.get_log_events.assert_called_with(logGroupName=log_group_name,logStreamName=stream_name)

def test_batch_metrics_multiple_metrics(mocker):
    """Test to ensure that batch_metrics works properly
    when log events contain more then one metric."""
    log_group_name = 'metricPublisherAppLogGroup'
    namespace = 'metricPublisherAppNamespace'
    num_iters = 3
    data = events.basic_valid_input()
    stream_name = '_'.join((namespace, data['request_id']))
    stream_names = list(itertools.repeat(stream_name,num_iters))
    get_log_events_response = {
        'events': [
            {
                'message': str({
                    'metric_data': [
                        {
                            'metric_name': 'metricName1',
                            'value': 123
                        },
                        {
                            'metric_name': 'metricName2',
                            'value': 234
                        },
                        {
                            'metric_name': 'metricName3',
                            'value': 345
                        }
                  ],
                    'request_id': data['request_id']
                })
            }
        ],
    }
    single_metric_1 = {
        "metric_name": "metricName1",
        "value": 123
    }
    single_metric_2 = {
        "metric_name": "metricName2",
        "value": 234
    }
    single_metric_3 = {
        "metric_name": "metricName3",
        "value": 345
    }
    combined_metrics_list = [single_metric_1,single_metric_2,single_metric_3]
    batch_metrics_expected_response = combined_metrics_list + combined_metrics_list + combined_metrics_list
    mocker.patch.object(metricpublisher.lambda_handler, 'LOG_CLIENT')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_log_group_name')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_namespace')
    metricpublisher.lambda_handler.LOG_CLIENT.get_log_events.return_value = get_log_events_response
    metricpublisher.lambda_handler.get_log_group_name.return_value = log_group_name
    metricpublisher.lambda_handler.get_namespace.return_value = namespace
    assert metricpublisher.lambda_handler.batch_metrics(stream_names) == batch_metrics_expected_response

def test_format_metric_simple_case():
    metric_before = events.simple_metric_before()
    metric_expected = events.simple_metric_after_expected()
    result = metricpublisher.lambda_handler.format_metric(metric_before)
    assert result == metric_expected

def test_format_metric_complex_case():
    metric_before = events.complex_metric_before()
    metric_expected = events.complex_metric_after_expected()
    result = metricpublisher.lambda_handler.format_metric(metric_before)
    assert result == metric_expected


def _assert_error_response(result, error_type):
    """Helper function to assert that the correct type of error was thrown"""
    assert 'error' in result
    assert 'type' in result['error']
    assert result['error']['type'] == error_type
