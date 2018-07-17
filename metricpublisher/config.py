"""Configuration values used by lambda functions."""

import os
import sys
sys.path.append('lib')

# JSONSCHEMA Name
LOG_EVENT_SCHEMA_NAME = 'log_event.json'

# DDB Table
CHECKPOINT_TABLE_NAME = os.getenv('CHECKPOINT_TABLE_NAME')

# Metrics Log Group
LOG_GROUP_NAME = os.getenv('LOG_GROUP_NAME')

# Events Rule
EVENTS_RULE_NAME = os.getenv('EVENTS_RULE_NAME')

# Namespace
NAMESPACE_PARAM = os.getenv('NAMESPACE_PARAM')
