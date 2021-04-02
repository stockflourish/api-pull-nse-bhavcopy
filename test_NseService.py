from unittest import TestCase
from services.NseService import NseService
import requests


class TestNseService(TestCase):
    def test_get_data(self):
        nse_service = NseService(year="2021", month="04", day="01")
        nse_data_response: requests.Response = nse_service.get_data()

        assert nse_data_response.status_code == 200
        assert nse_data_response.content is not None
