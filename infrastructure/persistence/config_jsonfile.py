import json

from domain.repository.config import ConfigRepository
from domain.config import Config

CONFIG_FILE_NAME = 'config.json'
CONFIG_KEY_MQTT_HOST = 'MQTTHost'
CONFIG_KEY_PORT = 'Port'
CONFIG_KEY_CA_CERTS = 'CACerts'
CONFIG_KEY_TOKEN = 'Token'
CONFIG_KEY_TOPIC = 'Topic'


class ConfigJsonFile(ConfigRepository):
    def __init__(self, file_path):
        self._file_path = file_path

    def load(self):
        with open(self._file_path, mode='r', encoding='utf-8') as file:
            load_data = json.load(file)
            config = Config(
                mqtt_host=load_data.get(CONFIG_KEY_MQTT_HOST),
                port=load_data.get(CONFIG_KEY_PORT),
                ca_certs=load_data.get(CONFIG_KEY_CA_CERTS),
                token=load_data.get(CONFIG_KEY_TOKEN),
                topic=load_data.get(CONFIG_KEY_TOPIC)
            )
        return config
