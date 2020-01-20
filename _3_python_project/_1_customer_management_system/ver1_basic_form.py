########################
# 제작: 2019/09/03
# 수정: 2020/01/14
# 제작자: 조현명(https://github.com/hahahihiho)
# title: 고객관리 시스템-1
########################
# ***Brief Description***
# 고객정보 관리
# 정규표현식으로 예외처리
# update는 예외처리x(추후 def로 구현예정)
########################

import re
start_explanation="="*40+"""
I : 고객정보 입력
P/C/N : 이전/현재/다음 고객정보 조회
U : 고객정보 수정
D : 고객정보 삭제
A : db 모두 보여주기
Q : 프로그램 종료
auto : 고객정보 테스트 자동넣기(Coming soon)
명령어를 입력해 주세요
"""+"="*40

table=[]
#-1일때 아무것도 없음
index=-1

# 동작
while True:
    order=input(start_explanation+"\n").upper()
    if order=="I":
        dic={'name':'name','gender':'F/M','email':'email','born-year':"1900"}
        while True:
            name=input("이름을 입력해 주세요 :")
            re_kor=re.compile('[ㄱ-ㅣ가-힣]')
            if re_kor.match(name):
                dic['name']=name
                break
            else :
                print("한국이름만 받습니다")
        while True:
            gender=input("성별을 입력해 주세요(F/M) :")
            re_gen=re.compile('[FM]')
            if re_gen.match(gender):
                dic['gender']=gender
                break
            else:
                print("F 나 M만 받습니다")

        while True:
            email=input("이메일을 입력해 주세요 :")
            re_email=re.compile(r'\w+[@]\w+[.]\w')
            print(email)
            if re_email.match(email):
                dic['email']=email
                break
            else:
                print("email 형식 : aaa@aaa.aaa")
        while True:
            year=input("태어난 년도를 입력해 주세요 :")
            if (year.isdigit()) and (int(year)>=1900) and (int(year)<=2100):
               dic['born-year']=year
               break
            else:
                print("숫자가 이상한걸요?(1900-2100사이로 입력하세요)")
        table.append(dic)
        index=len(table)-1
        print("#\t", "이름\t\t", "성별\t","이메일\t\t", "출생년도")
        print(index,'\t',dic['name'],'\t\t',dic['gender'],'\t',dic['email'],'\t\t',dic['born-year'])
    elif order=="P":
        if index>0: 
            index=index-1
            print("이전 고객 정보입니다")
            dic=table[index]
            print("#\t", "이름\t\t", "성별\t","이메일\t\t", "출생년도")
            print(index,'\t',dic['name'],'\t\t',dic['gender'],'\t',dic['email'],'\t\t',dic['born-year'])
        else:
            print("이전고객정보가 없습니다")

    elif order=="C":
        if index!=-1:
            print("현재 고객정보입니다")
            
            dic=table[index]
            print("#\t", "이름\t\t", "성별\t","이메일\t\t", "출생년도")
            print(index,'\t',dic['name'],'\t\t',dic['gender'],'\t',dic['email'],'\t\t',dic['born-year'])
        else:
            print("고객정보가 없습니다")
    elif order=="N":
        if index<len(table)-1:
            index=index+1
            print("다음 고객정보입니다")
            dic=table[index]
            print("#\t", "이름\t\t", "성별\t","이메일\t\t", "출생년도")
            print(index,'\t',dic['name'],'\t\t',dic['gender'],'\t',dic['email'],'\t\t',dic['born-year'])
        else:
            print("마지막 고객정보입니다")
    elif order=="U":
        if index!=-1:
            print("고객정보를 수정합니다")
            dic=table[index]
            dic['name']=str(input("이름을 입력해 주세요 :"))
            dic['gender']=str(input("성별을 입력해 주세요(F/M) :"))
            dic['email']=str(input("이메일을 입력해 주세요 :"))
            dic['born-year']=(input("태어난 년도를 입력해 주세요 :"))
            table[index]=dic
            dic=table[index]
            print("#\t", "이름\t\t", "성별\t","이메일\t\t", "출생년도")
            print(index,'\t',dic['name'],'\t\t',dic['gender'],'\t',dic['email'],'\t\t',dic['born-year'])
        else:
            print("고객정보가 없습니다")
    elif order=="D":
        if index!=-1:
            del table[index]
            index=index-1
            print("현재 고객정보를 삭제하였습니다")
        else:
            print("고객정보가 없습니다")

    elif order=="A":
        print("{0:=^40}".format("모두보기"),"\n")
        print("#\t", "이름\t\t", "성별\t","이메일\t\t", "출생년도")
        for n, i in enumerate(table):
            print(n,'\t',i['name'],'\t\t',i['gender'],'\t',i['email'],'\t\t',i['born-year'])
        
    elif order=="Q":
        print("콘솔을 종료합니다")
        break
    else:
        print("잘못된 명령")
    