from src.utils import create_hash


class Fingerprint:


    def generate(self, rule):

        important_data = {

            "title": rule.get(
                "title"
            ),

            "description": rule.get(
                "description"
            ),

            "level": rule.get(
                "level"
            ),

            "tags": rule.get(
                "tags"
            ),

            "logsource": rule.get(
                "logsource"
            ),

            "detection": rule.get(
                "detection"
            )
        }


        return create_hash(
            important_data
        )