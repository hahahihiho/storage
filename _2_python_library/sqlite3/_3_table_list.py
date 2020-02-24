import sqlite3

db_path = './db/example.db'

def showTable():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
    select name from sqlite_master
    where type='table'
    '''
    cur.execute(sql)
    r = cur.fetchall()
    print(r)

    conn.commit()
    conn.close()