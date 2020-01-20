import pickle,os
import sqlite3
import json


class simple_Mclass():
    table=[]

    def __init__(self):
        self.index=-1

    def getTableI(self,index):
        return simple_Mclass.table[index]

    def connectDB(self):
        conn=sqlite3.connect('./db/table.sql')
        c=conn.cursor()
        return c,conn

    def closeDB(self,conn):
        conn.commit()
        conn.close()

    # sqlite3 db이용
    def LoadData(self):
        c,conn=self.connectDB()

        c.execute('select * from customerList')
        cList=c.fetchall()

        for i in cList:
            dic={}
            dic['name']=i[0]
            dic['gender']=i[1]
            dic['email']=i[2]
            dic['born-year']=i[3]
            simple_Mclass.table.append(dic)
        
        self.index=len(simple_Mclass.table)-1

        self.closeDB(conn)

    def SaveData(self):
        conn=sqlite3.connect('./db/table.sql')
        c=conn.cursor()

        # 테이블 생성
        c.execute('''
            create table if not exists customerList(
                name text,
                gender text,
                email text,
                byear number
            )
        ''')

        # insert whole values into table
        sql='''insert into customerList(name,gender,email,byear)
                values(?,?,?,?)'''

        for data in simple_Mclass.table:
            insert=[data['name'],data['gender'],data['email'],data['born-year']]
            c.execute(sql,insert)
        conn.commit()
        conn.close()

    def insertDatas(self,name,gender,email,byear):
        
        dic={'name':name,'gender':gender,'email':email,'born-year':byear}
        print(dic)
        simple_Mclass.table.append(dic)
        self.index=len(simple_Mclass.table)-1

    def updateDatas(self,name,gender,email,byear):
        dic={'name':name,'gender':gender,'email':email,'born-year':byear}
        simple_Mclass.table[self.index]=dic

    def deleteData(self):
        if len(simple_Mclass.table)!=0:
            del simple_Mclass.table[self.index]
        if len(simple_Mclass.table) == self.index:
            self.index -= 1
            return True
        else:
            return False
    
    # view에 있는게 구조는 좋으나 여기있는게 동작이 편함 
    def printNow(self):
        print(simple_Mclass.table[self.index])
    def printAll(self):
        for i in simple_Mclass.table:
            print(i)

    # controller로 옮김
    # def prevCustomer(self):
    #     if self.index>0: 
    #         self.index -=1
    #         print("이전 고객 정보입니다")
    #         print(simple_Mclass.table[self.index])
    #     else:
    #         print("이전고객정보가 없습니다")

    # def currentCustomer(self):
    #     if self.index!=-1:
    #         print("현재 고객정보입니다")
    #         print(simple_Mclass.table[self.index])  
    #     else:
    #         print("고객정보가 없습니다")

    # def nextCustomer(self):
    #         if self.index<len(simple_Mclass.table)-1:
    #             self.index += 1
    #             print("다음 고객정보입니다")
    #             print(simple_Mclass.table[self.index])
    #         else:
    #             print("마지막 고객정보입니다")



    