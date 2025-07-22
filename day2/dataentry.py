import sqlite3
conn=sqlite3.connect('mydata.db')

cursor=conn.cursor()
cursor.execute("insert into user(name,age) Values(?,?)",("alice",25))
cursor.execute("insert into user(name,age) Values(?,?)",("boby",45))
conn.commit()
conn.close()