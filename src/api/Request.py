from socket import socket

class Request:

	def __init__(self, connection: tuple):
		self._client = connection[0]
		self._ip = connection[1]

		self._parse_data(self._client)

	def _parse_data(self, client):
		data = client.recv(1024)
		data = data.decode('utf-8')

		metadata, body = data.split('\r\n\r\n')
		self._parse_metadata(metadata)
		self._parse_body(body)

	def _parse_metadata(self, metadata: str):
		splitted_metadata = metadata.split('\r\n')

		method, path, protocol = splitted_metadata[0].split(' ')

		self._method = method
		self._path = path
		self._protocol = protocol

		self._parse_headers(splitted_metadata[1:])

	def _parse_headers(self, headers: list[str]):
		self._headers = {}

		for header in headers:
			key, value = header.split(': ')
			self._headers[key] = value

	def _parse_body(self, body: str):
		self._body = body

	def get_client(self) -> socket:
		return self._client

	def get_ip(self) -> str:
		return self._ip

	def get_protocol(self) -> str:
		return self._protocol

	def get_method(self) -> str:
		return self._method

	def get_path(self) -> str:
		return self._path

	def get_headers(self) -> dict[str, str]:
		return self._headers

	def get_body(self) -> str:
		return self._body