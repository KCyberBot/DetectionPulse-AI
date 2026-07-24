import sqlite3
from pathlib import Path

from src.config import Config


class Database:


    def __init__(self):

        Path("database").mkdir(
            exist_ok=True
        )

        self.conn = sqlite3.connect(
            Config.DATABASE_PATH
        )

        self.create_tables()



    def create_tables(self):

        cursor = self.conn.cursor()


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS rules
        (
            rule_id TEXT PRIMARY KEY,
            title TEXT,
            severity TEXT,
            environment TEXT,
            fingerprint TEXT,
            url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)


        self.conn.commit()



    def check_rule(
        self,
        rule_id,
        fingerprint
    ):

        cursor = self.conn.cursor()


        cursor.execute(
            """
            SELECT fingerprint
            FROM rules
            WHERE rule_id=?
            """,
            (rule_id,)
        )


        result = cursor.fetchone()


        if result is None:

            return "NEW"



        old_fingerprint = result[0]


        if old_fingerprint != fingerprint:

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


        cursor = self.conn.cursor()


        cursor.execute(
            """
            INSERT OR REPLACE INTO rules
            (
                rule_id,
                title,
                severity,
                environment,
                fingerprint,
                url
            )
            VALUES (?,?,?,?,?,?)
            """,
            (
                rule_id,
                title,
                severity,
                environment,
                fingerprint,
                url
            )
        )


        self.conn.commit()