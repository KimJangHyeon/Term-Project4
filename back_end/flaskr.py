#-*- coding: utf-8 -*-
from __future__ import with_statement
from flask import Flask, flash, session, request, redirect, url_for, render_template, g, abort
import logging
#import templates as view

app = Flask(__name__)

def render_redirect(template, url, error):
    if error == None:
        return redirect(url_for(url))
    return render_template(template, error=error)

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

    def signup(self, id, name, pw):
        error = None
        #cur = self.db.cursor()
        #같은 아이디가 있는 경우
        #db넣고 짜는 걸루...


        #저장
        #else:
            # id_ = cur.execute(u'SELECT EXISTS (SELECT id FROM userdata WHERE id = ?)', (id,)).fetchone()
            # name_ = cur.execute(u'SELECT EXISTS (SELECT username FROM userdata WHERE username = ?)', (name,)).fetchone()
            #
            # if id_[0] == 0 and name_[0] == 0:
            #     flash('Account Created!')
            #     self.db.execute('INSERT INTO userdata (id, username, password) VALUES (?, ?, ?)',
            #                     [id, name, pw])
            #     self.db.commit()
            # else:
            #    error = "Already Exist"
        return error

    def changeinfo(self):
        error = None
        return redirect(url_for('mypage'))

    def signout(self):
        error = None
        return redirect(url_for('signin'))


#sign in page 실행
@app.route("/")
def signin():
    return render_template('signin.html')



#mypage 실행
@app.route("/user/<userid>")
def go_mypage():
    #시간표 db에서 같은 아이디의 사람을 {'room_num', 'date', 'start', 'end'} 를 불러오는 arr 생성 및 넘겨주기
    #id에 해당하는 유저의 정보를 user db에서 넘겨주기

    arr = [
        {'room_num': 0, 'date': '170606', 'start': '08:00', 'end': '09:00'},
        {'room_num': 1, 'date': '170606', 'start': '08:00', 'end': '09:00'},
        {'room_num': 0, 'date': '170607', 'start': '08:00', 'end': '09:00'},
        {'room_num': 1, 'date': '170607', 'start': '08:00', 'end': '09:00'},
        {'room_num': 0, 'date': '170608', 'start': '08:00', 'end': '09:00'},
        {'room_num': 1, 'date': '170608', 'start': '08:00', 'end': '09:00'},
    ]
    #reuturn render_template('mypage.html', user = arr, reserved = arr)
    return render_template('mypage.html', userid="A", reserved=arr)

#예약 취소
@app.route("")
def lab_cancel():
    #시간표 db에서 같은 id를 가진 경우 전부 null로 초기화
    #return render_template("mypage.html", user = arr, reserved = arr)
    return

#예약
@app.route("")
def lab_book():
    #시간표 db에서 선택한 시간대에 null이 아닌 것이 있는지 확인
    #있다면 에러 출력
    #없으면 null에 id입력
    #return render_template("mypage.html", user = arr, reserved = arr)
    return

#id를 이름으로 (parameter:id, return: name)
def id_into_name(uid):
    #유저 db에서 id를 찾아 이름을 return
    #return name
    return


#sign up page 실행
@app.route("/gosignup", methods=['GET', 'POST'])
def go_signup():
    return render_template('signup.html')

#sign up 에서 sign up 버튼을 누른 경우
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    error = None
    logging.error(request.method)
    if request.method == 'POST':
        id = request.form['uid']
        pw = request.form['pw']
        name = request.form['name']

        #입력을 안한 값이 있는 경우
        if "" in [id, pw, name]:
            error = 'Empty Files'
            return render_template('signup.html', error = error)

        else:
            user = User(id)
            error = user.signup(id, pw, name)

            #sign up 성공
            if error == None:
                return render_template('signin.html')

            #id 중복
            return render_template('signup.html', error = error)
    # else:
    #     return render_template('signin.html')


if __name__ == "__main__":
    app.run()
