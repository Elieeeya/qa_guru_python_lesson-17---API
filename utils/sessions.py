import os
from dotenv import load_dotenv

from utils.requests_helper import BaseSession


def api() -> BaseSession:
    api_url = os.getenv('api')
    return BaseSession(base_url=api_url)




