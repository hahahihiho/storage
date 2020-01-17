import sqlite3

# Check version
print(sqlite3.version)

# db 생성 연결/경로지정 가능
# 없으면 생성
conn=sqlite3.connect('./db/example.db')
cur=conn.cursor()

# create table
cur.execute('''
    create table if not exists stocks(
        date text,
        trans text,
        symbol text,
        qty real,
        price real
    )
''')

# insert values
cur.execute('''
    insert into stocks(date,trans,symbol,qty,price)
        values('2006-0105','BUY','aaa',100,35.14)
''')

conn.commit()
conn.close()
