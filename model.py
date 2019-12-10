"""Initializes sqlite database and creates a table"""

import sqlite3


connection = sqlite3.connect('info.db', check_same_thread=False)
cursor = connection.cursor()


def user_phonenumber_query(search_string):
    # The SQL injection happens in this sql query, try --> jaime" or "1" ="1
    cursor.execute(f'SELECT first_name, last_name, phone_number FROM Users WHERE first_name="{search_string}"')
    # The fix for the above query is
    # cursor.execute('SELECT first_name, last_name, phone_number FROM Users WHERE first_name=:firstname',
    #                {'firstname': search_string})
    rows = cursor.fetchall()
    return rows


cursor.execute('DROP TABLE IF EXISTS Users')
cursor.execute('CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT,'
               ' first_name VARCHAR(20), last_name VARCHAR(20), phone_number TEXT, current_address TEXT)')
cursor.execute('INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
               ('Jaime', 'Lannister', '+35864682', 'Riverlands'))
cursor.execute('INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
               ('Tyrion', 'Lannister', '+35858424', 'Meereen'))
cursor.execute('INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
               ('Doran', 'Martell', '+35862334', 'Sunspear'))
cursor.execute('INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
               ('Petyr', 'Baelish', '+35896393', 'Vale of Arryn'))
cursor.execute('INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
               ('Shadrich', 'The Mad Mouse', '+35809057', 'Vale of Arryn'))

connection.commit()


