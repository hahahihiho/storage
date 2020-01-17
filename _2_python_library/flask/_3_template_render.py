from flask import Flask,render_template

app=Flask(__name__)

# templates폴더의 html파일을 읽어옴
@app.route('/')
def index():
    return render_template('index.html')

# html에변수전달
@app.route('/user/<username>/<age>')
def user1(username,age):
    return render_template('index.html',username=username,age=age)

# host='0.0.0.0' => 내 ip접속 허용
if __name__=='__main__':
    app.run()