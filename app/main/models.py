from sqlalchemy.dialects.postgresql import JSONB

from app.db import db


class FormDataSavedAsJson(db.Model):
    __tablename__ = 'form_data_as_jsonb'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSONB, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data
        }
