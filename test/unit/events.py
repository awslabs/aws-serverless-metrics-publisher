"""Collection of events for schema validation"""
import pytest
import uuid

@pytest.fixture()
def standard_valid_input():
    new_uuid = str(uuid.uuid4())
    request_id = "request_id_" + new_uuid
    return {
        "request_id": request_id,
        "metric_data": [
            {
                "metric_name": "theMetricname",
                "dimensions": [
                    {
                        "name": "thename1",
                        "value": "thevalue1"
                    },
                    {
                        "name": "thename2",
                        "value": "thevalue2"
                    }
                ],
                "timestamp": 1528236844480,
                "statistic_values": {
                    "sample_count": 12.17,
                    "sum": 12.17,
                    "minimum": 12.17,
                    "maximum": 12.17
                },
                "unit": "Seconds",
                "storage_resolution": 12
            }
        ]
    }

@pytest.fixture()
def basic_valid_input():
    new_uuid = str(uuid.uuid4())
    request_id = "request_id_" + new_uuid
    return {
        "request_id": request_id,
        "metric_data": [
            {
                "metric_name": "theMetricName",
                "value":123,
            }
        ]
    }

@pytest.fixture()
def multiple_metrics_input():
    new_uuid = str(uuid.uuid4())
    request_id = "request_id_" + new_uuid
    return {
        "request_id": request_id,
        "metric_data": [
            {
                "metric_name": "theMetricname",
                "dimensions": [
                    {
                        "name": "thename1",
                        "value": "thevalue1"
                    },
                    {
                        "name": "thename2",
                        "value": "thevalue2"
                    }
                ],
                "timestamp": 1528236844480,
                "statistic_values": {
                    "sample_count": 12.17,
                    "sum": 12.17,
                    "minimum": 12.17,
                    "maximum": 12.17
                },
                "unit": "Seconds",
                "storage_resolution": 12
            },
            {
                "metric_name": "theMetricname2",
                "dimensions": [
                    {
                        "name": "thename1",
                        "value": "thevalue1"
                    },
                    {
                        "name": "thename2",
                        "value": "thevalue2"
                    }
                ],
                "timestamp": 1528236844480,
                "value":123,
                "unit": "Seconds",
                "storage_resolution": 12
            }
        ]
    }

@pytest.fixture()
def value_and_statistic_values_both_included():
    return {
        "request_id": "an id",
        "metric_data": [
            {
                "metric_name": "theMetricname",
                "dimensions": [
                    {
                        "name": "thename1",
                        "value": "thevalue1"
                    },
                    {
                        "name": "thename2",
                        "value": "thevalue2"
                    }
                ],
                "timestamp": 1528236844480,
                "value": 123,
                "statistic_values": {
                    "sample_count": 12.17,
                    "sum": 12.17,
                    "minimum": 12.17,
                    "maximum": 12.17
                },
                "unit": "Seconds",
                "storage_resolution": 12
            }
        ]
    }

@pytest.fixture()
def missing_value_and_statistic_values():
    return {
        "request_id": "the_id",
        "metric_data": [
            {
                "metric_name": "the_metric_name",
                "dimensions": [
                    {
                        "name": "the_name_1",
                        "value": "the_value_1"
                    },
                    {
                        "name": "the_name_2",
                        "value": "the_value_2"
                    }
                ],
                "timestamp": 1528236844480,
                "unit": "Seconds",
                "storage_resolution": 12
            }
        ]
    }

@pytest.fixture()
def missing_request_id():
    return {
        "metric_data": [
            {
                "metric_name": "the_metric_name",
                "dimensions": [
                    {
                        "name": "the_name_1",
                        "value": "the_value_1"
                    },
                    {
                        "name": "the_name_2",
                        "value": "the_value_2"
                    }
                ],
                "timestamp": 1528236844480,
                "value":123,
                "unit": "Seconds",
                "storage_resolution": 12
            }
        ]
    }

