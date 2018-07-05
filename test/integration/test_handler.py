import events
import time
import boto3
from pytest_mock import mocker
import metricpublisher.lambda_handler
import metricpublisher.schema


CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000
CLOUDWATCH_CLIENT = boto3.client('cloudwatch')
NUM_RETRIES = 5

def test_overall_flow_mocking_env_vars_basic(mocker, retry_count=0):
    """Test the basic flow of the app
    given basic input, using mockers
    for the environment variables."""
    if retry_count == 5:
        raise Exception('Test took too long to run.')
    retry_count += 1
    data = events.input_event_basic()
    mocker.patch.object(metricpublisher.lambda_handler, 'get_log_group_name')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_table_name')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_namespace')
    metricpublisher.lambda_handler.get_log_group_name.return_value = 'metricPublisherAppLogGroup'
    metricpublisher.lambda_handler.get_table_name.return_value = 'metricPublisherAppDynamoDBTable'
    metricpublisher.lambda_handler.get_namespace.return_value = 'metricPublisherAppNamespace'
    start_time = int(time.time()) - 60
    metricpublisher.lambda_handler.log_event(data, None)
    metricpublisher.lambda_handler.metric_publisher(None, None)
    end_time = int(time.time()) + 2
    response = CLOUDWATCH_CLIENT.get_metric_data(
        MetricDataQueries= events.sample_query_basic(),
        StartTime=start_time,
        EndTime=end_time
    )
    sleep_count = 1
    for retry in range(NUM_RETRIES):
        finished = True
        for query in response['MetricDataResults']:
            if len(query['Values']) == 0:
                finished = False
                break
        if finished:
            break
        time.sleep(sleep_count)
        sleep_count += 1
        response = CLOUDWATCH_CLIENT.get_metric_data(
            MetricDataQueries= events.sample_query_basic(),
            StartTime=start_time,
            EndTime=time.time()
        )
    try:
        assert response['MetricDataResults'][0]['Values'][0] == 50
    except IndexError:
        test_overall_flow_mocking_env_vars_basic(mocker, retry_count)

def test_overall_flow_mocking_env_vars_standard(mocker, retry_count=0):
    """Test the basic flow of the app
    given standard input, using mockers
    for the environment variables."""
    if retry_count == 5:
        raise Exception('Test took too long to run.')
    retry_count += 1
    data = events.input_events_standard()
    mocker.patch.object(metricpublisher.lambda_handler, 'get_log_group_name')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_table_name')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_namespace')
    metricpublisher.lambda_handler.get_log_group_name.return_value = 'metricPublisherAppLogGroup'
    metricpublisher.lambda_handler.get_table_name.return_value = 'metricPublisherAppDynamoDBTable'
    metricpublisher.lambda_handler.get_namespace.return_value = 'metricPublisherAppNamespace'
    start_time = int(time.time()) - 60
    metricpublisher.lambda_handler.log_event(data, None)
    metricpublisher.lambda_handler.metric_publisher(None, None)
    end_time = int(time.time()) + 2
    response = CLOUDWATCH_CLIENT.get_metric_data(
        MetricDataQueries= events.sample_queries_standard(),
        StartTime=start_time,
        EndTime=end_time
    )
    sleep_count = 1
    for retry in range(NUM_RETRIES):
        finished = True
        for query in response['MetricDataResults']:
            if len(query['Values']) == 0:
                finished = False
                break
        if finished:
            break
        time.sleep(sleep_count)
        sleep_count += 1
        response = CLOUDWATCH_CLIENT.get_metric_data(
            MetricDataQueries= events.sample_queries_standard(),
            StartTime=start_time,
            EndTime=time.time()
        )
    try:
        assert response['MetricDataResults'][0]['Values'][0] == 30
        assert response['MetricDataResults'][1]['Values'][0] == 60
    except IndexError:
        test_overall_flow_mocking_env_vars_standard(mocker, retry_count)

def test_overall_flow_mocking_env_vars_complex(mocker, retry_count=0):
    """Test the basic flow of the app
    using more complex input, using mockers
    for the environment variables."""
    if retry_count == 5:
        raise Exception('Test took too long to run.')
    retry_count += 1
    data = events.input_events_complex()
    mocker.patch.object(metricpublisher.lambda_handler, 'get_log_group_name')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_table_name')
    mocker.patch.object(metricpublisher.lambda_handler, 'get_namespace')
    metricpublisher.lambda_handler.get_log_group_name.return_value = 'metricPublisherAppLogGroup'
    metricpublisher.lambda_handler.get_table_name.return_value = 'metricPublisherAppDynamoDBTable'
    metricpublisher.lambda_handler.get_namespace.return_value = 'metricPublisherAppNamespace'
    start_time = int(time.time()) - 60
    metricpublisher.lambda_handler.log_event(data, None)
    metricpublisher.lambda_handler.metric_publisher(None, None)
    end_time = int(time.time()) + 2
    response = CLOUDWATCH_CLIENT.get_metric_data(
        MetricDataQueries= events.sample_queries_complex(),
        StartTime=start_time,
        EndTime=end_time
    )
    sleep_count = 1
    for retry in range(NUM_RETRIES):
        finished = True
        for query in response['MetricDataResults']:
            if len(query['Values']) == 0:
                finished = False
                break
        if finished:
            break
        time.sleep(sleep_count)
        sleep_count += 1
        response = CLOUDWATCH_CLIENT.get_metric_data(
            MetricDataQueries= events.sample_queries_complex(),
            StartTime=start_time,
            EndTime=time.time()
        )
    try:
        assert response['MetricDataResults'][0]['Values'][0] == 5
        assert response['MetricDataResults'][1]['Values'][0] == 217
        assert response['MetricDataResults'][2]['Values'][0] == 1
        assert response['MetricDataResults'][3]['Values'][0] == 555
        assert response['MetricDataResults'][4]['Values'][0] == 43.4

    except IndexError:
        test_overall_flow_mocking_env_vars_complex(mocker, retry_count)
