from src.Gates import Gates
from src.api.Request import Request
from src.api.Response import Response
from src.api.services.GateService import GateService

class GateController:

	def __init__(self, gates: Gates):
		self._service = GateService(gates)

	def trigger_internal(self, request: Request, response: Response):
		if self._service.trigger_internal_gate():
			response.set_status_code(204)
			return

		response.set_status_code(400)

	def trigger_external(self, request: Request, response: Response):
		if self._service.trigger_external_gate():
			response.set_status_code(204)
			return

		response.set_status_code(400)