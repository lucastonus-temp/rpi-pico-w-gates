from socket import socket

class Response:

	_content_type = 'application/json'
	_status_code = 404
	_data = ''

	_status_code_description = {
		200: 'OK',
		204: 'No Content',
		401: 'Unauthorized',
		404: 'Not Found'
	}

	def set_content_type(self, content_type: str):
		self._content_type = content_type

	def set_status_code(self, status_code: int):
		self._status_code = status_code

	def get_status_code(self) -> int:
		return self._status_code

	def set_data(self, data: str):
		self._data = data

	def write(self, client: socket):
		client.send(f'HTTP/1.1 {self._status_code} {self._status_code_description[self._status_code]}\n')
		client.send(f'Content-Type: {self._content_type}\n\n')

		if len(self._data):
			client.send(self._data)

		client.close()