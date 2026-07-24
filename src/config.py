import os


class Config:

    # GitHub
    SIGMA_OWNER = "SigmaHQ"
    SIGMA_REPO = "sigma"
    SIGMA_BRANCH = "master"

    GITHUB_API = (
        f"https://api.github.com/repos/"
        f"{SIGMA_OWNER}/{SIGMA_REPO}"
    )

    RAW_URL = (
        f"https://raw.githubusercontent.com/"
        f"{SIGMA_OWNER}/{SIGMA_REPO}/"
        f"{SIGMA_BRANCH}/"
    )

    # Telegram (will be used in Pack 2)
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    # AI (will be used in Pack 2)
    AI_PROVIDER = os.getenv(
        "AI_PROVIDER",
        "github"
    )

    AI_TOKEN = os.getenv("AI_TOKEN")

    # Database
    DATABASE_PATH = (
        "database/detectionpulse.db"
    )

    # Filters
    ENABLE_CLOUD_RULES = False

    INTEREST_KEYWORDS = [
        "windows",
        "linux",
        "sysmon",
        "powershell",
        "active directory",
        "kerberos",
        "ldap",
        "defender",
        "exchange",
        "ivanti",
        "fortinet",
        "palo alto",
        "cisco",
        "firewall",
        "vpn",
        "dns",
        "smb",
        "rdp",
        "ransomware"
    ]