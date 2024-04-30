import sqlite3
con = sqlite3.connect("ofdru_Api.db")
cur = con.cursor()
sql = """\
CREATE TABLE user (
    id_user INTEGER PRIMARY KEY AUTOINCREMENT, 
    email TEXT, 
    passw TEXT
);
CREATE TABLE rubr(
    id_rubr INTEGER PRIMARY KEY AUTOINCREMENT,
    name_rubr TEXT 
);
CREATE TABLE site(
    id_site INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER, 
    id_rubr INTEGER, 
    url TEXT, 
    title TEXT, 
    msq TEXT, 
    id INTEGER 
);
"""
try:
    cur.executescript(sql)
except sqlite3.DatabaseError as  err:
    print("Ошибка: ", err)
else:
    print("Запрос успешно выполнен")
cur.close()
con.close()
input()