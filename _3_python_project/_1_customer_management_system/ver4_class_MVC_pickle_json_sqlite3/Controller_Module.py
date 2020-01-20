import View_Module as VM
import Model_Module as MM

class simple_Cclass():

    def __init__(self):
        self.v = VM.simple_Vclass()
        self.m = MM.simple_Mclass()

    def Controller(self):
        # 객체생성
        v = self.v
        m = self.m

        while True:
            
            # 명령어 입력, 명령 할당
            order=v.StartOrder()
            
            if order=="I":
                # 값 입력
                name=v.inputName()
                gender=v.inputGender()
                email=v.inputEmail()
                byear=v.inputBornYear()
                # m에 값 저장
                m.insertDatas(name,gender,email,byear)

            elif order=="P":
                m.prevCustomer()       
            elif order=="C":
                m.currentCustomer()
            elif order=="N":
                m.nextCustomer()

            elif order=="U":
                if m.index!=-1:
                    # 값 입력
                    name=v.inputName()
                    gender=v.inputGender()
                    email=v.inputEmail()
                    byear=v.inputBornYear()
                    # 값 수정
                    m.updateDatas(name,gender,email,byear)
                else:
                    print('업데이트할 고객이 없습니다')
                
            elif order=="D":
                m.deleteData()

            elif order=="A":
                m.printAll()
            
            elif order=="L":
                if m.index == -1:
                    while True: 
                        load_method = input('1:sql 2:pickle 3:json :')
                        if load_method == '1':
                            m.LoadDataSQL()
                            break
                        elif load_method == '2':
                            m.LoadData()
                            break
                        elif load_method == '3':
                            m.LoadDataJSON()
                            break
                        else:
                            print('select 1, 2, or 3')
                    print('로드완료')
                else:
                    print('데이터가 없을때만 load가 가능합니다')  

            elif order=="S":
                while True: 
                    save_method = input('1:sql 2:pickle 3:json :')
                    if save_method == '1':
                        m.SaveDataSQL()
                        break
                    elif save_method == '2':
                        m.SaveData()
                        break
                    elif save_method == '3':
                        m.SaveDataJSON()
                        break
                    else:
                        print('select 1, 2, or 3')
                print('저장완료')

            elif order=="Q":
                print("콘솔을 종료합니다")
                break
            else:
                print("잘못된 명령")