@pytest.fixture()
def missing_metric_name():
    return {
        "request_id": "the_id",
        "metric_data": [
            {
                "dimensions": [
                    {
                        "name": "the_name_1",
                        "value": "the_value_1"
                    },
                    {
                        "name": "the_name_2",
                        "value": "the_value_2"
                    }
                ],
                "timestamp": 1528236844480,
                "value":123,
                "unit": "Seconds",
                "storage_resolution": 12
            }
        ]
    }

@pytest.fixture()
def statistic_values_missing_sum():
    return {
        "request_id": "the_id",
        "metric_data": [
            {
                "metric_name": "the_metric_name",
                "dimensions": [
                    {
                        "name": "the_name_1",
                        "value": "the_value_1"
                    },
                    {
                        "name": "the_name_2",
                        "value": "the_value_2"
                    }
                ],
                "timestamp": 1528236844480,
                "statistic_values": {
                    "sample_count": 12.17,
                    "minimum": 12.17,
                    "maximum": 12.17
                },
                "unit": "Seconds",
                "storage_resolution": 12
            }
        ]
    }

@pytest.fixture()
def unit_type_not_available():
    return {
        "request_id": "the_id",
        "metric_data": [
            {
                "metric_name": "the_metric_name",
                "dimensions": [
                    {
                        "name": "the_name_1",
                        "value": "the_value_1"
                    },
                    {
                        "name": "the_name_2",
                        "value": "the_value_2"
                    }
                ],
                "timestamp": 1528236844480,
                "statistic_values": {
                    "sample_count": 12.17,
                    "sum": 12.17,
                    "minimum": 12.17,
                    "maximum": 12.17
                },
                "unit": "minutes",
                "storage_resolution": 12
            }
        ]
    }

@pytest.fixture()
def storage_resolution_type_invalid():
    return {
        "request_id": "the_id",
        "metric_data": [
            {
                "metric_name": "the_metric_name",
                "dimensions": [
                    {
                        "name": "the_name_1",
                        "value": "the_value_1"
                    },
                    {
                        "name": "the_name_2",
                        "value": "the_value_2"
                    }
                ],
                "timestamp": 1528236844480,
                "statistic_values": {
                    "sample_count": 12.17,
                    "sum": 12.17,
                    "minimum": 12.17,
                    "maximum": 12.17
                },
                "unit": "Seconds",
                "storage_resolution": "12"
            }
        ]
    }

@pytest.fixture()
def dimension_type_invalid():
    return {
        "request_id": "an id",
        "metric_data": [
            {
                "metric_name": "theMetricname",
                "dimensions": (
                    {
                        "name": "thename1",
                        "value": "thevalue1"
                    },
                    {
                        "name": "thename2",
                        "value": "thevalue2"
                    }
                ),
                "timestamp": 1528236844480,
                "statistic_values": {
                    "sample_count": 12.17,
                    "sum": 12.17,
                    "minimum": 12.17,
                    "maximum": 12.17
                },
                "unit": "Seconds",
                "storage_resolution": 12
            }
        ]
    }

@pytest.fixture()
def dimension_item_type_invalid():
    return {
        "request_id": "an id",
        "metric_data": [
            {
                "metric_name": "theMetricname",
                "dimensions": [
                    {
                        "name": "thename1",
                        "value": "thevalue1"
                    },
                    "a string"
                ],
                "timestamp": 1528236844480,
                "statistic_values": {
                    "sample_count": 12.17,
                    "sum": 12.17,
                    "minimum": 12.17,
                    "maximum": 12.17
                },
                "unit": "Seconds",
                "storage_resolution": 12
            }
        ]
    }

