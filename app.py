from flask import Flask, render_template, request, jsonify
from flask_sock import Sock
import json

app = Flask(__name__)
sock = Sock(app)

groups = []


@app.route("/")
def index():
    return render_template("index.html", groups=groups)

@app.route("/ws")
def index2():
    return render_template("index_ws.html", groups=groups)


@sock.route("/connect")
def websocket(ws):
    while True:
        data = ws.receive()
        if data is None:
            break
        msg = json.loads(data)
        name = msg.get("name")
        group = create_group(name)
        row_html = render_template("_group_row.html", group=group)
        ws.send(row_html)


@app.route("/add_group", methods=["POST"])
def add_group():
    name = request.form.get("name")
    if name:
        group = create_group(name)
        row_html = render_template("_group_row.html", group=group)
        return row_html
    return ("", 204)


def create_group(name):
    new_id = len(groups) + 1
    group = {"id": new_id, "name": name}
    groups.append(group)
    return group
