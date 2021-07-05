from configparser import ConfigParser
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

config = ConfigParser()
config.read('config.ini')

db_url = "mysql+pymysql://{username}:{password}@{inner_path}:{port}/{dbname}".format(
    username=config.get('account', 'USERNAME'),
    password=config.get('account', 'PASSWORD'),
    inner_path=config.get('db_connect', 'INNER_PATH'),
    port=config.get('db_connect', 'PORT'),
    dbname=config.get('db_connect', 'INNER_PATH')
)

con_engine = create_engine(db_url)
Base = declarative_base()
metadata = Base.metadata
DBSession = sessionmaker(bind=con_engine)
session = DBSession()


class UserInfo(Base):
    __tablename__ = 'userinfo'

    uid = Column(Integer, primary_key=True)
    authority = Column(Integer, nullable=False)
    account = Column(String)
    password = Column(String)
    ip = Column(String)


class LoginRecord(Base):
    __tablename__ = 'login_record'

    lid = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer)
    ip = Column(String)
    time = Column(DateTime)


class Update(Base):
    __tablename__ = 'update'

    pid = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer)
    time = Column(DateTime)
    type = Column(String)
    content = Column(String)
