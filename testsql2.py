# -*- coding: utf-8 -*-

import sqlite3
con = sqlite3.connect("ofdru_Api.db")
cur = con.cursor()
sql = """\
INSERT INTO user (email, passw)
values ('unicross@mail.ru', 'password1')
"""
try:
    cur.execute(sql)
except sqlite3.DatabaseError as err:
    print("пишипка: ", err)
else:
    print("Готово")
    con.commit()
cur.close()
con.close()

input()