class Mitre:


    def extract(self, rule):

        tags = rule.get(
            "tags",
            []
        )


        techniques = []


        for tag in tags:

            tag = str(tag)


            # Sigma format:
            # attack.t1059.001

            if "attack." in tag.lower():

                technique = (
                    tag.lower()
                    .replace(
                        "attack.",
                        ""
                    )
                )


                techniques.append(
                    technique.upper()
                )


        return techniques



    def format(self, rule):

        techniques = self.extract(
            rule
        )


        if not techniques:

            return "Not mapped"


        return "\n".join(
            techniques
        )