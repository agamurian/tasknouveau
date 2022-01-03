from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def hello_world():
    return jsonify({"result":"succes"})
