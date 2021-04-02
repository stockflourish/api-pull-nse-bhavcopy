from unittest import TestCase
from services.NseService import NseService
import requests
import pytest
from exception.WeekendException import WeekendException


class TestNseService(TestCase):
    def test_get_data(self):
        nse_service = NseService(year="2021", month="04", day="01")
        nse_data_response: requests.Response = nse_service.get_data()

        assert nse_data_response.status_code == 200
        assert nse_data_response.content is not None

    def test_weekend_exception(self):
        with pytest.raises(WeekendException):
            nse_service = NseService(year="2021", month="04", day="03")
            _ = nse_service.get_data()
