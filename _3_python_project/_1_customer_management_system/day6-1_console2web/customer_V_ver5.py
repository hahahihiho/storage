class simple_Vclass():
        
    def StartOrder(self):
        start_explanation="""
        L : 이전 db load
        S : 현재정보 db에 save
        I : 고객정보 입력
        P/C/N : 이전/현재/다음 고객정보 조회
        U : 고객정보 수정
        D : 고객정보 삭제
        A : db 모두 보여주기
        Q : 프로그램 종료
        auto : 고객정보 테스트 자동넣기(아직구현중)
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
        year=input("태어난 년도를 입력해 주세요 :")
        return year

    def inputall(self):
        n=self.inputName()
        g=self.inputGender()
        e=self.inputEmail()
        b=self.inputBornYear()
        return n,g,e,b










