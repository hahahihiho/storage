

    def __ini
        m,v=self.createObj()
    

    @app.route('/i/')
    def Control_I(self):
        
        # name,gender,email,bornYear값 입력받음
        n,g,e,b=v.inputall()
        # m에 값 저장
        m.insertDatas(n,g,e,b)
        return

    def Control_U(self,m,v):   
        # 값 입력
        name=v.inputName()
        gender=v.inputGender()
        email=v.inputEmail()
        byear=v.inputBornYear()
        # 값 수정
        m.updateDatas(name,gender,email,byear)

    def Control_D(self,m):
        isSuccess=m.deleteData()
        if isSuccess==True:
            # v.delsuccess()
            print("삭제 성공")
        else:
            # v.delfailure()
            print("삭제할 정보가 없습니다")

    """
    컨트롤러
    """
    def Controller(self):
        
        self.createObj()
        
        while True:
            
            # 명령어 입력, 명령 할당
            order=v.StartOrder()
            
            if order=="I":
                self.Control_I(m,v)

            elif order=="P":
                self.Control_P(m)
                    
            elif order=="C":
                self.Control_C(m)

            elif order=="N":
                self.Control_N(m)

            elif order=="U":
                self.Control_U(m,v)
                
            elif order=="D":
                self.Control_D(m)

            elif order=="A":
                # t=customer_M.simple_Mclass.table
                # v.printAll(t)
                m.printAll()
            
            elif order=="L":
                m.LoadData()

            elif order=="AUTO":
                pass                   

            elif order=="S":
                m.SaveData()

            elif order=="Q":
                print("콘솔을 종료합니다")
                break
            else:
                print("잘못된 명령")
