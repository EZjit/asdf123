from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy


metadata = MetaData()


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