@pytest.fixture()
def dimension_item_wrong_property():
    return {
        "request_id": "an id",
        "metric_data": [
            {
                "metric_name": "theMetricname",
                "dimensions": [
                    {
                        "name": "thename1",
                        "value": "thevalue1"
                    },
                    {
                        "name": "thename2",
                        "Value": "thevalue2"
                    }
                ],
                "timestamp": 1528236844480,
                "statistic_values": {
                    "sample_count": 12.17,
                    "sum": 12.17,
                    "minimum": 12.17,
                    "maximum": 12.17
                },
                "unit": "Seconds",
                "storage_resolution": 12
            }
        ]
    }

@pytest.fixture()
def simple_metric_before():
    return {
        "metric_name": "theMetricName",
        "value": 123,
    }

@pytest.fixture()
def simple_metric_after_expected():
    return {
        "MetricName":"theMetricName",
        "Value": 123,
    }

@pytest.fixture()
def complex_metric_before():
    return {
        "metric_name": "theMetricname",
        "dimensions": [
            {
                "name": "thename1",
                "value": "thevalue1"
            },
            {
                "name": "thename2",
                "value": "thevalue2"
            }
        ],
        "timestamp": 1528236844480,
        "statistic_values": {
            "sample_count": 12.17,
            "sum": 12.17,
            "minimum": 12.17,
            "maximum": 12.17
        },
        "unit": "Seconds",
        "storage_resolution": 12
    }

@pytest.fixture()
def complex_metric_after_expected():
    return {
        "MetricName": "theMetricname",
        "Dimensions": [
            {
                "Name": "thename1",
                "Value": "thevalue1"
            },
            {
                "Name": "thename2",
                "Value": "thevalue2"
            }
        ],
        "Timestamp": 1528236844480,
        "StatisticValues": {
            "SampleCount": 12.17,
            "Sum": 12.17,
            "Minimum": 12.17,
            "Maximum": 12.17
        },
        "Unit": "Seconds",
        "StorageResolution": 12
    }

@pytest.fixture()
def normal_log_streams():
    return [
        {
            u'firstEventTimestamp': 1530205415139,
            u'lastEventTimestamp': 1530205415139,
            u'creationTime': 1530205411189,
            u'uploadSequenceToken': u'49585782821487087039627614662111906038784367900020033842',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_68fccacd-f115-4393-871f-705447d02dda',
            u'lastIngestionTime': 1530205411271,
            u'arn': u'arn: aws: logs: us-east-1: 847660965084: log-group: metricPublisherAppLogGroup: log-stream: metricPublisherAppNamespace_request_id_68fccacd-f115-4393-871f-705447d02dda',
            u'storedBytes': 0
        },
        {
            u'firstEventTimestamp': 1530205415329,
            u'lastEventTimestamp': 1530205415329,
            u'creationTime': 1530205411378,
            u'uploadSequenceToken': u'49577993470643646818846630635275346630373036422051516530',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_b6b84c50-3521-4329-82e7-a3aab342d304',
            u'lastIngestionTime': 1530205411459,
            u'arn': u'arn: aws: logs: us-east-1: 847660965084: log-group: metricPublisherAppLogGroup: log-stream: metricPublisherAppNamespace_request_id_b6b84c50-3521-4329-82e7-a3aab342d304',
            u'storedBytes': 0
        },
        {
            u'firstEventTimestamp': 1530205415517,
            u'lastEventTimestamp': 1530205415517,
            u'creationTime': 1530205411565,
            u'uploadSequenceToken': u'49578853358253728930411628432651878890366737806776214482',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_6dbc066f-ec1d-4452-a36d-26363f6729bc',
            u'lastIngestionTime': 1530205411645,
            u'arn': u'arn: aws: logs: us-east-1: 847660965084: log-group: metricPublisherAppLogGroup: log-stream: metricPublisherAppNamespace_request_id_6dbc066f-ec1d-4452-a36d-26363f6729bc',
            u'storedBytes': 0
        }
    ]

