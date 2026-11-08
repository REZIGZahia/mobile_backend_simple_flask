from flask import Flask, jsonify
import json
import datetime
from pathlib import Path

app = Flask(__name__)


@app.route("/news.all.get")
def get_news_all_articles():
    data_file = Path(__file__).parent / "news_data.json"
    with open(data_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    app.logger.debug("Hello %s", data)
    return jsonify(data)


@app.route("/news.categories.get")
def get_news_categories():
    time_now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "title": "List of Categories",
        "time": time_now_str,
        "categories": [
            {"id": 1, "name": "Sports"},
            {"id": 2, "name": "Politics"},
            {"id": 3, "name": "Education"}
        ]
    }
    return jsonify(data)


@app.route("/")
def index():
    return jsonify({
        "message": "Welcome ENSIA Students from Flask!"
    })
