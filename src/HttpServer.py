import socket
import src.common as common
from src.Gates import Gates
from src.api.Request import Request
from src.api.Response import Response
from src.api.middlewares.AuthMiddleware import AuthMiddleware
from src.api.routes.Routes import Routes
from src.api.routes.GateRoute import GateRoute
from src.api.routes.HealthRoute import HealthRoute

class HttpServer:

	def __init__(self, address: str, port: int):
		self._address = address
		self._port = port

	def run(self, gates: Gates, backlog = 0):
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.bind((self._address, self._port))
		self._socket.listen(backlog)

		self._handle_requests(gates)

	def _ignore_auth(self, request: Request) -> bool:
		return request.get_method() == 'GET' and request.get_path() == '/health'

	def _handle_requests(self, gates: Gates):
		routes = Routes()
		routes.add(GateRoute(gates))
		routes.add(HealthRoute())

		authMiddleware = AuthMiddleware()

		while True:
			request = Request(self._socket.accept())
			response = Response()

			if self._ignore_auth(request) or authMiddleware(request, response):
				routes.handle(request, response)

			response.write(request.get_client())

			if common.debug():
				print(f'[{request.get_ip()[0]}] {request.get_method()} {request.get_path()} - {response.get_status_code()}')