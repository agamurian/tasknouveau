from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.String, unique=True, primary_key=True)
    name = db.Column(db.String(120), nullable=False) 
    text = db.Column(db.String(10000), nullable=False) 


@app.get("/notes")
def get_notes():
    response_object = {'status': 'success'}
    notes = Note.query.all()
    print(notes)
    response_list = []
    for note in notes:
        print(note)
        response_list.append({
            'id': note.id,
            'name': note.name,
            'text': note.text,
        })
    response_object['notes'] = response_list
    return jsonify(response_object)

@app.post("/note")
def new_note():
    response_object = {'status':'success'}
    note_data = request.get_json()
    generated_id = secrets.token_hex(4)
    print(generated_id)
    name = note_data.get('name')
    text = note_data.get('text')
    note = Note(id=generated_id, name=name, text=text)
    db.session.add(note)
    db.session.commit()
    print(note)
    return jsonify(response_object)


@app.get("/note/{id}")
def note(id):
    pass

@app.get("/")
def hello_world():
    return jsonify({"result":"success"})
