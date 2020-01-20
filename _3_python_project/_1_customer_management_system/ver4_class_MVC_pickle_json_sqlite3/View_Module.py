import re

class simple_Vclass():
        
    def StartOrder(self):
        start_explanation="""
        I : 고객정보 입력
        P/C/N : 이전/현재/다음 고객정보 조회
        U : 고객정보 수정
        D : 고객정보 삭제
        A : 모두 보여주기
        L : db 불러오기
        S : db 저장하기
        Q : 종료
        명령어를 입력해 주세요
        """
        return input(start_explanation+"\n").upper()

    def inputName(self):
        name=input("이름을 입력해 주세요 :")
        return name

    def inputGender(self):
        gender=input("성별을 입력해 주세요(F/M) :")
        return gender
        
    def inputEmail(self):
        email = input("이메일을 입력해 주세요 :")
        return email

    def inputBornYear(self):
        while True:
            year=input("태어난 년도를 입력해 주세요 :")
            re_year=re.compile('^[1][9][0-9][0-9]$|^[2][0][0-9][0-9]$')
            if re_year.match(year):
                return int(year)
            else:
                print("숫자가 이상한걸요? 1900-2099 사이에 태어나신거 아닌가요?")








