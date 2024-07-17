from environs import Env

env = Env()
env.read_env()

token: str = env.str('TOKEN')
admin_id: int = env.int('ADMIN_ID')
