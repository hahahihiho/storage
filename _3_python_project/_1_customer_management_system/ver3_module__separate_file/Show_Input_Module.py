import re
import json

def StartOrder():
    start_explanation="""
================================
I : 고객정보 입력
P/C/N : 이전/현재/다음 고객정보 조회
U : 고객정보 수정
D : 고객정보 삭제
A : db 모두 보여주기
Q : 프로그램 종료
auto : 고객정보 테스트 자동넣기
명령어를 입력해 주세요
=================================="""
    return input(start_explanation+"\n").upper()

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
        re_year=re.compile('^[1][9][0-9][0-9]$|^[2][0][0-9][0-9]$')
        if re_year.match(year):
            return year
        else:
            print("숫자가 이상한걸요? 1900-2099 사이에 태어나신거 아닌가요?")

def inputValue():
    dic={'name':'name','gender':'F/M','email':'email','born-year':"1900"}
    dic['name']=inputName()
    dic['gender']=inputGender()
    dic['email']=inputEmail()
    dic['born-year']=inputBornYear()
    return dic

def autoInsert(table,index):
    if index==-1:
        with open('./test_member.json','r',encoding='utf-8') as f:
            sample = json.load(f)
            for i in sample:
                table.append(i)
                index += 1
            print('테스트 고객정보 삽입완료') 
    else:
        print('아무것도 없을때만 사용 가능합니다')
    return index
