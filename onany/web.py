from typing import Any, Dict
import requests


def webhook_callback(rules: Dict[str, Any]) -> callable:
    def wrapper(*args, **kwargs):
        response = requests.post(
            rules.get("route"),
            json=kwargs.get("data"),
            headers=kwargs.get("headers"))

        if rules.get("callback"):
            rules.get("callback")(response)

    return wrapper
