from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

db_url = "mysql+pymysql://{username}:{password}@{inner_path}:{port}/users".format(
    username=config.get('account', 'USERNAME'),
    password=config.get('account', 'PASSWORD'),
    inner_path=config.get('db_connect', 'INNER_PATH'),
    port=config.get('db_connect', 'PORT')
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)


class UserInfo(db.Model):
    __tablename__ = 'userinfo'

    id = db.Column(db.Integer, primary_key=True)
    authority = db.Column(db.Integer, nullable=False)
    account = db.Column()


class LoginRecord(db.Model):
    __tablename__ = 'loginrecord'

    num = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    iplist = db.Column(db.String)


class UseRecord(db.Model):
    __tablename__ = 'loginrecord'

    num = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Integer, db.ForeignKey('userinfo.id'))
    uselist = db.Column(db.String)
