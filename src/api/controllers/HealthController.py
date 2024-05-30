from src.api.Request import Request
from src.api.Response import Response

class HealthController:

	def health(self, request: Request, response: Response):
		response.set_content_type('text/plain')
		response.set_status_code(200)
		response.set_data('OK')