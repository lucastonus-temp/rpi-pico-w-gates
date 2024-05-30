from src.Gates import Gates

class GateService:

	def __init__(self, gates: Gates):
		self._gates = gates

	def trigger_internal_gate(self) -> bool:
		return self._gates.trigger(self._gates.INTERNAL)

	def trigger_external_gate(self) -> bool:
		return self._gates.trigger(self._gates.EXTERNAL)