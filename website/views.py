import json

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

from . import db
from website.models import Note

views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if (len(note) < 1):
            flash('Note too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()

            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    note_id = note['noteId']
    note_to_delete = Note.query.get(note_id)
    if note_to_delete:
        if note_to_delete.user_id == current_user.id:
            db.session.delete(note_to_delete)
            db.session.commit()

    return jsonify({})