
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
def simple_metric_log_event_format():
    return {
        "metric_name": "theMetricName",
        "value": 123,
    }

@pytest.fixture()
def simple_metric_put_data_format():
    return {
        "MetricName":"theMetricName",
        "Value": 123,
    }

@pytest.fixture()
def complex_metric_log_event_format():
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
def complex_metric_put_data_format():
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
def sample_batch():
    return [
        {
            'MetricName': 'theMetricName',
            'Value': 17
        },
        {
            'MetricName': 'theMetricName',
            'Value': 18
        },
        {
            'MetricName': 'theMetricName',
            'Value': 19
        },
        {
            'MetricName': 'theMetricName',
            'Value': 20
        },
        {
            'MetricName': 'theMetricName',
            'Value': 21
        },
        {
            'MetricName': 'theMetricName',
            'Value': 22
        }
    ]

@pytest.fixture()
def unformated_metrics_expected():
    return [
        {
            'metric_name': 'theMetricName',
            'value': 17
        },
        {
            'metric_name': 'theMetricName',
            'value': 18
        },
        {
            'metric_name': 'theMetricName',
            'value': 19
        },
        {
            'metric_name': 'theMetricName',
            'value': 20
        },
        {
            'metric_name': 'theMetricName',
            'value': 21
        },
        {
            'metric_name': 'theMetricName',
            'value': 22
        }
    ]

@pytest.fixture()
def log_events_normal():
    return [
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
    ]

