import yaml


class SigmaParser:


    def parse(self, content):

        try:

            return yaml.safe_load(
                content
            )

        except Exception:

            return None


    def get_title(self, rule):

        return rule.get(
            "title",
            "Unknown"
        )


    def get_description(self, rule):

        return rule.get(
            "description",
            ""
        )


    def get_level(self, rule):

        return rule.get(
            "level",
            "unknown"
        )


    def get_tags(self, rule):

        return rule.get(
            "tags",
            []
        )


    def get_logsource(self, rule):

        return rule.get(
            "logsource",
            {}
        )


    def get_detection(self, rule):

        return rule.get(
            "detection",
            {}
        )


    def get_id(self, rule):

        return rule.get(
            "id",
            ""
        )