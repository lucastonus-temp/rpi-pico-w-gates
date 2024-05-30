from src.Gates import Gates
from src.api.Request import Request
from src.api.Response import Response
from src.api.controllers.GateController import GateController

class GateRoute():

	def __init__(self, gates: Gates):
		self._controller = GateController(gates)

	def post_gates_internal(self, request: Request, response: Response):
		self._controller.trigger_internal(request, response)

	def post_gates_external(self, request: Request, response: Response):
		self._controller.trigger_external(request, response)