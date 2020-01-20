########################
# 제작: 2019/09/05
# 수정: 2020/01/15
# 제작자: 조현명(https://github.com/hahahihiho)
# title: 고객관리 시스템-3
########################
# ***Brief Description***
# 고객관리 시스템-2을 모듈화
# auto 자동삽입 json 파일로 분할
# 년도예외처리 정규화방식변경
# delete 함수 문제 수정
#
# *** 더 공부해야할것 ***
# 정렬된 표 형태의 print
# main에서 조건할당 vs function에서 모두 처리(parameter와 return)
# call by value vs call by reference 를 문제없이 사용하는법
# Module,function을 나누는 기준
########################


from Show_Input_Module import StartOrder,inputValue,autoInsert
from Move_Print_Module import *

if __name__ == '__main__':

    table=[]
    #-1일때 아무것도 없음
    index=-1

    while True:
        order=StartOrder()

        if order=="I":
            dic=inputValue()
            table.append(dic)
            index=len(table)-1
            printNow(table,index) 
        
        elif order=="P":
            index = prevCustomer(table,index)
        elif order=="C":
            currentCustomer(table,index)
        elif order=="N":
            index = nextCustomer(table,index)

        elif order=="U":
            print("고객정보를 수정합니다")
            dic=inputValue()
            table[index]=dic
            printNow(table,index)

        elif order=="D":
            index = deleteUser(table,index)

        elif order=="A":
            printAll(table)    

        elif order=="AUTO":
            index = autoInsert(table,index)    
            
        elif order=="Q":
            print("콘솔을 종료합니다")
            break
        else:
            print("잘못된 명령")
    