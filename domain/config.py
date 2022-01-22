
class Config:
    def __init__(self, mqtt_host, ca_certs, token, topic, port=8883):
        self._mqtt_host = mqtt_host
        self._port = port
        self._ca_certs = ca_certs
        self._token = token
        self._topic = topic

    @property
    def mqtt_host(self):
        return self._mqtt_host

    @property
    def port(self):
        return self._port

    @property
    def ca_certs(self):
        return self._ca_certs

    @property
    def token(self):
        return self._token

    @property
    def topic(self):
        return self._topic