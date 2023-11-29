from flask import Flask, request, jsonify
from change import df
import sqlite3
app = Flask(__name__)
connection = sqlite3.connect("nba.db", check_same_thread=False)
cursor = connection.cursor()


@app.route('/', methods=['GET'])
def index():
    return "NBA API"

@app.route('/players/<player_name>', methods=['GET'])
def get_players(player_name):
    result = None
    try:
        cursor.execute(f"SELECT * FROM nba_base WHERE Player='{player_name}'")
        result = cursor.fetchall()
    except Exception as e:
        print("Error: ",  e)

    
    if result:
        player_data = {
            "Name": result[0][1],
            "Position": result[0][2],
            "Age": result[0][3],
            "Team": result[0][4],
            "Games": result[0][5],
            "Minutes Played": result[0][6],
            "Field Goals": result[0][7],
            "Field Goal Attempts": result[0][8],
            "Field Goal Percentage": result[0][9],
            "Three Pointers": result[0][10],
            "Three Point Attempts": result[0][11],
            "Three Point Percentage": result[0][12],
            "Two Pointers": result[0][13],
            "Two Point Attempts": result[0][14],
            "Two Point Percentage": result[0][15]
            

        }
        return jsonify(player_data)
    else:
        return jsonify({"Message" : "Incorrect Player Name"})

@app.route('/points/highest', methods=['GET']) 
def get_highest_pts():
    try: 
        highest_pts_index = df["PTS"].idxmax()
        player_name = df.loc[highest_pts_index, "Player"]
        pts = df.loc[highest_pts_index, "PTS"]

        data = {
        "Player: " : player_name,
        "Points: " : pts
        }
        return jsonify(data)
    except Exception as e:
        return jsonify(f"Error occurred: {e} \n Try again")
    
@app.route('/points/least', methods=['GET']) 
def get_least_pts():
    try: 
        least_pts_index = df["PTS"].idxmin()
        player_name = df.loc[least_pts_index, "Player"]
        pts = df.loc[least_pts_index, "PTS"]

        data = {
        "Player: " : player_name,
        "Points: " : pts
        }
        return jsonify(data)
    except Exception as e:
        return jsonify(f"Error occurred: {e} \n Try again")
    
@app.route("/assists/highest", methods=['GET'])
def get_most_assists():
    try: 
        highest_ast_index = df["AST"].idxmax()
        player_name = df.loc[highest_ast_index, "Player"]
        ast = df.loc[highest_ast_index, "AST"]

        data = {
            "Player: " : player_name,
            "Assists: " : ast
        }

        return jsonify(data)

    except Exception as e:
        return {f"Error occurred: {e} \n Try again"}
    
@app.route("/assists/least", methods=['GET'])
def get_least_assists():
    try: 
        least_ast_index = df["AST"].idxmin()
        player_name = df.loc[least_ast_index, "Player"]
        ast = df.loc[least_ast_index, "AST"]

        data = {
            "Player: " : player_name,
            "Assists: " : ast
        }

        return jsonify(data)

    except Exception as e:
        return {f"Error occurred: {e} \n Try again"}

@app.route('/rebounds/highest', methods=['GET'])
def get_most_rebounds():
    try:
        most_rbs_index = df["TRB"].idxmax()
        player_name = df.loc[most_rbs_index, "Player"]
        rbs = df.loc[most_rbs_index, "TRB"]

        data = {
            "Player: ": player_name,
            "Rebounds: " : rbs
        }

        return jsonify(data)
    except Exception as e:
        return {f"Error occurred: {e} \n Try again"}
@app.route('/rebounds/least', methods=['GET'])
def get_least_rebounds():
    try:
        least_rbs_index = df["TRB"].idxmin()
        player_name = df.loc[least_rbs_index, "Player"]
        rbs = df.loc[least_rbs_index, "TRB"]

        data = {
            "Player: ": player_name,
            "Rebounds: " : rbs
        }

        return jsonify(data)
    except Exception as e:
        return {f"Error occurred: {e} \n Try again"}
@app.route('/blocks/highest', methods=['GET'])   
def get_highest_blocks():
    try:
        most_blocks_index = df["BLK"].idxmax()
        player_name = df.loc[most_blocks_index, "Player"]
        blks = df.loc[most_blocks_index, "BLK"]

        data = {
            "Player: ": player_name,
            "Blocks: " : blks
        }

        return jsonify(data)
    except Exception as e:
        return {f"Error occurred: {e} \n Try again"}
    
@app.route('/blocks/least', methods=['GET'])   
def get_least_blocks():
    try:
        least_blocks_index = df["BLK"].idxmin()
        player_name = df.loc[least_blocks_index, "Player"]
        blks = df.loc[least_blocks_index, "BLK"]

        data = {
            "Player: ": player_name,
            "Blocks: " : blks
        }

        return jsonify(data)
    except Exception as e:
        return {f"Error occurred: {e} \n Try again"}

if __name__ == "__main__":
    app.run(port=8080, debug=True)