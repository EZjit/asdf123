from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import  Integer, Column
from sqlalchemy.dialects.postgresql import JSONB


app = Flask(__name__)
CORS(app)

# Configure postgres
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://flask_user:qwerty@localhost:5432/flask_db'
db = SQLAlchemy(app)


# model
class FormDataSavedAsJson(db.Model):
    __tablename__ = 'form_data_as_jsonb'
    id = Column(Integer, primary_key=True)
    data = Column(JSONB, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data
        }

# create db table
with app.app_context():
    db.create_all()


# routes
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.json
    if not form_data:
        form_data = request.form.to_dict()
    new_data = FormDataSavedAsJson(data=form_data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify({'message': 'Data saved successfully'}), 201


@app.route('/list', methods=['GET'])
def get_list_of_saved_data():
    all_entries = FormDataSavedAsJson.query.all()
    data = [entry.to_dict() for entry in all_entries]
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(debug=True)
