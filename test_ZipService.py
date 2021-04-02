from unittest import TestCase
from services.ZipService import ZipService
from services.NseService import NseService
import requests
import os
from os import path


class TestZipService(TestCase):
    def test_extract_all(self):
        nse_service = NseService(year="2021", month="03", day="31")
        nse_data_response: requests.Response = nse_service.get_data()

        assert nse_data_response.status_code == 200
        zip_service = ZipService(bytes_data=nse_data_response.content)
        zip_service.extract_all()

        assert zip_service.extract_path is not None

        file_with_path = os.path.join(str(zip_service.extract_path), nse_service.file_name)

        print(file_with_path)
        assert path.exists(file_with_path)