@pytest.fixture()
def batched_metrics_normal():
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
def many_log_events():
    return [
        {
            u'ingestionTime': 1530897511706,
            u'timestamp': 1530897511755,
            u'message': u"{'metric_data': [{'timestamp': 1530897511448, 'metric_name': 'theMetricName', 'value': 17}], 'request_id': 'request_id_bbf2b361-4cf8-4d13-87de-568bad11b521'}",
            u'eventId': u'34140155334712794451397393822139436354307158608090300416',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_bbf2b361-4cf8-4d13-87de-568bad11b521'
        },
        {
            u'ingestionTime': 1530897511904,
            u'timestamp': 1530897511957,
            u'message': u"{'metric_data': [{'timestamp': 1530897511866, 'metric_name': 'theMetricName', 'value': 18}], 'request_id': 'request_id_a8892402-2850-4f0c-b996-e2f961bde951'}",
            u'eventId': u'34140155339217544981500579696969049208210848175282388992',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_a8892402-2850-4f0c-b996-e2f961bde951'
        },
        {
            u'ingestionTime': 1530897512088,
            u'timestamp': 1530897512142,
            u'message': u"{'metric_data': [{'timestamp': 1530897512045, 'metric_name': 'theMetricName', 'value': 19}], 'request_id': 'request_id_4f4cb112-f862-40bc-bbd2-ce3f08950aa2'}",
            u'eventId': u'34140155343343182843228744978375816959492556136213512192',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_4f4cb112-f862-40bc-bbd2-ce3f08950aa2'
        },
        {
            u'ingestionTime': 1530897512257,
            u'timestamp': 1530897512311,
            u'message': u"{'metric_data': [{'timestamp': 1530897512224, 'metric_name': 'theMetricName', 'value': 20}], 'request_id': 'request_id_3161d1b2-1656-49cc-adc2-d66ad677be84'}",
            u'eventId': u'34140155347112008781780420289499265245750404335519203328',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_3161d1b2-1656-49cc-adc2-d66ad677be84'
        },
        {
            u'ingestionTime': 1530897512433,
            u'timestamp': 1530897512487,
            u'message': u"{'metric_data': [{'timestamp': 1530897512396, 'metric_name': 'theMetricName', 'value': 21}], 'request_id': 'request_id_a2414cd1-989c-43d4-b740-276d143e1134'}",
            u'eventId': u'34140155351036939936721809962622521924228387618665332736',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_a2414cd1-989c-43d4-b740-276d143e1134'
        },
        {
            u'ingestionTime': 1530897512617,
            u'timestamp': 1530897512670,
            u'message': u"{'metric_data': [{'timestamp': 1530897512576, 'metric_name': 'theMetricName', 'value': 22}], 'request_id': 'request_id_d2ea0faa-ddba-4acf-b44f-ad550b308f61'}",
            u'eventId': u'34140155355117976308052913997746049710635287394391556096',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_d2ea0faa-ddba-4acf-b44f-ad550b308f61'
        },
        {
            u'ingestionTime': 1530897512800,
            u'timestamp': 1530897512853,
            u'message': u"{'metric_data': [{'timestamp': 1530897512759, 'metric_name': 'theMetricName', 'value': 23}], 'request_id': 'request_id_1eebb564-2adc-4761-b5b8-c525f97f6605'}",
            u'eventId': u'34140155359199012679384018032868374480409545087618056192',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_1eebb564-2adc-4761-b5b8-c525f97f6605'
        },
        {
            u'ingestionTime': 1530897512989,
            u'timestamp': 1530897513043,
            u'message': u"{'metric_data': [{'timestamp': 1530897512945, 'metric_name': 'theMetricName', 'value': 24}], 'request_id': 'request_id_58211db8-3905-4a7f-948f-de1a6eb82525'}",
            u'eventId': u'34140155363436154267104836429988455163783523306798317568',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_58211db8-3905-4a7f-948f-de1a6eb82525'
        },
        {
            u'ingestionTime': 1530897513235,
            u'timestamp': 1530897513223,
            u'message': u"{'metric_data': [{'timestamp': 1530897513135, 'metric_name': 'theMetricName', 'value': 25}], 'request_id': 'request_id_9a2d80fb-b9fa-45f6-bffb-b8164805d28b'}",
            u'eventId': u'34140155367450288402840348595762125836865631491286695936',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_9a2d80fb-b9fa-45f6-bffb-b8164805d28b'
        },
        {
            u'ingestionTime': 1530897513429,
            u'timestamp': 1530897513481,
            u'message': u"{'metric_data': [{'timestamp': 1530897513390, 'metric_name': 'theMetricName', 'value': 26}], 'request_id': 'request_id_203cfc60-da33-4126-a7c5-c4ead39ebb0f'}",
            u'eventId': u'34140155373203880664061249366513296413228639787555749888',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_203cfc60-da33-4126-a7c5-c4ead39ebb0f'
        },
        {
            u'ingestionTime': 1530897513620,
            u'timestamp': 1530897513672,
            u'message': u"{'metric_data': [{'timestamp': 1530897513578, 'metric_name': 'theMetricName', 'value': 27}], 'request_id': 'request_id_92957208-0862-4017-8cd4-0ba6693fa9ae'}",
            u'eventId': u'34140155377463322996980598386777568039913421197688176640',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_92957208-0862-4017-8cd4-0ba6693fa9ae'
        },
        {
            u'ingestionTime': 1530897513799,
            u'timestamp': 1530897513851,
            u'message': u"{'metric_data': [{'timestamp': 1530897513760, 'metric_name': 'theMetricName', 'value': 28}], 'request_id': 'request_id_0bbf4dd5-7f17-4e88-9a39-422ee113ba21'}",
            u'eventId': u'34140155381455156387517579929328644727692714340910759936',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_0bbf4dd5-7f17-4e88-9a39-422ee113ba21'
        },
        {
            u'ingestionTime': 1530897513997,
            u'timestamp': 1530897514050,
            u'message': u"{'metric_data': [{'timestamp': 1530897513947, 'metric_name': 'theMetricName', 'value': 29}], 'request_id': 'request_id_8214c2e0-a28c-4b96-ad1d-14c80d41db38'}",
            u'eventId': u'34140155385893004682025173934733563848374142894722973696',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_8214c2e0-a28c-4b96-ad1d-14c80d41db38'
        },
        {
            u'ingestionTime': 1530897514176,
            u'timestamp': 1530897514228,
            u'message': u"{'metric_data': [{'timestamp': 1530897514140, 'metric_name': 'theMetricName', 'value': 30}], 'request_id': 'request_id_27ef607d-3950-44dc-9d0c-fe3cbb9baaf1'}",
            u'eventId': u'34140155389862537327363624854143331402385233102406680576',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_27ef607d-3950-44dc-9d0c-fe3cbb9baaf1'
        },
        {
            u'ingestionTime': 1530897514353,
            u'timestamp': 1530897514407,
            u'message': u"{'metric_data': [{'timestamp': 1530897514318, 'metric_name': 'theMetricName', 'value': 31}], 'request_id': 'request_id_60fb2df5-d87d-457d-9725-fcd3e48160c0'}",
            u'eventId': u'34140155393854370717900606396692373195828665652018675712',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_60fb2df5-d87d-457d-9725-fcd3e48160c0'
        },
        {
            u'ingestionTime': 1530897514570,
            u'timestamp': 1530897514624,
            u'message': u"{'metric_data': [{'timestamp': 1530897514532, 'metric_name': 'theMetricName', 'value': 32}], 'request_id': 'request_id_c3fb2d85-0af7-4076-8514-73d6dbdcba0c'}",
            u'eventId': u'34140155398693632425981751618667946965595437029575294976',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_c3fb2d85-0af7-4076-8514-73d6dbdcba0c'
        },
        {
            u'ingestionTime': 1530897514762,
            u'timestamp': 1530897514815,
            u'message': u"{'metric_data': [{'timestamp': 1530897514724, 'metric_name': 'theMetricName', 'value': 33}], 'request_id': 'request_id_24e658e4-2556-488e-9a25-82a1597db199'}",
            u'eventId': u'34140155402953074758901100638933022130082178699158487040',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_24e658e4-2556-488e-9a25-82a1597db199'
        },
        {
            u'ingestionTime': 1530897514951,
            u'timestamp': 1530897515003,
            u'message': u"{'metric_data': [{'timestamp': 1530897514907, 'metric_name': 'theMetricName', 'value': 34}], 'request_id': 'request_id_cfc9b0ee-881f-4d41-a6fe-f63e4e8e05f3'}",
            u'eventId': u'34140155407145614856224857789770439150351240429199425536',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_cfc9b0ee-881f-4d41-a6fe-f63e4e8e05f3'
        },
        {
            u'ingestionTime': 1530897515133,
            u'timestamp': 1530897515186,
            u'message': u"{'metric_data': [{'timestamp': 1530897515096, 'metric_name': 'theMetricName', 'value': 35}], 'request_id': 'request_id_2a9bbfeb-e1c9-49cb-9d87-895b198ace4a'}",
            u'eventId': u'34140155411226651227555961824891369295850487120759226368',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_2a9bbfeb-e1c9-49cb-9d87-895b198ace4a'
        },
        {
            u'ingestionTime': 1530897515344,
            u'timestamp': 1530897515366,
            u'message': u"{'metric_data': [{'timestamp': 1530897515275, 'metric_name': 'theMetricName', 'value': 36}], 'request_id': 'request_id_cb722e60-3534-49cb-a0ac-3537e5b50de4'}",
            u'eventId': u'34140155415240785363291473990622845109862547938389721088',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_cb722e60-3534-49cb-a0ac-3537e5b50de4'
        },
        {
            u'ingestionTime': 1530897515530,
            u'timestamp': 1530897515583,
            u'message': u"{'metric_data': [{'timestamp': 1530897515489, 'metric_name': 'theMetricName', 'value': 37}], 'request_id': 'request_id_66c82a99-c60f-49b1-88b3-2d19c0d019cd'}",
            u'eventId': u'34140155420080047071372619212561315534339973570889187328',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_66c82a99-c60f-49b1-88b3-2d19c0d019cd'
        },
        {
            u'ingestionTime': 1530897515712,
            u'timestamp': 1530897515765,
            u'message': u"{'metric_data': [{'timestamp': 1530897515674, 'metric_name': 'theMetricName', 'value': 38}], 'request_id': 'request_id_47ab6fe3-0cf5-4484-aebe-6b8ed378031e'}",
            u'eventId': u'34140155424138782697505192624540686407279398844138586112',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_47ab6fe3-0cf5-4484-aebe-6b8ed378031e'
        },
        {
            u'ingestionTime': 1530897515893,
            u'timestamp': 1530897515946,
            u'message': u"{'metric_data': [{'timestamp': 1530897515852, 'metric_name': 'theMetricName', 'value': 39}], 'request_id': 'request_id_080502dc-4083-4239-a5a6-3e0738d6fb9b'}",
            u'eventId': u'34140155428175217578439235413377806901430549560591253504',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_080502dc-4083-4239-a5a6-3e0738d6fb9b'
        },
        {
            u'ingestionTime': 1530897516071,
            u'timestamp': 1530897516125,
            u'message': u"{'metric_data': [{'timestamp': 1530897516032, 'metric_name': 'theMetricName', 'value': 40}], 'request_id': 'request_id_1853350a-3b29-4ccd-a590-414b3017e989'}",
            u'eventId': u'34140155432167050968976216955927842186209312428805259264',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_1853350a-3b29-4ccd-a590-414b3017e989'
        },
        {
            u'ingestionTime': 1530897516248,
            u'timestamp': 1530897516301,
            u'message': u"{'metric_data': [{'timestamp': 1530897516211, 'metric_name': 'theMetricName', 'value': 41}], 'request_id': 'request_id_ae1a3f67-d086-442c-8597-6209305a3f70'}",
            u'eventId': u'34140155436091982123917606629051900954924366077243817984',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_ae1a3f67-d086-442c-8597-6209305a3f70'
        },
        {
            u'ingestionTime': 1530897516433,
            u'timestamp': 1530897516485,
            u'message': u"{'metric_data': [{'timestamp': 1530897516393, 'metric_name': 'theMetricName', 'value': 42}], 'request_id': 'request_id_e51ba315-3bc0-4653-9fab-9cff22fa36f1'}",
            u'eventId': u'34140155440195319240447241287318153741572525219388915712',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_e51ba315-3bc0-4653-9fab-9cff22fa36f1'
        },
        {
            u'ingestionTime': 1530897516611,
            u'timestamp': 1530897516665,
            u'message': u"{'metric_data': [{'timestamp': 1530897516574, 'metric_name': 'theMetricName', 'value': 43}], 'request_id': 'request_id_98572219-257b-423e-be21-7ac045d443d6'}",
            u'eventId': u'34140155444209453376182753453009574801489562262114861056',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_98572219-257b-423e-be21-7ac045d443d6'
        },
        {
            u'ingestionTime': 1530897516788,
            u'timestamp': 1530897516840,
            u'message': u"{'metric_data': [{'timestamp': 1530897516750, 'metric_name': 'theMetricName', 'value': 44}], 'request_id': 'request_id_4fd4dc17-6860-4a2a-9f29-92adf6740705'}",
            u'eventId': u'34140155448112083785925612502992643509185034050503835648',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_4fd4dc17-6860-4a2a-9f29-92adf6740705'
        },
        {
            u'ingestionTime': 1530897516975,
            u'timestamp': 1530897517025,
            u'message': u"{'metric_data': [{'timestamp': 1530897516935, 'metric_name': 'theMetricName', 'value': 45}], 'request_id': 'request_id_66343cf1-a4a1-44e4-8675-ca78cc057104'}",
            u'eventId': u'34140155452237721647653777784402671101351646704514957312',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_66343cf1-a4a1-44e4-8675-ca78cc057104'
        },
        {
            u'ingestionTime': 1530897517208,
            u'timestamp': 1530897517262,
            u'message': u"{'metric_data': [{'timestamp': 1530897517163, 'metric_name': 'theMetricName', 'value': 46}], 'request_id': 'request_id_98ce4df1-29d8-4950-b813-21f3060f36a8'}",
            u'eventId': u'34140155457522998259705535469228209373138091971047063552',
            u'logStreamName': u'metricPublisherAppNamespace_request_id_98ce4df1-29d8-4950-b813-21f3060f36a8'
        }
    ]

