from flask import Flask

# name of app
app=Flask("김모씨")

# 127.0.0.1:5000/user/string
@app.route('/user/<username>')
def user(username):
    return 'user %s' %username

# 127.0.0.1:5000/age/홍길동/33
@app.route('/age/<username>/<int:age>')
def age(username,age):
    return 'username %s age %d' %(username+'1',age+1)

if __name__=='__main__':
    app.run()