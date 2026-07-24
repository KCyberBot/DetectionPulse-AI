from src.config import Config


class Filter:


    def is_interesting(self, rule):

        text = str(rule).lower()


        for keyword in Config.INTEREST_KEYWORDS:

            if keyword in text:

                return True


        return False