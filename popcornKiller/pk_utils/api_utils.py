from typing import Optional, Dict
import requests, json


def fetch_api_data(url: str) -> Optional[Dict[str, str]]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, json.JSONDecodeError):
        return None
