from flask import render_template, request, jsonify, Blueprint

from app.db import db
from app.main.models import FormDataSavedAsJson


bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET'])
def index():
    return render_template('main/index.html')


@bp.route('/submit', methods=['POST'])
def submit():
    form_data = request.json
    if not form_data:
        form_data = request.form.to_dict()
    new_data = FormDataSavedAsJson(data=form_data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify({'message': 'Data saved successfully'}), 201


@bp.route('/list', methods=['GET'])
def get_list_of_saved_data():
    all_entries = FormDataSavedAsJson.query.all()
    data = [entry.to_dict() for entry in all_entries]
    return jsonify({'data': data})
