import json
import requests

from src.config import Config
from src.logger import get_logger
from src.prompts import SYSTEM_PROMPT


logger = get_logger()


class AIClient:


    def __init__(self):

        self.token = Config.AI_TOKEN



    def analyze_rule(self, rule):


        if not self.token:

            logger.warning(
                "AI token missing, using fallback"
            )

            return self.fallback()



        payload = {

            "model": "gpt-4o-mini",

            "messages": [

                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": json.dumps(rule)
                }

            ]

        }


        headers = {

            "Authorization":
            f"Bearer {self.token}",

            "Content-Type":
            "application/json"

        }


        try:

            response = requests.post(

                "https://models.inference.ai.azure.com/chat/completions",

                headers=headers,

                json=payload,

                timeout=60

            )


            response.raise_for_status()


            result = response.json()


            content = (
                result["choices"][0]
                ["message"]
                ["content"]
            )


            return json.loads(content)


        except Exception as error:


            logger.error(
                f"AI error: {error}"
            )


            return self.fallback()



    def fallback(self):

        return {

            "summary":
            "AI analysis unavailable.",


            "why_it_matters":
            "Review the Sigma rule manually.",


            "hunt_ideas":
            [],


            "false_positives":
            [],


            "investigation_steps":
            [],


            "required_logs":
            [],


            "priority":
            3

        }