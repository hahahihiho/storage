from flask import Flask

app=Flask(__name__)

# 텍스트 출력
@app.route('/')
def index():
    return 'Hello world'

# host='0.0.0.0' => 같은 네트워크에서 ip로 접속 허용
# debug=True => 에러를 웹에 출력
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')