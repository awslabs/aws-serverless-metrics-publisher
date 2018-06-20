"""Configuration values used by lambda functions."""

import os
import time

CONVERT_SECONDS_TO_MILLIS_FACTOR = 1000

# DDB Table
CHECKPOINT_TABLE_NAME = os.getenv('CHECKPOINT_TABLE_NAME')

# Metrics Log Group
LOG_GROUP_NAME = os.getenv('LOG_GROUP_NAME')
LOG_GROUP_NAME_TEMP = "metricPublisherAppLogGroup"

# Events Rule
EVENTS_RULE_NAME = os.getenv('EVENTS_RULE_NAME')

# Namespace
NAMESPACE_PARAM = os.getenv('NAMESPACE_PARAM')
NAMESPACE_PARAM_TEMP = "temp_namespace"

CURRENT_TIME = int(time.time()*CONVERT_SECONDS_TO_MILLIS_FACTOR)
