#-*- coding: utf-8 -*-
from __future__ import with_statement
from flask import Flask, flash, session, request, redirect, url_for, render_template
import logging
#import templates as view

app = Flask(__name__)


#class
class User(object):
    def __init__(self, id):
        self.signed_in = False
        self.id = id
        #self.db = connect_db()

    def signin(self, pw):
        error = None
        cur = self.db.cursor()

        id_ = cur.execute(u"SELECT EXISTS ( SELECT id FROM userdata WHERE id = ?)", (self.id,)).fetchone()
        if id_[0] == 0:
            error = "Invalid"
        else:
            pw_ = cur.execute(u"SELECT EXISTS ( SELECT password FROM userdata WHERE id = ?)",
                                (self.id,)).fetchone()
            if pw_[0] == pw:
                error = "Invalid"
            else:
                session['logged_in'] = True
                session['id'] = self.id
                self.signed_in = True
                self.name = self.db.execute(
                    'SELECT username FROM userdata WHERE id=\'' + request.form['id'] + '\'').fetchone()
                flash('Welcom ' + self.name[0])
        return error

    def signup(self, id, name, pw, pw_identify):
        error = None
        cur = self.db.cursor()
        #같은 아이디가 있는 경우
        #db넣고 짜는 걸루...
        #입력값이 없는 경우
        if "" in [id, name, pw, pw_identify]:
            error = "Filed is Empty!"

        #두 pw가 다른 경우
        elif pw != pw_identify:
            error = 'Password does not match'

        #저장
        else:
            id_ = cur.execute(u'SELECT EXISTS (SELECT id FROM userdata WHERE id = ?)', (id,)).fetchone()
            name_ = cur.execute(u'SELECT EXISTS (SELECT username FROM userdata WHERE username = ?)', (name,)).fetchone()

            if id_[0] == 0 and name_[0] == 0:
                flash('Account Created!')
                self.db.execute('INSERT INTO userdata (id, username, password) VALUES (?, ?, ?)',
                                [id, name, pw])
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



@app.route("/")
def signin():
    return render_template('signin.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():

        return render_template('signup.html')
if __name__ == "__main__":
    app.run()
