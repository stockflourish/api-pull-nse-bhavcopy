import requests


class NseService:
    _month_name_dict = {
        "01": "JAN", "02": "FEB", "03": "MAR", "04": "APR", "05": "MAY", "06": "JUN",
        "07": "JUL", "08": "AUG", "09": "SEP", "10": "OCT", "11": "NOV", "12": "DEC"}

    def __init__(self, *, year: str, month: str, day: str):
        self.year = year
        self.month = month
        self.day = day
        self._file_name = "cm{}bhav.csv".format(self._get_date_mmm_format())

    @property
    def file_name(self):
        return self._file_name

    def get_data(self) -> requests.Response:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63',
            'Upgrade-Insecure-Requests': '1',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'www1.nseindia.com',
            'Referer': 'https://www1.nseindia.com/products/content/equities/equities/archieve_eq.htm',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'}

        resp1 = requests.get('https://www1.nseindia.com/products/content/equities/equities/archieve_eq.htm',
                             headers=headers)

        _date = self._get_date()

        _ = requests.get(
            "https://www1.nseindia.com/ArchieveSearch?h_filetype=eqbhav&date={}&section=EQ".format(_date),
            headers=headers,
            cookies=resp1.cookies
        )

        _date_mmm_format = self._get_date_mmm_format()
        _month_mmm_format = self._month_name_dict.get(self.month)
        resp3 = requests.get(
            "https://www1.nseindia.com/content/historical/EQUITIES/{}/{}/cm{}bhav.csv.zip"
                .format(self.year, _month_mmm_format, _date_mmm_format),
            headers=headers
        )

        return resp3

    def _get_date(self) -> str:
        return "{}-{}-{}".format(self.day, self.month, self.year)

    def _get_date_mmm_format(self) -> str:
        return "{}{}{}".format(self.day, self._month_name_dict.get(self.month), self.year)
