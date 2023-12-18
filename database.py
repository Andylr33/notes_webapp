from sqlalchemy import create_engine, text
from flask_login import UserMixin
import os
from werkzeug.security import check_password_hash, generate_password_hash

db_connection_string = os.environ['NOTES_APP_DB']
engine = create_engine(db_connection_string) # "mysql+pymysql://sylvain:passwd@localhost/db?host=localhost?port=3306" <-- sample of how to connect to local machine

def create_user_account(data):
    with engine.connect() as conn:
        query = "INSERT INTO users (email, hash, full_name) VALUES (:email, :hash, :full_name);"
        
        conn.execute(text(query), 
                        {"email": data['email'], "hash": generate_password_hash(data['password1']),
                        "full_name": data['full_name']})
        conn.execute(text("commit;"))                   # MUST COMMIT TO SEE CHANGES IN DATABASE!!
        print("User was added to the database!")

def check_if_user_exists(data):
    with engine.connect() as conn:
        query = "SELECT * FROM users WHERE email = :email;"
        result = conn.execute(text(query),
                    {"email": data['email']})
        rows = result.all()
        # print(f"The length of rows is {len(rows)}")
        if len(rows) ==  1:
            return True
        else:
            return False
        
def get_user_info(data):
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM users WHERE email = :email;"), {"email": data['email']}) # pass in parameters as dictionary key-value pair
            rows = result.all()
            if len(rows) == 0:
                return None
            else: 
                return dict(rows[0]._mapping)


def add_note(user_id, note):
    with engine.connect() as conn:
        query = "INSERT INTO notes (user_id, note_data) VALUES (:user_id, :note_data);"
        
        conn.execute(text(query), 
                        {"user_id": user_id, "note_data": note})
        conn.execute(text("commit;"))                   # MUST COMMIT TO SEE CHANGES IN DATABASE!!

def get_notes(user_id):
    with engine.connect() as conn:
        query = "SELECT * FROM notes WHERE user_id = :user_id;"
        
        result = conn.execute(text(query), 
                        {"user_id": user_id})
        conn.execute(text("commit;"))                   # MUST COMMIT TO SEE CHANGES IN DATABASE!!
        
        rows = result.all()

        notes = [] # list of dictionaries

        for row in rows:
            notes.append(dict(row._mapping)) # add dictionary to list
        return notes

def delete_note():
    pass
