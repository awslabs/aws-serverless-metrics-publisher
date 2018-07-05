"""Collection of events for unit tests."""
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
def empty_request_id():
    return {
        "request_id": "",
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
def empty_dimension_name():
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
                        "name": "",
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
def empty_metric_name():
    return {
        "request_id": "an id",
        "metric_data": [
            {
                "metric_name": "",
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
def sample_log_events():
        return {
        u'searchedLogStreams': [
            {
                u'searchedCompletely': True,
                u'logStreamName': u'metricPublisherAppNamespace_request_id_1beda470-2c17-44c9-b2bd-cefed4fe40d8'
            },
            {
                u'searchedCompletely': True,
                u'logStreamName': u'metricPublisherAppNamespace_request_id_3618d626-b668-4976-abca-6bb544a6b478'
            },
            {
                u'searchedCompletely': True,
                u'logStreamName': u'metricPublisherAppNamespace_request_id_402ef2a1-eaf3-418f-ac9c-3a4ec4fffa39'
            },
            {
                u'searchedCompletely': True,
                u'logStreamName': u'metricPublisherAppNamespace_request_id_4232fdf3-e66b-4cd4-9db1-96e9be48a4ee'
            },
            {
                u'searchedCompletely': True,
                u'logStreamName': u'metricPublisherAppNamespace_request_id_61cb9208-b388-466c-87fd-79a5ea89c922'
            },
            {
                u'searchedCompletely': True,
                u'logStreamName': u'metricPublisherAppNamespace_request_id_d7b593f0-b154-49b4-91f0-864c13740640'
            }
        ],
        u'events': [
            {
                u'ingestionTime': 1530295428233,
                u'timestamp': 1530295428222,
                u'message': u"{'metric_data': [{'metric_name': 'theMetricName2', 'value': 17}], 'request_id': 'request_id_61cb9208-b388-466c-87fd-79a5ea89c922'}",
                u'eventId': u'34126728423255130347406918563580169267920727811577872384',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_61cb9208-b388-466c-87fd-79a5ea89c922'
            },
            {
                u'ingestionTime': 1530295428421,
                u'timestamp': 1530295428416,
                u'message': u"{'metric_data': [{'metric_name': 'theMetricName2', 'value': 18}], 'request_id': 'request_id_3618d626-b668-4976-abca-6bb544a6b478'}",
                u'eventId': u'34126728427581474915921859453265385545568477186932670464',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_3618d626-b668-4976-abca-6bb544a6b478'
            },
            {
                u'ingestionTime': 1530295428601,
                u'timestamp': 1530295428595,
                u'message': u"{'metric_data': [{'metric_name': 'theMetricName2', 'value': 19}], 'request_id': 'request_id_4232fdf3-e66b-4cd4-9db1-96e9be48a4ee'}",
                u'eventId': u'34126728431573308306458840995817882099436477345871167488',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_4232fdf3-e66b-4cd4-9db1-96e9be48a4ee'
            },
            {
                u'ingestionTime': 1530295428776,
                u'timestamp': 1530295428767,
                u'message': u"{'metric_data': [{'metric_name': 'theMetricName2', 'value': 20}], 'request_id': 'request_id_d7b593f0-b154-49b4-91f0-864c13740640'}",
                u'eventId': u'34126728435409036480606108176373631531088849482571448320',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_d7b593f0-b154-49b4-91f0-864c13740640'
            },
            {
                u'ingestionTime': 1530295428950,
                u'timestamp': 1530295428945,
                u'message': u"{'metric_data': [{'metric_name': 'theMetricName2', 'value': 21}], 'request_id': 'request_id_402ef2a1-eaf3-418f-ac9c-3a4ec4fffa39'}",
                u'eventId': u'34126728439378569125944559095777385025694673565001449472',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_402ef2a1-eaf3-418f-ac9c-3a4ec4fffa39'
            },
            {
                u'ingestionTime': 1530295429134,
                u'timestamp': 1530295429127,
                u'message': u"{'metric_data': [{'metric_name': 'theMetricName2', 'value': 22}], 'request_id': 'request_id_1beda470-2c17-44c9-b2bd-cefed4fe40d8'}",
                u'eventId': u'34126728443437304752077132507759222312180838774063235072',
                u'logStreamName': u'metricPublisherAppNamespace_request_id_1beda470-2c17-44c9-b2bd-cefed4fe40d8'
            }
        ],
        'ResponseMetadata': {
            'RetryAttempts': 0,
            'HTTPStatusCode': 200,
            'RequestId': '7d38f350-7bc8-11e8-98e7-e75833189162',
            'HTTPHeaders': {
                'x-amzn-requestid': '7d38f350-7bc8-11e8-98e7-e75833189162',
                'date': 'Fri',
                'content-length': '3305',
                'content-type': 'application/x-amz-json-1.1'
            }
        }
    }

@pytest.fixture()
def standard_item():
    return {
        u'Item': {
            u'cursor': {
                u'S': u'cursor_for_next_batch'
            },
            u'cursor_timestamp': {
                u'N': u'1530295428700'
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
            'metric_name': 'theMetricName2',
            'value': 17
        },
        {
            'metric_name': 'theMetricName2',
            'value': 18
        },
        {
            'metric_name': 'theMetricName2',
            'value': 19
        },
        {
            'metric_name': 'theMetricName2',
            'value': 20
        },
        {
            'metric_name': 'theMetricName2',
            'value': 21
        },
        {
            'metric_name': 'theMetricName2',
            'value': 22
        }
    ]

@pytest.fixture()
def metrics_to_put_expected():
    return [
        {
            'Value': 17,
            'MetricName': 'theMetricName2'
        },
        {
            'Value': 18,
            'MetricName': 'theMetricName2'
        },
        {
            'Value': 19,
            'MetricName': 'theMetricName2'
        },
        {
            'Value': 20,
            'MetricName': 'theMetricName2'
        },
        {
            'Value': 21,
            'MetricName': 'theMetricName2'
        },
        {
            'Value': 22,
            'MetricName': 'theMetricName2'
        }
    ]
