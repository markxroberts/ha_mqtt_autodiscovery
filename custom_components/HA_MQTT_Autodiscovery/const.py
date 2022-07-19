"""Constants for integration_blueprint."""
# Base component constants
NAME = "HA MQTT Autodiscovery"
DOMAIN = "HA_MQTT_autodiscovery"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
ATTRIBUTION = ""
ISSUE_URL = "https://github.com/markxroberts/ha_mqtt_autodiscovery/issues"

# Icons
ICON = "mdi:water-percent"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
BUTTON = "button"
PLATFORMS = [BINARY_SENSOR, SENSOR, BUTTON]


# Configuration and options
CONF_ENABLED = "enabled"
DATA_FILE = "data_file"
HA_AUTODISCOVERY_PREFIX = "ha_prefix"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""