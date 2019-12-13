"""Initializes sqlite database and creates a table"""

import sqlite3
from application import db

connection = sqlite3.connect('application/info.db', check_same_thread=False)
cursor = connection.cursor()


class User(db.Model):
    __tablename__ = 'passwords'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=False, unique=True, nullable=False)
    password = db.Column(db.String(50), index=False, unique=False, nullable=False)  # If passwords are hashed, low
    # password limit like (50) doesn't make sense, should be high
    # Passwords are also in plaintext which is a big no-no

    def __repr__(self):
        return f'<User {self.username}'


class Comments(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, unique=False, nullable=False)


def user_phonenumber_query(search_string):
    # The SQL injection happens in this sql query, try --> jaime" or "1" ="1
    cursor.execute(f'SELECT first_name, last_name, phone_number FROM Users WHERE first_name="{search_string}"')
    # The fix for the above query is
    # cursor.execute('SELECT first_name, last_name, phone_number FROM Users WHERE first_name=:firstname',
    #                {'firstname': search_string})
    rows = cursor.fetchall()
    return rows


def db_init():
    cursor.execute('DROP TABLE IF EXISTS Users')
    cursor.execute('CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT,'
                   ' first_name VARCHAR(20), last_name VARCHAR(20), phone_number TEXT, current_address TEXT)')
    cursor.execute(
        'INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
        ('Jaime', 'Lannister', '+35864682', 'Riverlands'))
    cursor.execute(
        'INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
        ('Tyrion', 'Lannister', '+35858424', 'Meereen'))
    cursor.execute(
        'INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
        ('Doran', 'Martell', '+35862334', 'Sunspear'))
    cursor.execute(
        'INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
        ('Petyr', 'Baelish', '+35896393', 'Vale of Arryn'))
    cursor.execute(
        'INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
        ('Shadrich', 'The Mad Mouse', '+35809057', 'Vale of Arryn'))
    connection.commit()


