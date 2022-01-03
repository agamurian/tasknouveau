from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False) 
    text = db.Column(db.String(10000), nullable=False) 


@app.get("/notes")
def notes():
    response_object = {'status': 'success'}
    notes = Note.query
    response_list = []
    for note in notes:
        response_list.append({
            'id': notes.id,
            'name': notes.name,
            'text': notes.text,
        })
    response_object['notes'] = response_list
    return jsonify(response_object)

@app.get("/note/{id}")
def note(id):
    pass

@app.get("/")
def hello_world():
    return jsonify({"result":"success"})
