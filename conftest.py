import pytest
import requests
import allure
import logging
import curlify
import os
from dotenv import load_dotenv
from utils.sessions import api

from schemas.model_scheme import *


@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()
