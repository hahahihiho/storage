########################
# 제작: 2019/09/04
# 수정: 2020/01/14
# 제작자: 조현명(https://github.com/hahahihiho)
# title: 고객관리 시스템-2
########################
# ***Brief Description***
# 고객관리 시스템-1 함수화
# email 예외처리 제거
# 년도예외처리 정규화방식 이용(년도 범위변경)
# global 사용(추후 parameter와 return의 사용으로 객체지향)
########################

import re

def StartOrder():
    start_explanation='''
===================================
I : 고객정보 입력
P/C/N : 이전/현재/다음 고객정보 조회
U : 고객정보 수정
D : 고객정보 삭제
A : db 모두 보여주기
Q : 프로그램 종료
AUTO : 고객정보 테스트 자동넣기
명령어를 입력해 주세요
===================================
'''
    return input(start_explanation).upper()

def inputName():
    while True:
        name=input("이름을 입력해 주세요 :")
        re_kor=re.compile('[ㄱ-ㅣ가-힣]')
        if re_kor.match(name):
            return name
        else :
            print("한국이름만 받습니다")

def inputGender():
    while True:
        gender=input("성별을 입력해 주세요(F/M) :")
        re_gen=re.compile('[FM]')
        if re_gen.match(gender):
            return gender
        else:
            print("F 나 M만 받습니다")

def inputEmail():
    while True:
        email = input("이메일을 입력해 주세요 :")
        if email:
            return email

def inputBornYear():
    while True:
        year=input("태어난 년도를 입력해 주세요 :")
        re_year=re.compile('^[12][0-9][0-9][0-9]$')
        if re_year.match(year):
            return year
        else:
            print("숫자가 이상한걸요? 1000-2999년도 사이에 태어나신거 아닌가요?")

def inputValue():
    dic={'name':'name','gender':'F/M','email':'email','born-year':"1900"}
    dic['name']=inputName()
    dic['gender']=inputGender()
    dic['email']=inputEmail()
    dic['born-year']=inputBornYear()
    return dic

def printNow(index):
    global table
    dic=table[index]
    print("#\t", "이  름\t\t", "성별\t","이메일\t\t", "출생년도")
    print(str(index)+'\t',dic['name']+'\t\t',dic['gender']+'\t','{0: <20}'.format(i['email']),str(dic['born-year']))

def printAll():
    global table
    print("{0:=^40}".format("모두보기"),"\n")
    print('{0: <7}'.format("#"),
          '{0: <10}'.format("이름"),
          '{0: <7}'.format("성별"),
          '{0: <14}'.format("이메일"), "출생년도")
    for n, i in enumerate(table):
        print('{0: <7}'.format(n),
              '{0: <10}'.format(i['name']),
              '{0: <7}'.format(i['gender']),
              '{0: <20}'.format(i['email']),i['born-year'])


def prevCustomer():
    global index
    if index>0: 
        index=index-1
        print("이전 고객 정보입니다")
        printNow(index) 
    else:
        print("이전고객정보가 없습니다")

def currentCustomer():
    global index
    if index!=-1:
        print("현재 고객정보입니다")
        printNow(index)  
    else:
        print("고객정보가 없습니다")

def nextCustomer():
    global index
    if index<len(table)-1:
        index=index+1
        print("다음 고객정보입니다")
        printNow(index) 
    else:
        print("마지막 고객정보입니다")

def deleteUser():
    global index
    if index!=-1:
        del table[index]
        index=index-1
        print("현재 고객정보를 삭제하였습니다")
    else:
        print("고객정보가 없습니다")

if __name__ == '__main__':
    # 모든 고객 정보 담을 리스트 선언
    # 테스트용 데이터
    example_members = [
        {
            'name': '강화수',
            'gender': 'F',
            'email': 'a@a.com',
            'born-year': '2000'},
        {
            'name': '홍길동',
            'gender': 'M',
            'email': 'd@d.com',
            'born-year': '1900'}
        ]

    table=[]
    #-1일때 아무것도 없음
    index=-1

    while True:
        order=StartOrder()

        if order=="I":
            dic=inputValue()
            table.append(dic)
            index=len(table)-1
            printNow(index) 
        
        elif order=="P":
            prevCustomer()
        elif order=="C":
            currentCustomer()
        elif order=="N":
            nextCustomer()

        elif order=="U":
            if index!=-1:
                print("고객정보를 수정합니다")
                dic=inputValue()
                table[index]=dic
                printNow(index)
            else:
                print("고객정보가 없습니다")

        elif order=="D":
            deleteUser()

        elif order=="A":
            printAll()      

        elif order=="AUTO":
            if index==-1:
                for i in example_members:
                    table.append(i)
                    index += 1
                print('테스트 고객정보 삽입완료') 
            else:
                print('아무것도 없을때만 사용 가능합니다')
            
        elif order=="Q":
            print("콘솔을 종료합니다")
            break
        else:
            print("잘못된 명령")
    