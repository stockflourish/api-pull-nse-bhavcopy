import boto3
from constants.constants import REGION
from exception.AWSException import AWSException
from botocore.exceptions import ClientError, NoCredentialsError
import os


class S3Wrapper:
    def __init__(self, *, bucket_name: str, folder_name: str):
        self.bucket_name = bucket_name
        self.folder_name = folder_name
        try:
            self.s3_client = boto3.client('s3', region_name=REGION)
        except ClientError as error:
            # Put your error handling logic here
            raise AWSException(error)
        except NoCredentialsError as error:
            raise AWSException(error)

    def upload_file(self, *, local_file_path: str, local_file_name: str):
        file_with_path = os.path.join(local_file_path, local_file_name)

        self.s3_client.upload_file(
            file_with_path,
            self.bucket_name,
            "{}/{}".format(self.folder_name, local_file_name),
            ExtraArgs={'Metadata': {'source': 'nse'}}
        )
