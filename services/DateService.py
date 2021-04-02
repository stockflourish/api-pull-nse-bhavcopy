import datetime


class DateService:
    def __init__(self, *, date_str: str, date_format: str):
        self.date_str = date_str
        self.date_format = date_format
        self._date_time_date = datetime.datetime.strptime(self.date_str, self.date_format)

    @property
    def date_time_date(self):
        return self._date_time_date
