import io
import zipfile
import tempfile


class ZipService:
    def __init__(self, *, bytes_data: bytes):
        self.bytes_data = bytes_data
        self._extract_path = tempfile.mkdtemp()

    def extract_all(self):
        z = zipfile.ZipFile(io.BytesIO(self.bytes_data))
        z.extractall(path=self._extract_path)

    @property
    def extract_path(self):
        return self._extract_path
