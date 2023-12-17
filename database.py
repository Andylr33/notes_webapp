from sqlalchemy import create_engine, text
from flask_login import UserMixin
import os

db_connection_string = os.environ['NOTES_APP_DB']
engine = create_engine(db_connection_string) # "mysql+pymysql://sylvain:passwd@localhost/db?host=localhost?port=3306" <-- sample of how to connect to local machine

with engine.connect() as conn:
    print("Database was connected!")

