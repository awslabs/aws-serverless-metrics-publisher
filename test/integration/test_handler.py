import events
import time
import boto3
from pytest_mock import mocker
import metricpublisher.lambda_handler
import metricpublisher.schema


CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000
CLOUDWATCH_CLIENT = boto3.client('cloudwatch')
LOG_CLIENT = boto3.client('logs')


def wait_until_events_put(start_time, timeout=20, period=0.5):
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
    stop_time = time.time() + timeout
    while time.time() < stop_time:
        if metricpublisher.lambda_handler.metric_publisher(None, None) != 0:
            return True
        time.sleep(period)
    return False

def check_if_many_events_published(results):
    """Helper function to ensure that
    all of the data from the last test
    case has published."""
    if len(results[8]['Values']) == 0:
        return False
    if len(results[9]['Values']) == 0:
        return False
    if results[8]['Values'][0] != 30:
        return False
    if results[9]['Values'][0] != 41:
        return False
    return True

def wait_until_data_appears(queries, start_time, timeout=120, period=0.5):
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
        if not check_if_many_events_published(response['MetricDataResults']):
            finished = False
        if finished:
            return response
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
    assert response['MetricDataResults'][0]['Values'][0] == 50
    assert response['MetricDataResults'][1]['Values'][0] == 30
    assert response['MetricDataResults'][2]['Values'][0] == 60
    assert response['MetricDataResults'][3]['Values'][0] == 5
    assert response['MetricDataResults'][4]['Values'][0] == 217
    assert response['MetricDataResults'][5]['Values'][0] == 1
    assert response['MetricDataResults'][6]['Values'][0] == 555
    assert response['MetricDataResults'][7]['Values'][0] == 43.4
    assert response['MetricDataResults'][8]['Values'][0] == 30
    assert response['MetricDataResults'][9]['Values'][0] == 41
