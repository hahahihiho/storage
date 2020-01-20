########################
# 제작: 2019/09/06
# 수정: 2020/01/20
# 제작자: 조현명(https://github.com/hahahihiho)
# title: 고객관리 시스템-5
########################
# ***Brief Description***
# 고객관리 시스템(curd)을 flask로 web에 구현
# insert,update,delete,search,showTable 기능 구현
#
# *** 더 공부해야할것 ***
# primary key, foreign key 등 sql 다루기
# 배포(deploying) : virtualenv,gunicorn,heroku
########################


from flask import Flask,render_template,request,url_for,redirect
import sqlite3

app=Flask(__name__)

## this is for general sql_excuter(Future version)
# def execute_sql(sql:str,keys:iter):
#     print(sql,keys)
#     data=c.execute(sql,keys)
#     # select
#     data=c.fetchall()
#     return data

def createTable():
    conn=sqlite3.connect('./db/customerList.sql')
    cur=conn.cursor()
    sql='''    
        create table if not exists customerList(
            name text,
            gender text,
            email text,
            byear int
        )
    '''
    cur.execute(sql)

    conn.commit()
    conn.close()

def insertSQL(data):
    conn=sqlite3.connect('./db/customerList.sql')
    cur=conn.cursor()
    sql='insert into customerList(name,gender,email,byear) values(?,?,?,?)'
    key=data
    
    cur.execute(sql,key)

    conn.commit()
    conn.close()

def selectAllSQL():
    conn=sqlite3.connect('./db/customerList.sql')
    cur=conn.cursor()
    sql='select * from customerList'
    cur.execute(sql)

    customerList = cur.fetchall()

    conn.commit()
    conn.close()
    return customerList

def updateSQL(data):
    conn=sqlite3.connect('./db/customerList.sql')
    cur=conn.cursor()
    sql='UPDATE customerList SET name=?,gender=?,byear=? WHERE email=?'
    cur.execute(sql,data)

    conn.commit()
    conn.close()


def deleteSQL(email):
    conn=sqlite3.connect('./db/customerList.sql')
    cur=conn.cursor()
    sql='DELETE FROM customerList WHERE email=?'
    cur.execute(sql,(email,))

    conn.commit()
    conn.close()

def searchSQL(email):
    conn=sqlite3.connect('./db/customerList.sql')
    cur=conn.cursor()
    sql='select * from customerList where email=?'
    cur.execute(sql,(email,))
    data = cur.fetchall()
    conn.commit()
    conn.close()

    return data

# app
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/insertCustomer/',methods=['GET','POST'])
def insertcustomer():
    if request.method =='GET':
        return render_template('insertCustomer.html')
    elif request.method =='POST':

        name=request.form['name']
        gender=request.form['gender']
        email=request.form['email']
        byear=request.form['byear']
        data=[name,gender,email,byear]

        createTable()

        insertSQL(data)

        return redirect('/showData/')

@app.route('/showData/', methods=['GET','POST'])
def showdata():
    if request.method=='GET':
        
        customerList = selectAllSQL()
        
        return render_template('showData.html',table=customerList)
    elif request.method=='POST':
        # 고객정보 수정,삭제
        req = request.form
        name = req.get('name')
        gender = req.get('gender')
        email = req.get('email')
        byear = req.get('birth-year')
        action = request.form.get('action')

        if action == 'update':
            data = [name,gender,byear,email]
            updateSQL(data)
        else :
            deleteSQL(email)

        return redirect('/showData/')

@app.route('/searchData/', methods=['GET','POST'])
def searchData():
    if request.method=='POST':
        email=request.form['searchEmail']
        data=searchSQL(email)
        return render_template('showdata.html',table=data)
    else:
        return redirect('/showData/')


# host='0.0.0.0' => 내 ip접속 허용
if __name__=='__main__':
    app.run(debug=True)