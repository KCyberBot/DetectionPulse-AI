import hashlib
import json


def create_hash(data):

    if isinstance(data, dict):
        data = json.dumps(
            data,
            sort_keys=True
        )

    return hashlib.sha256(
        data.encode()
    ).hexdigest()


def safe_get(dictionary, key, default=None):

    if not dictionary:
        return default

    return dictionary.get(
        key,
        default
    )