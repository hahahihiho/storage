import pickle,os,sqlite3,json


class simple_Mclass():

    def __init__(self):
        self.table=[]
        self.index=-1
        
    def insertDatas(self,name,gender,email,byear):
        dic={'name':name,'gender':gender,'email':email,'born-year':byear}
        print(dic)
        self.table.append(dic)
        self.index += 1

    def updateDatas(self,name,gender,email,byear):
        dic={'name':name,'gender':gender,'email':email,'born-year':byear}
        self.table[self.index]=dic

    def deleteData(self):
        if len(self.table)!=0:
            del self.table[self.index]
            print("현재 고객정보를 삭제하였습니다")
            if len(self.table) == self.index:
                self.index -= 1
        else:
            print("삭제할 고객정보가 없습니다.")   

    def printAll(self):
        for i,v in enumerate(self.table):
            print(i,v)

    def prevCustomer(self):
        if self.index>0: 
            self.index -=1
            print("이전 고객 정보입니다")
            print(self.table[self.index])
        else:
            print("이전고객정보가 없습니다")

    def currentCustomer(self):
        if self.index!=-1:
            print("현재 고객정보입니다")
            print(self.table[self.index])  
        else:
            print("고객정보가 없습니다")

    def nextCustomer(self):
            if self.index<len(self.table)-1:
                self.index += 1
                print("다음 고객정보입니다")
                print(self.table[self.index])
            else:
                print("마지막 고객정보입니다")

    def LoadData(self):
        if os.path.exists('./db/table.pickle'):
            with open('./db/table.pickle','rb') as f:
                self.table=pickle.load(f)
                self.index=len(self.table)-1
        
    def SaveData(self):
        with open('./db/table.pickle','wb') as f:
            pickle.dump(self.table,f,pickle.HIGHEST_PROTOCOL)

    def LoadDataJSON(self):
        if os.path.exists('./db/table.json'):
            with open('./db/table.json','r',encoding='utf-8') as f:
                self.table=json.load(f)
                self.index=len(self.table)-1

    def SaveDataJSON(self):
        with open('./db/table.json','w') as f:
            json.dump(self.table, f, indent=4)


    # sqlite3 db이용
    def connectSQL(self):
        conn=sqlite3.connect('./db/table.sql')
        c=conn.cursor()
        return conn,c
    
    def createSqlTable(self,c):
        c.execute('''
            create table if not exists customerList(
                name text,
                gender text,
                email text,
                byear integer
            )
        ''')

    def LoadDataSQL(self):
        conn,c = self.connectSQL()
        
        self.createSqlTable(c)

        c.execute('select * from customerList')
        cList=c.fetchall()
        for i in cList:
            dic={}
            dic['name']=i[0]
            dic['gender']=i[1]
            dic['email']=i[2]
            dic['born-year']=i[3]
            self.table.append(dic)
        
        self.index=len(self.table)-1

        conn.close()

    def SaveDataSQL(self):
        conn,c = self.connectSQL()

        # drop table
        c.execute('DROP TABLE customerList')
        # 테이블 생성
        self.createSqlTable(c)

        # insert whole values into table
        sql='''insert into customerList(name,gender,email,byear)
                values(?,?,?,?)'''

        for data in self.table:
            insert=[data['name'],data['gender'],data['email'],data['born-year']]
            c.execute(sql,insert)
        conn.commit()
        conn.close()





    