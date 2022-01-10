import base64
import json
import logging
import requests
from urllib.parse import urlencode
from copy import deepcopy

from django.conf import settings

logger = logging.getLogger(__name__)


class RasPiApiClient:
    def __init__(
        self, prefix_url: str, auth_user_username: str, auth_user_password: str
    ):
        self.prefix_url = prefix_url
        self.auth_user_username = auth_user_username
        self.auth_user_password = auth_user_password

    def _create_url(self, endpoint: str, query: dict = None) -> str:
        if query:
            params = urlencode(query)
            return self.prefix_url + endpoint + "?" + params
        return self.prefix_url + endpoint

    def _create_headers(self, access_token: str = None, extra: dict = None) -> dict:
        headers = {}
        if access_token:
            headers.update({"Authorization": "JWT {}".format(access_token)})
        if extra:
            headers.update(extra)
        return headers

    def login(self) -> requests.Response:
        url = self._create_url("auth")
        headers = self._create_headers(
            extra={
                "Content-Type": "application/json",
            }
        )
        query = {
            "username": self.auth_user_username,
            "password": self.auth_user_password,
        }
        response = requests.post(url=url, headers=headers, data=json.dumps(query))
        logger.info(response.text)
        return response

    def start_system(self) -> requests.Response:
        login_response = self.login()
        access_token = json.loads(login_response.text)["access_token"]

        url = self._create_url("api/v1/start_system")
        headers = self._create_headers(
            access_token=access_token,
            extra={
                "Content-Type": "application/json",
            },
        )
        query = {}
        response = requests.post(url=url, headers=headers, data=json.dumps(query))
        logger.info(response.text)
        return response

    def stop_system(self) -> requests.Response:
        login_response = self.login()
        access_token = json.loads(login_response.text)["access_token"]

        url = self._create_url("api/v1/stop_system")
        headers = self._create_headers(
            access_token=access_token,
            extra={
                "Content-Type": "application/json",
            },
        )
        query = {}
        response = requests.post(url=url, headers=headers, data=json.dumps(query))
        logger.info(response.text)
        return response


raspiApiClient = RasPiApiClient(
    prefix_url=settings.RASPI_API_SERVER_BASE_URL,
    auth_user_username=settings.RASPI_API_USER_USERNAME,
    auth_user_password=settings.RASPI_API_USER_PASSWORD,
)
