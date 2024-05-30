from libs.Dotenv import Dotenv
from src.Gates import Gates
from src.WLAN import WLAN
from src.HttpServer import HttpServer
from src.GateButton import GateButton

env = Dotenv()

gates = Gates()

GateButton(gates, gates.INTERNAL, int(env.get('PIN_BUTTON_INTERNAL')))
GateButton(gates, gates.EXTERNAL, int(env.get('PIN_BUTTON_EXTERNAL')))

wlan = WLAN(env.get('WIFI_SSID'), env.get('WIFI_PASSWORD'))
wlan.connect()

http_server = HttpServer(env.get('HTTP_SERVER_ADDRESS'), int(env.get('HTTP_SERVER_PORT')))
http_server.run(gates)