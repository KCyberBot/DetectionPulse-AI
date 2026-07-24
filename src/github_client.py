import requests

from src.config import Config
from src.logger import get_logger


logger = get_logger()


class GithubClient:

    def __init__(self):
        self.api = Config.GITHUB_API
        self.raw = Config.RAW_URL


    def get_latest_commit(self):

        url = f"{self.api}/commits"

        response = requests.get(
            url,
            timeout=30
        )

        response.raise_for_status()

        return response.json()[0]


    def get_commit_files(self, sha):

        url = (
            f"{self.api}/commits/"
            f"{sha}"
        )

        response = requests.get(
            url,
            timeout=30
        )

        response.raise_for_status()

        return response.json().get(
            "files",
            []
        )


    def download_file(self, path):

        url = self.raw + path

        response = requests.get(
            url,
            timeout=30
        )

        if response.status_code != 200:
            logger.warning(
                f"Unable to download {path}"
            )
            return None

        return response.text