import sqlite3

# 연결
conn=sqlite3.connect('./db/example.db')
cur=conn.cursor()

##### 방식1
symbol='aaa'

# 실행(select)
cur.execute("select * from stocks where symbol='%s'" %symbol)

# 값 가져오기
items = cur.fetchall()
for i,item in enumerate(items):
    print(i,item)

##### 방식2
t=('RHAT',2)
sql="select * from stocks where symbol=? and qty=?"
cur.execute(sql,t)

print(cur.fetchall())


conn.close()