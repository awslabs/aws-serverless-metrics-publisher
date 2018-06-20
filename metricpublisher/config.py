"""Configuration values used by lambda functions."""

import os

# DDB Table
LOG_INFO_TABLE_NAME = os.getenv('LOG_INFO_TABLE_NAME')

# Metrics Log Group
LOG_GROUP_NAME = os.getenv('LOG_GROUP_NAME')
LOG_GROUP_NAME_TEMP = "metricPublisherAppLogGroup"
NAMESPACE_TEMP_PARAM = "parameter_namespace"

# Events Rule
EVENTS_RULE_NAME = os.getenv('EVENTS_RULE_NAME')
