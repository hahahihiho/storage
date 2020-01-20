from flask import Flask,render_template,request,redirect

app=Flask(__name__)

# 입력페이지
@app.route('/')
def forminput():
    return render_template('forminput.html')

# 값받음
@app.route('/method',methods=['GET','POST'])
def method():
    if request.method=='POST':
        # form : form에서 post 한 값을 가져옴 ('username'을 못찾으면 404error)
        # form.get : post 한 값을 가져옴 (못찾으면 None)
        # args : 주소값에 친 값(get)을 가져옴 
        # values : get, post 어떤거든 가져옴 ()

        id=request.form['username']
        id1 = request.form.get('username')
        pw = request.values.get('password')

        return "id : %s = %s \n password : %s" %(id,id1,pw)
    else :
        # http://127.0.0.1:5000/method?pw=1&id=2
        return "{} {} {}".format(request.args.get('pw'),request.form.get('a'),request.values.get("id"))

if __name__=='__main__':
    app.run(debug=True)