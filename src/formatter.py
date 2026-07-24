class Formatter:


    def priority(self, severity):

        severity = str(
            severity
        ).lower()


        if severity == "critical":
            return "⭐⭐⭐⭐⭐"

        if severity == "high":
            return "⭐⭐⭐⭐"

        if severity == "medium":
            return "⭐⭐⭐"

        return "⭐⭐"



    def create_message(
        self,
        rule,
        environment,
        ai_data=None,
        mitre=None,
        rule_url=None
    ):


        title = rule.get(
            "title",
            "Unknown"
        )


        severity = rule.get(
            "level",
            "unknown"
        )


        tags = rule.get(
            "tags",
            []
        )


        logsource = rule.get(
            "logsource",
            {}
        )


        tags_text = "\n".join(
            str(x)
            for x in tags
        )


        message = f"""
{self.priority(severity)} {severity.upper()}

🔴 NEW SIGMA RULE

🖥 Platform:
{environment}

━━━━━━━━━━━━━━━━━━

📝 Title:
{title}

⚠ Severity:
{severity.upper()}

"""


        message += """
📂 Log Source

"""


        if logsource:

            for key,value in logsource.items():

                message += (
                    f"{key}: {value}\n"
                )

        else:

            message += "Unknown\n"



        if mitre:

            message += """

🎯 MITRE ATT&CK

"""

            message += mitre + "\n"



        if ai_data:

            message += """

🧠 AI Summary

"""


            message += ai_data.get(
                "summary",
                ""
            )


            message += """

💡 Hunt Ideas

"""


            for item in ai_data.get(
                "hunt_ideas",
                []
            ):

                message += (
                    f"• {item}\n"
                )


            message += """

⚠ False Positives

"""


            for item in ai_data.get(
                "false_positives",
                []
            ):

                message += (
                    f"• {item}\n"
                )



        message += """

🏷 Tags

"""


        message += (
            tags_text
            if tags_text
            else "None"
        )


        message += "\n\n🔗 Sigma Rule\n"


        message += (
            rule_url
            if rule_url
            else "Unavailable"
        )


        message += """

━━━━━━━━━━━━━━━━━━

🤖 DetectionPulse AI
"""


        return message