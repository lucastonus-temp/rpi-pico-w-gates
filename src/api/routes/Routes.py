from src.api.Request import Request
from src.api.Response import Response

class Routes():

	_routes = []

	def add(self, route: object):
		self._routes.append(route)

	def handle(self, request: Request, response: Response):
		for route in self._routes:
			method = request.get_method().lower() + request.get_path().replace('/', '_')

			try:
				named_attribute = getattr(route, method)

				if hasattr(route, method) and callable(named_attribute):
					named_attribute(request, response)
			except:
				pass