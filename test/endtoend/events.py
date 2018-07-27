"""Collection of events for end-to-end tests."""
import pytest
import time
import uuid
import json
CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000
def dict_to_binary(the_dict):
    str = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)
    return binary
@pytest.fixture()
def standard_valid_input():
    current_time = int(time.time()*CONVERT_SECONDS_TO_MILLIS_FACTOR)
    new_uuid = str(uuid.uuid4())
    request_id = "request_id_" + new_uuid
    return {
        "request_id": request_id,
        "metric_data": [
            {
                "metric_name": "theMetricName",
                "dimensions": [
                    {
                        "name": "theName",
                        "value": "theValue"
                    }
                ],
                "timestamp": current_time,
                "value": 17,
                "unit": "Seconds",
                "storage_resolution": 12
            }
        ]
    }
    byte_event = dict_to_binary(dict_event)
    return byte_event
@pytest.fixture()
def sample_query():
    return [
        {
            "Id": "id",
            "MetricStat": {
                "Metric": {
                    #"Namespace": "josh_namespace",
                    #"Namespace": "MetricPublisherDefaultNamespace",
                    "Namespace": "demo_namespace",
                    "MetricName": "theMetricName",
                    "Dimensions": [
                        {
                            "Name": "theName",
                            "Value": "theValue",
                        }
                    ]
                },
                "Period": 5,
                "Stat": "Average",
                "Unit": "Seconds"
            }
        }
    ]
