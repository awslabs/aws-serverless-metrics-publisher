"""Collection of events for integration tests."""
import pytest
import uuid
import time

@pytest.fixture()
def input_events():
    new_uuid = str(uuid.uuid4())
    request_id = "request_id_" + new_uuid
    input_1 = {
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
    new_uuid = str(uuid.uuid4())
    request_id = "request_id_" + new_uuid
    input_2 = {
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
    new_uuid = str(uuid.uuid4())
    request_id = "request_id_" + new_uuid
    input_3 = {
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
                }
            }
        ]
    }
    new_uuid = str(uuid.uuid4())
    request_id = "request_id_" + new_uuid
    the_data = []
    for i in range(20):
        single_point = {
            "metric_name": "theMetricName4",
            "dimensions": [
                {
                    "name": "test_name",
                    "value": "test_value"
                }
            ],
            "timestamp": time.time(),
            "value": 42
        }
        the_data.append(single_point)
    input_4 = {
        "request_id": request_id,
        "metric_data": the_data
    }
    new_uuid = str(uuid.uuid4())
    request_id = "request_id_" + new_uuid
    the_data = []
    for i in range(10):
        single_point = {
            "metric_name": "theMetricName4",
            "dimensions": [
                {
                    "name": "test_name",
                    "value": "test_value"
                }
            ],
            "timestamp": time.time(),
            "value": 39
        }
        the_data.append(single_point)
    input_5 = {
        "request_id": request_id,
        "metric_data": the_data
    }
    return [input_1, input_2, input_3, input_4, input_5]

@pytest.fixture()
def sample_queries():
    return [
        {
            'Id': 'id_1',
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
                'Period': 1,
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
                'Period': 1,
                'Stat': 'Average'
            }
        },
        {
            'Id': 'id_3',
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
                'Period': 1,
                'Stat': 'Sum'
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
                'Period': 1,
                'Stat': 'SampleCount'
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
                'Period': 1,
                'Stat': 'Sum'
            }
        },
        {
            'Id': 'id_6',
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
                'Stat': 'Minimum'
            }
        },
        {
            'Id': 'id_7',
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
                'Stat': 'Maximum'
            }
        },
        {
            'Id': 'id_8',
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
                'Stat': 'Average'
            }
        },
        {
            'Id': 'id_9',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'metricPublisherAppNamespace',
                    'MetricName': 'theMetricName4',
                    'Dimensions': [
                        {
                            'Name': 'test_name',
                            'Value': 'test_value'
                        }
                    ]
                },
                'Period': 5,
                'Stat': 'SampleCount'
            }
        },
        {
            'Id': 'id_10',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'metricPublisherAppNamespace',
                    'MetricName': 'theMetricName4',
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
