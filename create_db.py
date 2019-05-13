import sqlite3

conn = sqlite3.connect('Face-DataBase.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Attendance5(Id INTEGER PRIMARY KEY, Roll NUMERIC, Name BLOB, Date BLOB, Time BLOB, Subject TEXT, Status TEXT)')


create_table()