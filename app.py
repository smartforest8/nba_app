import os
import json
from flask import Flask, url_for, render_template, jsonify, request
from functions.use_api import get_curry, get_playersdata, get_ShotData
app = Flask(__name__)

# ルーティング
@app.route("/shotchart",methods=['GET', 'POST'])
def shortchart():
    json_curry = get_curry()
    nba_players = get_playersdata()
    if request.method == 'GET':
        return render_template('shotchart.html', shotchart = json_curry , nba_players = nba_players)
    else:
        print("json")
        print(request.form['player_name'])
        nba_players = get_playersdata()
        player_id = json.loads(request.form['player_name'])['id']
        player_name = json.loads(request.form['player_name'])['full_name']
        json_curry = get_ShotData(player_id = player_id)
        print(player_name)
        return render_template('shotchart.html', shotchart = json_curry , nba_players = nba_players, player_name = player_name)



@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=8000, debug=True)