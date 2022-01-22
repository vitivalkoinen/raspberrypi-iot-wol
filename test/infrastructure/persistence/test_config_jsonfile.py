import unittest
from infrastructure.persistence.config_jsonfile import ConfigJsonFile
from infrastructure.persistence.config_jsonfile import CONFIG_FILE_NAME


class TestConfigJsonFile(unittest.TestCase):
    def test_load(self):
        file_path = 'test/infrastructure/persistence/testdata/' + CONFIG_FILE_NAME
        config_jsonfile = ConfigJsonFile(file_path)
        config = config_jsonfile.load()

        expected = {
            'MQTTHost': 'xxxx.com',
            'Port': 8883,
            'CACerts': 'dummy_certs.pem',
            'Token': 'token_xxxxxxaaaaa',
            'Topic': 'wol/raspberrypi'
        }

        self.assertEqual(expected['MQTTHost'], config.mqtt_host)
        self.assertEqual(expected['Port'], config.port)
        self.assertEqual(expected['CACerts'], config.ca_certs)
        self.assertEqual(expected['Token'], config.token)
        self.assertEqual(expected['Topic'], config.topic)

if __name__ == "__main__":
    unittest.main()