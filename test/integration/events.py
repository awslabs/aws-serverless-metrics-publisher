"""Collection of events for integration tests."""
import pytest
import uuid
import time


@pytest.fixture()
def input_event_basic():
    new_uuid = str(uuid.uuid4())
    request_id = "request_id_" + new_uuid
    input = {
        "request_id": request_id,
        "metric_data": [
            {
                "metric_name": "theMetricName1",
                "dimensions": [
                    {
                        "name": "test_name",
                        "value": "test_value"
                    }
                ],
                "timestamp": time.time(),
                "value":50,
            }
        ]
    }
    return input

@pytest.fixture()
def input_events_standard():
    new_uuid = str(uuid.uuid4())
    request_id = "request_id_" + new_uuid
    input = {
        "request_id": request_id,
        "metric_data": [
            {
                "metric_name": "theMetricName2",
                "dimensions": [
                    {
                        "name": "test_name",
                        "value": "test_value"
                    }
                ],
                "timestamp": time.time(),
                "value":25
            },
            {
                "metric_name": "theMetricName2",
                "dimensions": [
                    {
                        "name": "test_name",
                        "value": "test_value"
                    }
                ],
                "timestamp": time.time(),
                "value":35
            }
        ]
    }
    return input

@pytest.fixture()
def input_events_complex():
    new_uuid = str(uuid.uuid4())
    request_id = "request_id_" + new_uuid
    input = {
        "request_id": request_id,
        "metric_data": [
            {
                "metric_name": "theMetricName3",
                "dimensions": [
                    {
                        "name": "test_name",
                        "value": "test_value"
                    }
                ],
                "timestamp": time.time(),
                "statistic_values": {
                    "sample_count": 5,
                    "sum": 217,
                    "minimum": 1,
                    "maximum": 555
                },
            }
        ]
    }
    return input

@pytest.fixture()
def sample_query_basic():
    return [
        {
            'Id': 'the_id',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'metricPublisherAppNamespace',
                    'MetricName': 'theMetricName1',
                    'Dimensions': [
                        {
                            'Name': 'test_name',
                            'Value': 'test_value'
                        }
                    ]
                },
                'Period': 5,
                'Stat': 'Average'
            }
        }
    ]

@pytest.fixture()
def sample_queries_standard():
    return [
        {
            'Id': 'id_1',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'metricPublisherAppNamespace',
                    'MetricName': 'theMetricName2',
                    'Dimensions': [
                        {
                            'Name': 'test_name',
                            'Value': 'test_value'
                        }
                    ]
                },
                'Period': 5,
                'Stat': 'Average'
            }
        },
        {
            'Id': 'id_2',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'metricPublisherAppNamespace',
                    'MetricName': 'theMetricName2',
                    'Dimensions': [
                        {
                            'Name': 'test_name',
                            'Value': 'test_value'
                        }
                    ]
                },
                'Period': 5,
                'Stat': 'Sum'
            }
        }
    ]

@pytest.fixture()
def sample_queries_complex():
    return [
        {
            'Id': 'id_1',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'metricPublisherAppNamespace',
                    'MetricName': 'theMetricName3',
                    'Dimensions': [
                        {
                            'Name': 'test_name',
                            'Value': 'test_value'
                        }
                    ]
                },
                'Period': 1,
                'Stat': 'SampleCount'
            }
        },
        {
            'Id': 'id_2',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'metricPublisherAppNamespace',
                    'MetricName': 'theMetricName3',
                    'Dimensions': [
                        {
                            'Name': 'test_name',
                            'Value': 'test_value'
                        }
                    ]
                },
                'Period': 5,
                'Stat': 'Sum'
            }
        },
        {
            'Id': 'id_3',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'metricPublisherAppNamespace',
                    'MetricName': 'theMetricName3',
                    'Dimensions': [
                        {
                            'Name': 'test_name',
                            'Value': 'test_value'
                        }
                    ]
                },
                'Period': 5,
                'Stat': 'Minimum'
            }
        },
        {
            'Id': 'id_4',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'metricPublisherAppNamespace',
                    'MetricName': 'theMetricName3',
                    'Dimensions': [
                        {
                            'Name': 'test_name',
                            'Value': 'test_value'
                        }
                    ]
                },
                'Period': 5,
                'Stat': 'Maximum'
            }
        },
        {
            'Id': 'id_5',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'metricPublisherAppNamespace',
                    'MetricName': 'theMetricName3',
                    'Dimensions': [
                        {
                            'Name': 'test_name',
                            'Value': 'test_value'
                        }
                    ]
                },
                'Period': 5,
                'Stat': 'Average'
            }
        }
    ]
