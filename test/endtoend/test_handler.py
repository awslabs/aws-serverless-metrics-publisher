import time
import boto3
import uuid
import json
from endtoend import events
CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000
CLOUDWATCH_CLIENT = boto3.client('cloudwatch')
LOG_CLIENT = boto3.client('logs')
LAMBDA_CLIENT = boto3.client('lambda')
CLOUDFORMATION_CLIENT = boto3.client('cloudformation')
def get_current_time():
    """Get the current time."""
    return int(time.time()*CONVERT_SECONDS_TO_MILLIS_FACTOR)
def p(prefix, message):
    import uuid
    stream_name = prefix + '_' + str(uuid.uuid4())
    LOG_CLIENT.create_log_stream(
        logGroupName='DebuggingMessages',
        logStreamName=stream_name
    )
    LOG_CLIENT.put_log_events(
        logGroupName='DebuggingMessages',
        logStreamName=stream_name,
        logEvents=[
            {
                'timestamp': get_current_time(),
                'message': str(message)
            },
        ],
    )
def wait_for_metrics(start_time, period=10):
    num_seconds_in_six_minutes = 360
    stop_time = start_time + num_seconds_in_six_minutes
    while time.time() < stop_time:
        response = CLOUDWATCH_CLIENT.get_metric_data(
            MetricDataQueries=events.sample_query(),
            StartTime=start_time,
            EndTime=time.time()
            )['MetricDataResults']
        if len(response[0]['Values']) != 0:
            p("results", str(response))
            return response[0]['Values'][0]
        time.sleep(period)
def test_end_to_end():
    start_time = time.time()
    #TEMPO
    #test_stack_name = 'DemoStack'
    test_stack_name = 'metricpublisherapp-Beta'
    logger_name = 'MetricLogger'
    publisher_name = 'MetricPublisher'
    logger_physical_id = ""
    publisher_physical_id = ""
    stack_resources = CLOUDFORMATION_CLIENT.list_stack_resources(
        StackName=test_stack_name
    )['StackResourceSummaries']
    for resource in stack_resources:
        if 'LogicalResourceId' not in resource:
            continue
        if resource['LogicalResourceId'] == logger_name:
            logger_physical_id = resource['PhysicalResourceId']
        if resource['LogicalResourceId'] == publisher_name:
            publisher_physical_id = resource['PhysicalResourceId']
    event = dict(events.standard_valid_input())
    p("lambda_name",logger_physical_id)
    response = LAMBDA_CLIENT.invoke(
        FunctionName='DemoStack-MetricLogger-13XGI2CJEW8C9',
        Payload=json.dumps(event)
    )
    p("logger response", str(response))
    result = wait_for_metrics(start_time)
    expected_result = 17
    assert result == expected_result
