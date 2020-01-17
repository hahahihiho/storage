def printNow(table,index):
    dic=table[index]
    print("#", "이  름", "성별","이메일", "출생년도")
    print(index,dic['name'],dic['gender'],'  ',dic['email'],dic['born-year'])

def printAll(table):
    print("{0:=^40}".format("모두보기"),"\n")
    print("#", "이  름", "성별","이메일", "출생년도")
    for n, i in enumerate(table):
        print(n,i['name'],i['gender'],'  ',i['email'],i['born-year'])

def prevCustomer(table,index):
    if index>0: 
        index=index-1
        print("이전 고객 정보입니다")
        printNow(table,index)
    else:
        print("이전고객정보가 없습니다")
    return index

def currentCustomer(table,index):
    if index!=-1:
        print("현재 고객정보입니다")
        printNow(table,index)  
    else:
        print("고객정보가 없습니다")

def nextCustomer(table,index):
    if index<len(table)-1:
        index=index+1
        print("다음 고객정보입니다")
        printNow(table,index) 
    else:
        print("마지막 고객정보입니다")
    return index

def deleteUser(table,index):
    if index!=-1:
        del table[index]
        if index == 0 and len(table)!=0:
            index = 0
        else:
            index=index-1
        print("현재 고객정보를 삭제하였습니다")
    else:
        print("고객정보가 없습니다")
    return index