@pytest.fixture()
def several_log_streams():
    return {
        'logStreams': [
            {
                u'firstEventTimestamp': 1530207698194,
                u'lastEventTimestamp': 1530207698194,
                u'creationTime': 1530207694148,
                u'uploadSequenceToken': u'49578308592059599247367931452786885946978748512422025922',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_addc0d36-3155-499d-a048-8edd1d7ddd95',
                u'lastIngestionTime': 1530207694229,
                u'arn': u'arn: aws: logs: us-east-1: 847660965084: log-group: metricPublisherAppLogGroup: log-stream: metricPublisherAppNamespace_request_id_addc0d36-3155-499d-a048-8edd1d7ddd95',
                u'storedBytes': 0
            },
            {
                u'firstEventTimestamp': 1530207698412,
                u'lastEventTimestamp': 1530207698412,
                u'creationTime': 1530207694363,
                u'uploadSequenceToken': u'49581139916413231263843871290705327156785846599979071922',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_8c74aaa9-143f-4f01-9bc8-12be2d61b09f',
                u'lastIngestionTime': 1530207694441,
                u'arn': u'arn: aws: logs: us-east-1: 847660965084: log-group: metricPublisherAppLogGroup: log-stream: metricPublisherAppNamespace_request_id_8c74aaa9-143f-4f01-9bc8-12be2d61b09f',
                u'storedBytes': 0
            },
            {
                u'firstEventTimestamp': 1530207698645,
                u'lastEventTimestamp': 1530207698645,
                u'creationTime': 1530207694599,
                u'uploadSequenceToken': u'49577999090030023434983583228096341761855242308258326098',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_09ede3ff-b8b6-42a0-b07f-a068d80ad9cd',
                u'lastIngestionTime': 1530207694676,
                u'arn': u'arn: aws: logs: us-east-1: 847660965084: log-group: metricPublisherAppLogGroup: log-stream: metricPublisherAppNamespace_request_id_09ede3ff-b8b6-42a0-b07f-a068d80ad9cd',
                u'storedBytes': 0
            },
            {
                u'firstEventTimestamp': 1530207727387,
                u'lastEventTimestamp': 1530207727387,
                u'creationTime': 1530207723343,
                u'uploadSequenceToken': u'49578564105122387422228115007747330764121295191801983714',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_3b7e3bc3-0d54-447c-a57c-566bdb9e150e',
                u'lastIngestionTime': 1530207723432,
                u'arn': u'arn: aws: logs: us-east-1: 847660965084: log-group: metricPublisherAppLogGroup: log-stream: metricPublisherAppNamespace_request_id_3b7e3bc3-0d54-447c-a57c-566bdb9e150e',
                u'storedBytes': 0
            },
            {
                u'firstEventTimestamp': 1530207727596,
                u'lastEventTimestamp': 1530207727596,
                u'creationTime': 1530207723553,
                u'uploadSequenceToken': u'49577633063728840599792377953746771463707837255087489314',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_397c6293-2c81-4eb2-884d-fc589bd3d4a6',
                u'lastIngestionTime': 1530207723817,
                u'arn': u'arn: aws: logs: us-east-1: 847660965084: log-group: metricPublisherAppLogGroup: log-stream: metricPublisherAppNamespace_request_id_397c6293-2c81-4eb2-884d-fc589bd3d4a6',
                u'storedBytes': 0
            },
            {
                u'firstEventTimestamp': 1530207727970,
                u'lastEventTimestamp': 1530207727970,
                u'creationTime': 1530207723927,
                u'uploadSequenceToken': u'49585201660722101551809574982145209965467572678261110738',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_3c4d101e-3691-4c49-b8ae-3d111ee672ed',
                u'lastIngestionTime': 1530207724014,
                u'arn': u'arn: aws: logs: us-east-1: 847660965084: log-group: metricPublisherAppLogGroup: log-stream: metricPublisherAppNamespace_request_id_3c4d101e-3691-4c49-b8ae-3d111ee672ed',
                u'storedBytes': 0
            },
            {
                u'firstEventTimestamp': 1530207755659,
                u'lastEventTimestamp': 1530207755659,
                u'creationTime': 1530207751612,
                u'uploadSequenceToken': u'49583023662300315977855931561438919299973431053275747106',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_a83b59d5-6896-4d11-b28f-af72c8d3851c',
                u'lastIngestionTime': 1530207751696,
                u'arn': u'arn: aws: logs: us-east-1: 847660965084: log-group: metricPublisherAppLogGroup: log-stream: metricPublisherAppNamespace_request_id_a83b59d5-6896-4d11-b28f-af72c8d3851c',
                u'storedBytes': 0
            },
            {
                u'firstEventTimestamp': 1530207755856,
                u'lastEventTimestamp': 1530207755856,
                u'creationTime': 1530207751808,
                u'uploadSequenceToken': u'49576984091170065852809983543603419722473890776256497570',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_2858f1c1-31ee-48e9-91e1-953e30af16ee',
                u'lastIngestionTime': 1530207751885,
                u'arn': u'arn: aws: logs: us-east-1: 847660965084: log-group: metricPublisherAppLogGroup: log-stream: metricPublisherAppNamespace_request_id_2858f1c1-31ee-48e9-91e1-953e30af16ee',
                u'storedBytes': 0
            },
            {
                u'firstEventTimestamp': 1530207756043,
                u'lastEventTimestamp': 1530207756043,
                u'creationTime': 1530207751994,
                u'uploadSequenceToken': u'49579391000117993019634025338620304736277083209014122562',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_163c59a0-8ff2-471f-93e0-c93415e03adb',
                u'lastIngestionTime': 1530207752074,
                u'arn': u'arn: aws: logs: us-east-1: 847660965084: log-group: metricPublisherAppLogGroup: log-stream: metricPublisherAppNamespace_request_id_163c59a0-8ff2-471f-93e0-c93415e03adb',
                u'storedBytes': 0
            }
        ]
    }

