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
