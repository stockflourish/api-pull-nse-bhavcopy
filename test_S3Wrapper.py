from unittest import TestCase
from services.S3Wrapper import S3Wrapper
from constants.constants import STOCK_DATA_BUCKET
from services.ZipService import ZipService
from services.NseService import NseService
import requests
import os


class TestS3Wrapper(TestCase):
    def test_upload_file(self):
        nse_service = NseService(year="2021", month="03", day="31")
        nse_data_response: requests.Response = nse_service.get_data()

        assert nse_data_response.status_code == 200
        zip_service = ZipService(bytes_data=nse_data_response.content)
        zip_service.extract_all()

        assert zip_service.extract_path is not None

        s3_wrapper = S3Wrapper(bucket_name=STOCK_DATA_BUCKET, folder_name="stock_prices_daily")

        s3_wrapper.upload_file(local_file_path=str(zip_service.extract_path), local_file_name=nse_service.file_name)

        assert True
