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


# CRUD

@app.get("/notes")
def get_all_notes():
    response_object = {'status': 'success'}
    notes = Note.query.all()
    response_list = []
    for note in notes:
        response_list.append({
            'id': note.id,
            'name': note.name,
            'text': note.text,
        })
    response_object['notes'] = response_list
    return jsonify(response_object)


@app.post("/note")
def create_note():
    response_object = {'status':'success'}
    note_data = request.get_json()
    generated_id = secrets.token_hex(4)
    name = note_data.get('name')
    text = note_data.get('text')
    note = Note(id=generated_id, name=name, text=text)
    db.session.add(note)
    db.session.commit()
    return jsonify(response_object)


@app.get("/note/<id>")
def get_note(id):
    response_object = {'status': 'success'}
    note = Note.query.get_or_404(id)
    response_list = {
        'id': note.id,
        'name': note.name,
        'text': note.text,
    }
    response_object['note'] = response_list
    return jsonify(response_object)


@app.post("/note/<id>")
def update_note(id):
    response_object = {'status': 'success'}
    note = Note.query.get_or_404(id)
    note_data = request.get_json()
    note.name = note_data.get('name')
    note.text = note_data.get('text')
    db.session.add(note)
    db.session.commit()
    return jsonify(response_object)


@app.delete("/note/<id>")
def delete_note(id):
    response_object = {'status': 'success'}
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return jsonify(response_object)


@app.get("/")
def hello_world():
    return jsonify({"result":"success"})
