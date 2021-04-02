from unittest import TestCase
from services.DateService import DateService


class TestDateService(TestCase):
    def test_date_time_date(self):
        date_service = DateService(date_str="02-04-2021", date_format="%d-%m-%Y")
        assert date_service.date_time_date.weekday() == 4
