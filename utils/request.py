from dataclasses import dataclass
from utils.logger import Logger
import requests

logger = Logger()

@dataclass
class Response:
    status_code: int
    text: str
    json: object
    headers: dict

class Request:

    def get(self, url):
        response = requests.get(url)
        return self.__get_responses(response)

    def __get_responses(self, response):
        request = response.request
        status_code = response.status_code
        text = str(response.json())

        try:
            json = response.json()
        except Exception:
            json = {}

        headers = response.headers
        logger.logger(request, response)
        return Response(status_code, text, json, headers)