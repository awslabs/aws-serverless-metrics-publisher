import events
import time
import boto3
from pytest_mock import mocker
import metricpublisher.lambda_handler
import metricpublisher.schema


CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000
CLOUDWATCH_CLIENT = boto3.client('cloudwatch')
LOG_CLIENT = boto3.client('logs')


def wait_until_events_put(start_time, timeout=60, period=0.5):
    """Helper function to account for latency
    in put_log_events API"""
    stop_time = time.time() + timeout
    while time.time() < stop_time:
        log_events = LOG_CLIENT.filter_log_events(
            logGroupName='metricPublisherAppLogGroup',
            startTime=start_time,
            endTime=int(time.time()*CONVERT_SECONDS_TO_MILLIS_FACTOR)
        )['events']
        if len(log_events) >= 5:
            return True
    return False

def wait_until_metrics_published(timeout=60, period=0.5):
    """Helper function to account for latency
    in put_metric_data API"""
    number_of_metrics_expected = 34
    stop_time = time.time() + timeout
    while time.time() < stop_time:
        if metricpublisher.lambda_handler.metric_publisher(None, None) == 34:
            return True
        time.sleep(period)
    return False

def wait_until_data_appears(queries, start_time, timeout=60, period=0.5):
    """Helper function to account for latency
    in get_metric_data API"""
    stop_time = time.time() + timeout
    while time.time() < stop_time:
        response = CLOUDWATCH_CLIENT.get_metric_data(
            MetricDataQueries=queries,
            StartTime=start_time,
            EndTime=time.time()
        )
        finished = True
        for query in response['MetricDataResults']:
            if len(query['Values']) == 0:
                finished = False
                break
        if finished:
            values = [response['MetricDataResults'][i]['Values'][0] for i in range(10)]
            expected_values = [50, 30, 60, 5, 217, 1, 555, 43.4, 30, 41]
            if values == expected_values:
                return True
        time.sleep(period)

def test_overall_flow_mocking_env_vars(mocker):
    """Test the basic flow of the app using mockers
    for the environment variables."""
    mocker.patch.object(metricpublisher.lambda_handler, 'get_log_group_name')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_table_name')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_namespace')
    metricpublisher.lambda_handler.get_log_group_name.return_value = 'metricPublisherAppLogGroup'
    metricpublisher.lambda_handler.get_table_name.return_value = 'metricPublisherAppDynamoDBTable'
    metricpublisher.lambda_handler.get_namespace.return_value = 'metricPublisherAppNamespace'
    start_time = int(time.time()) - 60
    data = events.input_events()
    for event in data:
        metricpublisher.lambda_handler.log_event(event, None)
    if not wait_until_events_put((start_time + 60)*CONVERT_SECONDS_TO_MILLIS_FACTOR):
        raise Exception("TimeoutError")
    if not wait_until_metrics_published():
        raise Exception("Timeout Error")
    sample_queries = events.sample_queries()
    response = wait_until_data_appears(sample_queries, start_time)
    if response == None:
        raise Exception("Timeout Error")
