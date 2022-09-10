from test_reqres_api.conftest import *
from requests import Session


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    @allure.step('{method}')
    def request(self, method, url, **kwargs):
        with allure.step(f'Attachments:'):
            response = super().request(method, url=f'{self.base_url}{url}', **kwargs)
            message = curlify.to_curl(response.request)
            logging.info(f'cURL: {message}\n')
            logging.info(f'Response: {response.json()}\n')
            allure.attach(
                body=message.encode('utf8'),
                name=f'Request',
                attachment_type=allure.attachment_type.TEXT,
                extension='txt'
            )
            allure.attach(
                body=str(response.json()).encode('utf-8'),
                name='Response',
                attachment_type=allure.attachment_type.TEXT,
                extension='txt'
            )

        return response
