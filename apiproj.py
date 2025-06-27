import requests
import sqlalchemy as db
import pandas as pd
API_TOKEN = "23dd00f6561d4d8e963b967f9af1952f"

url = "https://api.football-data.org/v4/competitions/PL/standings"
headers = {
    "X-Auth-Token": API_TOKEN
}
response = requests.get(url, headers=headers)
data = response.json()
standings = data['standings'][0]['table']
teams = []
for team in standings:
    teams.append({
        "position": team["position"],
        "team_name": team["team"]["name"],
        "playedGames": team["playedGames"],
        "won": team["won"],
        "draw": team["draw"],
        "lost": team["lost"],
        "points": team["points"],
        "goalDifference": team["goalDifference"]
    })
df = pd.DataFrame(teams)
engine = db.create_engine('sqlite:///data_base_name.db')
df.to_sql('table_name', con=engine, if_exists='replace', index=False)
with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))



