import network
import time
import src.common as common

class WLAN:

	def __init__(self, ssid: str, password: str):
		self._ssid = ssid
		self._password = password

		self._wlan = network.WLAN(network.STA_IF)
		self._wlan.active(True)

	def connect(self):
		if common.debug():
			print(f'Connecting to {self._ssid}', end='')

		self._wlan.connect(self._ssid, self._password)

		while not self._wlan.isconnected():
			if common.debug():
				print('.', end='')
				time.sleep(1)
			pass

		if common.debug():
			print('Connected')