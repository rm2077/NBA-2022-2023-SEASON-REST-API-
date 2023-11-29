import pandas as pd

df = pd.read_csv('data.csv')

def highest_pts(num_players):
    descending_vals = df.sort_values(by='PTS', ascending=False)
    d = descending_vals.head(num_players)
    print(df.columns)

def locate_player(name: str):

    player_find = df[df["Player"] == name]
    if player_find.empty:
        print("Try again..")
    else:
        print(player_find)
highest_pts(10)




