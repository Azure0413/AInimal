from flask import Flask, request, render_template, redirect, url_for, flash,jsonify
app_messenge = Flask(__name__)

@app_messenge.route('/', methods=['GET', 'POST'])
def index():
    #if request.method == 'POST':
        #if login_check(request.form['email'], request.form['password']):
            #flash('Login Success!')
            #return redirect(url_for('hi', email=request.form.get('email')))
    return render_template('index.html')

def login_check(email, password):
    """登入帳號密碼檢核"""
    if email == 'ainimal@ainimal.com' and password == '123123':
        return True
    else:
        return False

@app_messenge.route('/login', methods=['POST'])
def login():
    if request.form['email'] == '' or request.form['password'] == '':
        return jsonify({'msg': "empty"})
    if login_check(request.form['email'], request.form['password']):
        return jsonify({'msg': "success"})
    else:
        return jsonify({'msg': "fail"})
            #flash('Login Success!')
            #return redirect(url_for('hi', email=request.form.get('email'))) 
@app_messenge.route('/hi/<email>')
def hi(email):
    return render_template('hi.html', email=email)

if __name__ == '__main__':
    app_messenge.debug = True
    app_messenge.secret_key = "Your Key"
    app_messenge.run()