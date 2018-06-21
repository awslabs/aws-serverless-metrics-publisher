import json
import pytest
import events
from jsonschema import ValidationError
import mock
from pytest_mock import mocker
import metricpublisher.lambda_handler
import metricpublisher.config


def test_standard_valid_input():
    """Test to make sure a standard valid input passes the JSON schema"""
    data = events.standard_valid_input()
    assert metricpublisher.lambda_handler.log_event(data,None) == None

def test_basic_valid_input():
    """Test to make sure a minimalistic input passes the JSON schema"""
    data = events.basic_valid_input()
    assert metricpublisher.lambda_handler.log_event(data,None) == None

def test_multiple_metrics_input():
    """Test to validate that the option to input multiple metrics simultaneously is available."""
    data = events.multiple_metrics_input()
    assert metricpublisher.lambda_handler.log_event(data,None) == None

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

def test_log_event(mocker):
    """Test to ensure that log_event is called with the correct parameters."""
    mocker.patch.object(metricpublisher.lambda_handler, 'log_event')
    metricpublisher.lambda_handler.log_event.return_value = None
    data = events.standard_valid_input()
    assert metricpublisher.lambda_handler.log_event(data, None) == None
    metricpublisher.lambda_handler.log_event.assert_called_with(data, None)

def test_create_log_stream(mocker):
    """Test to ensure that create_log_stream is called with the correct parameters."""
    data = events.standard_valid_input()
    log_stream_name = metricpublisher.lambda_handler.NAMESPACE + '_' + data["request_id"]
    log_group_name = metricpublisher.lambda_handler.LOG_GROUP_NAME
    mocker.patch.object(metricpublisher.lambda_handler, 'CLIENT')
    assert metricpublisher.lambda_handler.log_event(data, None) == None
    metricpublisher.lambda_handler.CLIENT.create_log_stream.assert_called_with(logGroupName=log_group_name, logStreamName=log_stream_name)


def _assert_error_response(result, error_type):
    """Helper function to assert that the correct type of error was thrown"""
    assert 'error' in result
    assert 'type' in result['error']
    assert result['error']['type'] == error_type
