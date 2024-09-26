from environs import Env

class Config:
    def __init__(self):
        self.env = Env()
        self.env.read_env()

        self.token: str = self.env.str("TOKEN")
        self.admin_id: int = self.env.int("ADMIN_ID")

config = Config()
