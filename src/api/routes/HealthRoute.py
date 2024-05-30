from src.api.Request import Request
from src.api.Response import Response
from src.api.controllers.HealthController import HealthController

class HealthRoute():

	def __init__(self):
		self._controller = HealthController()

	def get_health(self, request: Request, response: Response):
		self._controller.health(request, response)