@pytest.fixture()
def standard_item():
    return {
        u'Item': {
            u'cursor': {
                u'S': u'cursor_for_next_batch'
            },
            u'last_event_time': {
                u'N': u'1530207698645'
            }
        },
        'ResponseMetadata': {
            'RetryAttempts': 0,
            'HTTPStatusCode': 200,
            'RequestId': 'IAT4B0D1SOJ8JUBGF47E8C8SEVVV4KQNSO5AEMVJF66Q9ASUAAJG',
            'HTTPHeaders': {
                'x-amzn-requestid': 'IAT4B0D1SOJ8JUBGF47E8C8SEVVV4KQNSO5AEMVJF66Q9ASUAAJG',
                'content-length': '89',
                'server': 'Server',
                'connection': 'keep-alive',
                'x-amz-crc32': '2052685527',
                'content-type': 'application/x-amz-json-1.0'
            }
        }
    }

@pytest.fixture()
def metrics_before():
    return [
        {
            'metric_name': 'theMetricName',
            'value': 130
        },
        {
            'metric_name': 'theMetricName',
            'value': 45
        },
        {
            'metric_name': 'theMetricName',
            'value': 576
        },
        {
            'metric_name': 'theMetricName',
            'value': 241
        },
        {
            'metric_name': 'theMetricName',
            'value': 34
        },
        {
            'metric_name': 'theMetricName',
            'value': 17
        }
    ]

@pytest.fixture()
def metrics_to_put_expected():
    return [
        {
            'Value': 130,
            'MetricName': 'theMetricName'
        },
        {
            'Value': 45,
            'MetricName': 'theMetricName'
        },
        {
            'Value': 576,
            'MetricName': 'theMetricName'
        },
        {
            'Value': 241,
            'MetricName': 'theMetricName'
        },
        {
            'Value': 34,
            'MetricName': 'theMetricName'
        },
        {
            'Value': 17,
            'MetricName': 'theMetricName'
        }
    ]