@pytest.fixture()
def batch_metrics_many_events():
    return [
        {
            'timestamp': 1530897511448,
            'metric_name': 'theMetricName',
            'value': 17
        },
        {
            'timestamp': 1530897511866,
            'metric_name': 'theMetricName',
            'value': 18
        },
        {
            'timestamp': 1530897512045,
            'metric_name': 'theMetricName',
            'value': 19
        },
        {
            'timestamp': 1530897512224,
            'metric_name': 'theMetricName',
            'value': 20
        },
        {
            'timestamp': 1530897512396,
            'metric_name': 'theMetricName',
            'value': 21
        },
        {
            'timestamp': 1530897512576,
            'metric_name': 'theMetricName',
            'value': 22
        },
        {
            'timestamp': 1530897512759,
            'metric_name': 'theMetricName',
            'value': 23
        },
        {
            'timestamp': 1530897512945,
            'metric_name': 'theMetricName',
            'value': 24
        },
        {
            'timestamp': 1530897513135,
            'metric_name': 'theMetricName',
            'value': 25
        },
        {
            'timestamp': 1530897513390,
            'metric_name': 'theMetricName',
            'value': 26
        },
        {
            'timestamp': 1530897513578,
            'metric_name': 'theMetricName',
            'value': 27
        },
        {
            'timestamp': 1530897513760,
            'metric_name': 'theMetricName',
            'value': 28
        },
        {
            'timestamp': 1530897513947,
            'metric_name': 'theMetricName',
            'value': 29
        },
        {
            'timestamp': 1530897514140,
            'metric_name': 'theMetricName',
            'value': 30
        },
        {
            'timestamp': 1530897514318,
            'metric_name': 'theMetricName',
            'value': 31
        },
        {
            'timestamp': 1530897514532,
            'metric_name': 'theMetricName',
            'value': 32
        },
        {
            'timestamp': 1530897514724,
            'metric_name': 'theMetricName',
            'value': 33
        },
        {
            'timestamp': 1530897514907,
            'metric_name': 'theMetricName',
            'value': 34
        },
        {
            'timestamp': 1530897515096,
            'metric_name': 'theMetricName',
            'value': 35
        },
        {
            'timestamp': 1530897515275,
            'metric_name': 'theMetricName',
            'value': 36
        },
        {
            'timestamp': 1530897515489,
            'metric_name': 'theMetricName',
            'value': 37
        },
        {
            'timestamp': 1530897515674,
            'metric_name': 'theMetricName',
            'value': 38
        },
        {
            'timestamp': 1530897515852,
            'metric_name': 'theMetricName',
            'value': 39
        },
        {
            'timestamp': 1530897516032,
            'metric_name': 'theMetricName',
            'value': 40
        },
        {
            'timestamp': 1530897516211,
            'metric_name': 'theMetricName',
            'value': 41
        },
        {
            'timestamp': 1530897516393,
            'metric_name': 'theMetricName',
            'value': 42
        },
        {
            'timestamp': 1530897516574,
            'metric_name': 'theMetricName',
            'value': 43
        },
        {
            'timestamp': 1530897516750,
            'metric_name': 'theMetricName',
            'value': 44
        },
        {
            'timestamp': 1530897516935,
            'metric_name': 'theMetricName',
            'value': 45
        },
        {
            'timestamp': 1530897517163,
            'metric_name': 'theMetricName',
            'value': 46
        }
    ]

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
