"""Collection of events for schema validation"""
import pytest

@pytest.fixture()
def standard_valid_input():
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
    return {
        "request_id":"an id",
        "metric_data": [
            {
                "metric_name": "theMetricname",
                "value":123,
            }
        ]
    }

@pytest.fixture()
def multiple_metrics_input():
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
