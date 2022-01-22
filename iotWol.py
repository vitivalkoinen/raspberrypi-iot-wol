from ast import Try
from wakeonlan import send_magic_packet
import paho.mqtt.client as mqtt
import json

from infrastructure.persistence.config_jsonfile import ConfigJsonFile
from infrastructure.persistence.config_jsonfile import CONFIG_FILE_NAME

def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))

def on_message(client, userdata, msg):
    macaddr = json.loads(msg.payload.decode('utf-8'))['data']
    send_magic_packet(macaddr)
    print('Send magic packet: ' + macaddr)

def main():
    config_file = ConfigJsonFile(CONFIG_FILE_NAME)
    config = config_file.load()

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set('token:%s' % config.token)
    client.tls_set(config.ca_certs)
    client.connect(config.mqtt_host, config.port)
    client.subscribe(config.topic)
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        return 0
if __name__ == "__main__":
    main()
