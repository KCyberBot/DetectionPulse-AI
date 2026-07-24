import json
import os


class Database:

    def __init__(self):

        self.path = "database/state.json"

        os.makedirs(
            "database",
            exist_ok=True
        )

        if not os.path.exists(self.path):

            with open(
                self.path,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump({}, f, indent=4)


    def load(self):

        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    def save(self, data):

        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )


    def check_rule(
        self,
        rule_id,
        fingerprint
    ):

        data = self.load()

        if rule_id not in data:

            return "NEW"

        if data[rule_id]["fingerprint"] != fingerprint:

            return "UPDATED"

        return "UNCHANGED"


    def save_rule(
        self,
        rule_id,
        title,
        severity,
        environment,
        fingerprint,
        url
    ):

        data = self.load()

        data[rule_id] = {

            "title": title,

            "severity": severity,

            "environment": environment,

            "fingerprint": fingerprint,

            "url": url

        }

        self.save(data)