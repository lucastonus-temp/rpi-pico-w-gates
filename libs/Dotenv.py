"""
Dotenv - Used to read and store values of a .env file
Designed to be used on Raspberry Pi Pico
"""

class Dotenv:

	_instance = None
	_data = {}

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super(Dotenv, cls).__new__(cls)
			cls._instance._load()

		return cls._instance

	def _load(self) -> None:
		try:
			with open('.env', 'r') as file:
				for line in file:
					if line.strip() and not line.startswith('#'):
						key, value = map(str.strip, line.split('=', 1))
						self._data[key] = value
		except Exception as e:
			print(f'[ERROR] Failed to read .env file: {e}')

	def get(self, key) -> str:
		if key in self._data:
			return self._data[key]
		else:
			print('[WARNING] .env key not set: ' + key)
			return ''