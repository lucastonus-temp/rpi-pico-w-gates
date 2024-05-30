import time
import src.common as common
from machine import Pin
from src.Gates import Gates

class GateButton:

	def __init__(self, gates: Gates, gate: int, pin: int):
		self._gates = gates
		self._gate = gate

		self.button = Pin(pin, Pin.IN, Pin.PULL_DOWN)
		self.button.irq(trigger=Pin.IRQ_RISING, handler=self.handle)

	def handle(self, pin):
		if pin.value():
			if common.debug():
				print(f'{"Internal" if self._gate == self._gates.INTERNAL else "External"} gate button pressed')

			self._gates.trigger(self._gate)
			time.sleep(1)