import sqlite3

db_path = './db/example.db'

# sql connect decorator
def connectSql(f):
    def function(*args, **kwargs):
        conn=sqlite3.connect(db_path)
        cur=conn.cursor()
        conn.execute('pragma foreign_keys=ON')

        sql = f(*args, **kwargs)
        sql_list = sql.split(';')
        for query in sql_list:
            # try:
            # print(query)
            cur.execute(query)
            # except:
            #     raise ValueError(query)
        result = cur.fetchall()
        conn.commit()
        conn.close()
        return result
    return function


@connectSql
def swapRecordSeq1(data):
    sql = '''
    UPDATE RECORD AS R
    SET seq = (CASE WHEN seq = {seq1} then {seq2} else {seq1} end)
    WHERE date = '{date}' AND seq IN ({seq1},{seq2})
    '''.format(date = data['date'],seq1 = data['seq1'],seq2 = data['seq2'])
    return sql

@connectSql
def swapRecordSeq2(data):
    sql = '''
    UPDATE RECORD AS R
    SET seq = CASE seq
        WHEN {seq1} THEN {seq2}
        WHEN {seq2} THEN {seq1}
    END
    WHERE date = '{date}'
    '''.format(date = data['date'],seq1 = data['seq1'],seq2 = data['seq2'])
    return sql


# if __name__ == "__main__":
#     # 값을 넣고난 뒤 swap 가능
#     data = {"date":'2020-01-01',"seq1":0, "seq2":1}
#     result = db.swapRecordSeq(data)