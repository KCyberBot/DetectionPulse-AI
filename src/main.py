from src.github_client import GithubClient
from src.sigma_parser import SigmaParser
from src.fingerprint import Fingerprint
from src.database import Database
from src.filters import Filter
from src.classifier import Classifier
from src.logger import get_logger

from src.telegram_client import TelegramClient
from src.formatter import Formatter
from src.ai_client import AIClient
from src.mitre import Mitre


logger = get_logger()


github = GithubClient()
parser = SigmaParser()
fingerprint = Fingerprint()
database = Database()

filter_engine = Filter()
classifier = Classifier()

telegram = TelegramClient()
formatter = Formatter()
ai = AIClient()

mitre = Mitre()



def run():

    logger.info(
        "DetectionPulse AI Started"
    )


    commit = github.get_latest_commit()

    sha = commit["sha"]


    logger.info(
        f"Checking commit {sha}"
    )


    files = github.get_commit_files(
        sha
    )


    alerts_sent = 0



    for file in files:


        path = file["filename"]


        # Only Sigma rules

        if not path.startswith(
            "rules/"
        ):

            continue


        if not path.endswith(
            ".yml"
        ):

            continue



        content = github.download_file(
            path
        )


        if not content:

            continue



        rule = parser.parse(
            content
        )


        if not rule:

            continue



        if not filter_engine.is_interesting(
            rule
        ):

            continue



        rule_id = parser.get_id(
            rule
        )


        if not rule_id:

            continue



        fp = fingerprint.generate(
            rule
        )


        status = database.check_rule(
            rule_id,
            fp
        )


        if status == "UNCHANGED":

            continue



        environment = classifier.detect(
            rule
        )


        logger.info(
            f"{status}: {parser.get_title(rule)}"
        )



        # AI analysis

        ai_result = ai.analyze_rule(
            rule
        )



        # MITRE extraction

        mitre_data = mitre.format(
            rule
        )



        # Direct Sigma URL

        rule_url = (
            "https://github.com/"
            "SigmaHQ/sigma/blob/master/"
            + path
        )



        message = formatter.create_message(

            rule,

            environment,

            ai_result,

            mitre_data,

            rule_url

        )



        if status == "NEW":

            message = (
                "🆕 NEW DETECTION RULE\n\n"
                + message
            )


        elif status == "UPDATED":

            message = (
                "♻️ UPDATED DETECTION RULE\n\n"
                + message
            )



        telegram.send_message(
            message
        )



        database.save_rule(

            rule_id,

            parser.get_title(rule),

            parser.get_level(rule),

            environment,

            fp,

            rule_url

        )


        alerts_sent += 1



    logger.info(
        f"Completed. Alerts sent: {alerts_sent}"
    )



if __name__ == "__main__":

    run()