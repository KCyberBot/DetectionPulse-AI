import requests

from src.config import Config
from src.logger import get_logger


logger = get_logger()


class TelegramClient:


    def __init__(self):

        self.token = Config.TELEGRAM_TOKEN
        self.chat_id = Config.TELEGRAM_CHAT_ID


    def send_message(self, message):

        if not self.token or not self.chat_id:

            logger.warning(
                "Telegram credentials missing"
            )

            return False


        url = (
            f"https://api.telegram.org/"
            f"bot{self.token}/sendMessage"
        )


        payload = {

            "chat_id": self.chat_id,

            "text": message,

            "parse_mode": "Markdown"

        }


        response = requests.post(
            url,
            json=payload,
            timeout=30
        )


        if response.status_code == 200:

            logger.info(
                "Telegram notification sent"
            )

            return True


        logger.error(
            response.text
        )

        return False