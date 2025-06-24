import requests

API_TOKEN = "23dd00f6561d4d8e963b967f9af1952f"

url = "https://api.football-data.org/v4/competitions/PL/standings"
headers = {
    "X-Auth-Token": API_TOKEN
}
response = requests.get(url, headers=headers)
print(response.json())  


