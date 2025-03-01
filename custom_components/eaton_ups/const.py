"""Constants for eaton_ups."""

from logging import Logger, getLogger
from typing import Final

LOGGER: Logger = getLogger(__package__)

DOMAIN = "eaton_ups"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"

CONF_SERVER_CERT: Final = "server_cert"
CONF_CLIENT_KEY: Final = "client_key"
CONF_CLIENT_CERT: Final = "client_cert"

DEFAULT_PORT = 8883

MQTT_TIMEOUT = 5
MQTT_CONNECTION_ATTEMPTS = 10
