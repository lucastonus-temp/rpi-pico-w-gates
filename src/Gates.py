import time
import src.common as common
from machine import Pin
from libs.Dotenv import Dotenv

env = Dotenv()

class Gates():

	INTERNAL = 1
	EXTERNAL = 2

	def __init__(self):
		self._init_led()
		self._init_relays()

	def _init_led(self):
		self._led = Pin(int(env.get('PIN_LED')), Pin.OUT)
		self._led.off()

	def _init_relays(self):
		relay_internal = Pin(int(env.get('PIN_RELE_INTERNAL')), Pin.OUT)
		relay_internal.on()

		relay_external = Pin(int(env.get('PIN_RELE_EXTERNAL')), Pin.OUT)
		relay_external.on()

		self._relays = {
			self.INTERNAL: relay_internal,
			self.EXTERNAL: relay_external
		}

	def trigger(self, gate: int) -> bool:
		if not gate in self._relays:
			return False

		relay = self._relays[gate]

		self._led.on()
		relay.off()
		time.sleep(0.5)
		relay.on()
		self._led.off()

		if common.debug():
			print(f'{"Internal" if gate == self.INTERNAL else "External"} gate triggered')

		return True