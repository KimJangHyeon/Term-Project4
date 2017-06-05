from __future__ import with_statement
from flask import Flask, flash, session, request, redirect, url_for
app = Flask(__name__)


#유저 로그인 class
class User(object):
    def __init__(self, email):
        self.signed_in = False
        self.email = email
        self.db = connect_db()

    def signin(self, pwss):
        error = None
        cur = self.db.cursor()

        email_ = cur.execute(u"SELECT EXISTS ( SELECT email FROM userdata WHERE email = ?)", (self.email,)).fetchone()
        if email_[0] == 0:
            error = "Invalid"
        else:
            pwss_ = cur.execute(u"SELECT EXISTS ( SELECT password FROM userdata WHERE email = ?)",
                                (self.email,)).fetchone()
            if pwss_[0] == pwss:
                error = "Invalid"
            else:
                session['logged_in'] = True
                session['email'] = self.email
                self.signed_in = True
                self.name = self.db.execute(
                    'SELECT username FROM userdata WHERE email=\'' + request.form['email'] + '\'').fetchone()
                flash('Welcom ' + self.name[0])
        return error

    def signup(self, email, name, pw, pw_identify):
        error = None
        cur = self.db.cursor()
        #같은 아이디가 있는 경우

        #입력값이 없는 경우
        if "" in [email, name, pw, pw_identify]:
            error = "Filed is Empty!"

        #두 pw가 다른 경우
        elif pw != pw_identify:
            error = 'Password does not match'

        #저장
        else:
            email_ = cur.execute(u'SELECT EXISTS (SELECT email FROM userdata WHERE email = ?)', (email,)).fetchone()
            name_ = cur.execute(u'SELECT EXISTS (SELECT username FROM userdata WHERE username = ?)', (name,)).fetchone()

            if email_[0] == 0 and name_[0] == 0:
                flash('Account Created!')
                self.db.execute('INSERT INTO userdata (email, username, password) VALUES (?, ?, ?)',
                                [email, name, pw])
                self.db.commit()
            else:
                error = "Already Exist"
        return error

    def changeinfo(self):
        error = None
        return redirect(url_for('mypage'))

    def signout(self):
        error = None
        return redirect(url_for('signin'))

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])




@app.route("/")
def hello():
    flash("hello")
    return "hello world"

@app.route("/h/")
def llo():
    return "/h"

if __name__ == "__main__":
    app.run()
