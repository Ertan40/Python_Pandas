import pandas as pd
import json
from pathlib import Path

# Configuration
INPUT_DIR = Path("C:/Users/ertan/Downloads/a-datasets/dataset_cricket_json/")
OUTPUT_DIR = INPUT_DIR
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load match data
with open(INPUT_DIR / "t20_wc_match_results.json") as f:
    match_data = json.load(f)
df_match = pd.DataFrame(match_data[0]['matchSummary'])
df_match = df_match.rename(columns={'scorecard': 'match_id'})

# Process batting data
with open(INPUT_DIR / "t20_wc_batting_summary.json") as f:
    batting_data = json.load(f)

all_records = []
for record in batting_data:
    all_records.extend(record['battingSummary'])
df_batting = pd.DataFrame(all_records)

# Clean data
df_batting['out/not_out'] = df_batting['dismissal'].apply(lambda x: 'out' if len(x) > 0 else 'not_out')
# df_batting['out/not_out'] = df_batting['dismissal'].apply(
#     lambda x: 'out' if x.strip() else 'not_out'
# )

df_batting = df_batting.drop(columns=['dismissal'])
df_batting['batsmanName'] = (
    df_batting['batsmanName']
    .str.replace('â€', '')
    .str.replace('\xa0', '')
)

# Create dictionary and add match IDs
match_ids_dict = {}
for index, row in df_match.iterrows():
    key1 = row['team1'] + ' Vs ' + row['team2']
    key2 = row['team2'] + ' Vs ' + row['team1']

    match_ids_dict[key1] = row['match_id']
    match_ids_dict[key2] = row['match_id']

df_batting['match_id'] = df_batting['match'].map(match_ids_dict)

# Process bowling data
with open(INPUT_DIR / "t20_wc_bowling_summary.json") as f:
    bowling_data = json.load(f)

bowling_records = []
for record in bowling_data:
    bowling_records.extend(record['bowlingSummary'])

df_bowling = pd.DataFrame(bowling_records)
df_bowling['match_id'] = df_bowling['match'].map(match_ids_dict)

with open(INPUT_DIR / "t20_wc_player_info.json") as f:
    data_players = json.load(f)

df_players = pd.DataFrame(data_players)
# Clean names
df_players['name'] = df_players['name'].apply(lambda x: x.replace('\xa0', '').replace('â€', '').replace('†', ''))

# Save files
df_match.to_csv(OUTPUT_DIR / "dim_match_summary.csv", index=False)
df_batting.to_csv(OUTPUT_DIR / "fact_batting_summary.csv", index=False)
df_bowling.to_csv(OUTPUT_DIR / "fact_bowling_summary.csv", index=False)
df_players.to_csv(OUTPUT_DIR / "dim_players.csv", index=False)

print("Files created successfully!")