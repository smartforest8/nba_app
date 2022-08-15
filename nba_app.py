import os
from flask import Flask, url_for, render_template, jsonify
from functions.use_api import get_curry
app = Flask(__name__)

# ルーティング
@app.route("/shotchart",methods=['GET'])
def shortchart():
    json_curry = get_curry()
    return render_template('shotchart.html', shotchart = json_curry)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=8000, debug=True)