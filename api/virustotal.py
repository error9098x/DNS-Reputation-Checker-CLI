import requests
from config import API_KEY, API_URL

def get_reputation(domain):
    headers = {
        'x-apikey': API_KEY
    }
    response = requests.get(API_URL + domain, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch data"}
