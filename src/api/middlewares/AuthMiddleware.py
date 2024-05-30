from libs.Dotenv import Dotenv
from src.api.Request import Request
from src.api.Response import Response

env = Dotenv()

class AuthMiddleware():

	_header_key = 'x-api-key'

	def __call__(self, request: Request, response: Response) -> bool:
		headers = request.get_headers()

		if self._header_key in headers and headers[self._header_key] == env.get('API_SECRET'):
			return True

		response.set_status_code(401)

		return False