from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://username:password@inner_path:port/users"

db = SQLAlchemy(app)


class UserInfo(db.Model):
    __tablename__ = 'userinfo'

    id = db.Column(db.Integer, primary_key=True)
    authority = db.Column(db.Integer, nullable=False)


class LoginRecord(db.Model):
    __tablename__ = 'loginrecord'

    num = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Integer)
