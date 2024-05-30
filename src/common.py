from libs.Dotenv import Dotenv

env = Dotenv()

def debug() -> bool:
	return bool(int(env.get('DEBUG')))