from application import *
from flask import session,render_template
from flask.globals import request
import pickle,os

app.secret_key='secret'
t=0
u=0
lid=[]
name=[]
lid1=[]
name1=[]
@app.route('/')
def mainp():
    return render_template('mainpage.htm')

@app.route('/cliesign',methods=['POST','GET'])
def cliesign():
    if (request.method == 'POST'):

        email = request.form['user']
        n1 = request.form['n1']
        password = request.form['psw']
        try:
            u1=auth.create_user_with_email_and_password(email, password)
            l1=u1.get('localId')
            lid.append(l1)
            with open(os.path.abspath('file.pkl'), 'wb') as file:
                pickle.dump(lid, file)
            name.append(n1)
            with open(os.path.abspath('file1.pkl'), 'wb') as file1:
                pickle.dump(name, file1)
            flash('User Created!','info')
            return render_template('client_login.htm')
        except:
            flash('User already exists','error')
            return redirect(url_for('cliesign'))
    return render_template('client_login.htm')

@app.route('/custsign',methods=['POST','GET'])
def custsign():
    if (request.method == 'POST'):
        email = request.form['user']
        n1 = request.form['n1']
        password = request.form['psw']
        try:
            el=auth.create_user_with_email_and_password(email, password)
            l1=el.get('localId')
            lid1.append(l1)
            with open(os.path.abspath('file4.pkl'), 'wb') as file4:
                pickle.dump(lid1, file4)
            name1.append(n1)
            with open(os.path.abspath('file5.pkl'), 'wb') as file5:
                pickle.dump(name1, file5)
            flash('User Created!','info')
            return redirect(url_for('custsign'))
        except:
            flash('User already exists','error')
            return redirect(url_for('custsign'))
    return render_template('customer_login.htm')

@app.route('/clielog',methods=['POST','GET'])
def clielog():
    if request.method=='POST':
        email = request.form.get('username')
        password=request.form.get('psw')
        try:
            u2 = auth.sign_in_with_email_and_password(email, password)
            l3=u2.get('localId')
            with open(os.path.abspath('file.pkl'), 'rb') as file:
                lid = pickle.load(file)
            with open(os.path.abspath('file1.pkl'), 'rb') as file1:
                name = pickle.load(file1)
            i=lid.index(l3)
            t=1
            u=1
        except:
            flash('Incorrect credentials','error')
            return redirect(url_for('clielog'))
        if((t==1) and (u!=0)):
            return render_template('in.htm',e=name[i])
    return render_template('client_login.htm')

@app.route('/custlog',methods=['POST','GET'])
def custlog():
    if request.method=='POST':
        email = request.form.get('username')
        password=request.form.get('psw')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            l3=user.get('localId')
            with open(os.path.abspath('file4.pkl'), 'rb') as file4:
                lid1 = pickle.load(file4)
            with open(os.path.abspath('file5.pkl'), 'rb') as file5:
                name1 = pickle.load(file5)
            i=lid1.index(l3)
            t=1
            u=1
        except:
            flash('Incorrect credentials','error')
            return redirect(url_for('custlog'))
        if((t==1) and (u!=0)):
            return render_template('in.htm',e=name1[i])
    return render_template('customer_login.htm')

@app.route('/logout',methods=['POST','GET'])
def logout():
        auth.current_user = None
        u=0
        t=0
        return redirect('/')

@app.route('/forgotps', methods=['GET', 'POST'])
def forgotps():
    if (request.method == 'POST'):
        email = request.form['username']
        try:
            auth.send_password_reset_email(email)
            flash('Reset link sent to email ID','info')
            return render_template('forgotps.html')
        except:
            flash('User does not exist','error')
            return render_template('forgotps.html')
    return render_template('forgotps.html')

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache,no-store, must-revalidate"
    return response