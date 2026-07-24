import requests

from src.config import Config


class GithubClient:

    BASE_URL = "https://api.github.com/repos/SigmaHQ/sigma"

    def __init__(self):

        self.headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "DetectionPulse-AI"
        }

        # Use authenticated requests if token exists
        if getattr(Config, "GITHUB_TOKEN", None):
            self.headers["Authorization"] = f"Bearer {Config.GITHUB_TOKEN}"

    def get_latest_commit(self):

        url = f"{self.BASE_URL}/commits"

        response = requests.get(
            url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        commits = response.json()

        return commits[0]

    def get_commit_files(self, sha):

        url = f"{self.BASE_URL}/commits/{sha}"

        response = requests.get(
            url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        commit = response.json()

        return commit.get("files", [])

    def download_file(self, path):

        url = (
            "https://raw.githubusercontent.com/"
            f"SigmaHQ/sigma/master/{path}"
        )

        response = requests.get(
            url,
            headers={
                "User-Agent": "DetectionPulse-AI"
            },
            timeout=30
        )

        if response.status_code != 200:
            return None

        return response.text