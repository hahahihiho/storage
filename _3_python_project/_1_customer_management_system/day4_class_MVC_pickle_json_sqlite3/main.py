########################
# 제작: 2019/09/06
# 수정: 2020/01/16
# 제작자: 조현명(https://github.com/hahahihiho)
# title: 고객관리 시스템-4
########################
# ***Brief Description***
# 고객관리 시스템-3을 class화, MVC(Model View Controller)
# 파일 분리에 집중하기 위해 input조건제거(숫자제외)
# pickle 파일로 저장,로드기능
# json 로 저장,로드기능
# sqlite3 로 insert 로드기능(db동기화x)
#
# *** 더 공부해야할것 ***
# deleteData()변경(index-=1, len(table), ==,!=,>,< 각각의 시간,자원소모정도 )
########################

import Controller_Module as CM

if __name__=='__main__':

    # init
    a=CM.simple_Cclass()
    # 실행
    a.Controller()
