import pycom
pycom.heartbeat(False)
pycom.rgbled(0xff00)

from network import WLAN
import machine
wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == 'TESTES-NASH':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'nashifce8556'), timeout=5000)
        while not wlan.isconnected():
            machine.idle()
        print('WLAN connection succeeded!')
        break

wlan.init(mode=WLAN.STA)
wlan.ifconfig(config=('192.168.0.3', '255.255.255.0', '192.168.178.1', '8.8.8.8'))

print("ready!")

import config
from nanogateway import NanoGateway

if __name__ == '__main__':
    nanogw = NanoGateway(
        id=config.GATEWAY_ID,
        frequency=config.LORA_FREQUENCY,
        datarate=config.LORA_GW_DR,
        ssid=config.WIFI_SSID,
        password=config.WIFI_PASS,
        server=config.SERVER,
        port=config.PORT,
        ntp_server=config.NTP,
        ntp_period=config.NTP_PERIOD_S
        )

    nanogw.start()
    nanogw._log('You may now press ENTER to enter the REPL')
    input()
