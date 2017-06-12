# -*- coding: utf-8 -*-
from __future__ import with_statement
from flask import Flask, flash, session, request, redirect, url_for, render_template, g
import sqlite3
import datetime
import os
import urllib2
from flask_socketio import SocketIO, send
from contextlib import closing
import functions
import logging
# import templates as view

app = Flask(__name__)


def initialize_db():
    con = sqlite3.connect("sqlite.db")
    cur = con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS Room0_Timetable0(z_090 TEXT,z_093 TEXT,z_100 TEXT,z_103 TEXT,z_110 TEXT,z_113 TEXT,z_120 TEXT,z_123 TEXT,z_130 TEXT,z_133 TEXT,z_140 TEXT,z_143 TEXT,z_150 TEXT,z_153 TEXT,z_160 TEXT,z_163 TEXT,z_170 TEXT,z_173 TEXT,z_180 TEXT, z_183 TEXT,z_190 TEXT,z_193 TEXT,z_200 TEXT,z_203 TEXT,z_210 TEXT,z_213 TEXT);"
    cur.execute(sql)
    sql = "CREATE TABLE IF NOT EXISTS Room0_Timetable1(z_090 TEXT,z_093 TEXT,z_100 TEXT,z_103 TEXT,z_110 TEXT,z_113 TEXT,z_120 TEXT,z_123 TEXT,z_130 TEXT,z_133 TEXT,z_140 TEXT,z_143 TEXT,z_150 TEXT,z_153 TEXT,z_160 TEXT,z_163 TEXT,z_170 TEXT,z_173 TEXT,z_180 TEXT, z_183 TEXT,z_190 TEXT,z_193 TEXT,z_200 TEXT,z_203 TEXT,z_210 TEXT,z_213 TEXT);"
    cur.execute(sql)
    sql = "CREATE TABLE IF NOT EXISTS Room0_Timetable2(z_090 TEXT,z_093 TEXT,z_100 TEXT,z_103 TEXT,z_110 TEXT,z_113 TEXT,z_120 TEXT,z_123 TEXT,z_130 TEXT,z_133 TEXT,z_140 TEXT,z_143 TEXT,z_150 TEXT,z_153 TEXT,z_160 TEXT,z_163 TEXT,z_170 TEXT,z_173 TEXT,z_180 TEXT, z_183 TEXT,z_190 TEXT,z_193 TEXT,z_200 TEXT,z_203 TEXT,z_210 TEXT,z_213 TEXT);"
    cur.execute(sql)
    sql = "CREATE TABLE IF NOT EXISTS Room1_Timetable0(z_090 TEXT,z_093 TEXT,z_100 TEXT,z_103 TEXT,z_110 TEXT,z_113 TEXT,z_120 TEXT,z_123 TEXT,z_130 TEXT,z_133 TEXT,z_140 TEXT,z_143 TEXT,z_150 TEXT,z_153 TEXT,z_160 TEXT,z_163 TEXT,z_170 TEXT,z_173 TEXT,z_180 TEXT, z_183 TEXT,z_190 TEXT,z_193 TEXT,z_200 TEXT,z_203 TEXT,z_210 TEXT,z_213 TEXT);"
    cur.execute(sql)
    sql = "CREATE TABLE IF NOT EXISTS Room1_Timetable1(z_090 TEXT,z_093 TEXT,z_100 TEXT,z_103 TEXT,z_110 TEXT,z_113 TEXT,z_120 TEXT,z_123 TEXT,z_130 TEXT,z_133 TEXT,z_140 TEXT,z_143 TEXT,z_150 TEXT,z_153 TEXT,z_160 TEXT,z_163 TEXT,z_170 TEXT,z_173 TEXT,z_180 TEXT, z_183 TEXT,z_190 TEXT,z_193 TEXT,z_200 TEXT,z_203 TEXT,z_210 TEXT,z_213 TEXT);"
    cur.execute(sql)
    sql = "CREATE TABLE IF NOT EXISTS Room1_Timetable2(z_090 TEXT,z_093 TEXT,z_100 TEXT,z_103 TEXT,z_110 TEXT,z_113 TEXT,z_120 TEXT,z_123 TEXT,z_130 TEXT,z_133 TEXT,z_140 TEXT,z_143 TEXT,z_150 TEXT,z_153 TEXT,z_160 TEXT,z_163 TEXT,z_170 TEXT,z_173 TEXT,z_180 TEXT, z_183 TEXT,z_190 TEXT,z_193 TEXT,z_200 TEXT,z_203 TEXT,z_210 TEXT,z_213 TEXT);"
    cur.execute(sql)
    sql = '''CREATE TABLE IF NOT EXISTS userdata (
    	idn INTEGER PRIMARY KEY AUTOINCREMENT,
        id TEXT NOT NULL,
    	username TEXT NOT NULL,
    	password TEXT NOT NULL
        );'''
    cur.execute(sql)


def render_redirect(template, url, error):
    if error == None:
        return redirect(url_for(url))
    return render_template(template, error=error)

    # sign in page 실행


@app.route("/")
def home():
    functions.timetable_into_arr()
    functions.initialize_db()
    #functions.initialize_time()
    return render_template('signin.html')

# sign up page 실행
@app.route("/signup", methods=['GET', 'POST'])
def go_signup():
    return render_template('signup.html')

@app.route("/", methods=['GET', 'POST'])
def go_signin():
    return render_template('signin.html')

# sign up 에서 sign up 버튼을 누른 경우
@app.route("/", methods=['GET', 'POST'])
def signup():
    logging.error('signup들어옴')
    error = None
    con = sqlite3.connect("sqlite.db")
    cur = con.cursor()
    if request.method == 'POST':
        id = request.form['uid']
        pw = request.form['pw']
        name = request.form['name']

        # 입력을 안한 값이 있는 경우
        if "" in [id, pw, name]:
            error = 'Empty Files'
            return render_template('signup.html', error=error)

        else:
            id_ = cur.execute(u'SELECT EXISTS (SELECT id FROM userdata WHERE id = ?)', (id,)).fetchone()
            logging.error(id_[0])
            # id 중복
            if (id_[0] != 0):
                logging.error('아이디 중복')
                error = 'Same ID Exists'
            # sign up 성공
            if error == None:
                cur.execute('INSERT INTO userdata (id, password, username, check_ ) VALUES (?, ?, ?, ?)', [id, pw, name, 1])
                con.commit()
                con.close()
                return render_template('signin.html')

            logging.error('아이디중복2')

            return render_template('signup.html', error=error)
    else:
        return render_template('signin.html')


# def check_sign(id, pw):
#     con = sqlite3.connect('sqlite.db')
#     cur = con.cursor()
#
#     if request.method == 'POST':
#         id = request.form['uid']
#         pw = request.form['pw']
#         if (id == ''):
#             return 'id를 입력하세요'
#         login_pw = cur.execute('SELECT password FROM userdata WHERE id = \'' + id + '\'').fetchone()
#         con.close()
#         logging.error(login_pw[0])
#         if (login_pw[0] != pw):
#             return 'id와 pw가 일치하지 않습니다'
#         else:
#             return render_template(url_for('signin', ))
@app.route("/signin", methods=['GET', 'POST'])
def signin():
    id=None
    error=None
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()

    if request.method == 'POST':
        id = request.form['uid']
        pw = request.form['pw']
        if(id==''):
            error = 'id를 입력하세요'
            return render_template('signin.html', error=error)
        login_pw = cur.execute('SELECT password FROM userdata WHERE id = \''+ id + '\'').fetchone()
        con.close()
        if(login_pw[0] != pw):
            error='id와 pw가 일치하지 않습니다'
            return render_template('signin.html', error=error)
        else:
            now = datetime.datetime.now()
            nowDate = now.strftime('%Y-%m-%d')
            return render_template('reserve.html', uid = id, date = nowDate, arr=functions.timetable_into_arr())

# mypage 실행
@app.route("/mypagee", methods=['GET', 'POST'])
def go_mypage():
    logging.error("dsfkljsdklfjlsdkjf")
    # 시간표 db에서 같은 아이디의 사람을 {'room_num', 'date', 'start', 'end'} 를 불러오는 arr 생성 및 넘겨주기
    # id에 해당하는 유저의 정보를 user db에서 넘겨주기
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    #name = cur.execute('SELECT name FROM userdata WHERE id = \''+id+'\'').fetchone()
    user= functions.infrom_by_id(id)
    name = user['name']
    
    # arr = [
    #     {'room_num': 0, 'date': '170606', 'start': '08:00', 'end': '09:00'},
    #     {'room_num': 1, 'date': '170606', 'start': '08:00', 'end': '09:00'},
    #     {'room_num': 0, 'date': '170607', 'start': '08:00', 'end': '09:00'},
    #     {'room_num': 1, 'date': '170607', 'start': '08:00', 'end': '09:00'},
    #     {'room_num': 0, 'date': '170608', 'start': '08:00', 'end': '09:00'},
    #     {'room_num': 1, 'date': '170608', 'start': '08:00', 'end': '09:00'}
    # ]
    # reuturn render_template('mypage.html', user = arr, reserved = arr)
    con.close()
    return render_template('mypage.html', userid=id, reserved=arr)

@app.route("/mypage", methods=['GET', 'POST'])
def btn_reserve():
    logging.error('reserve 함수 실행1')
    cycle = functions.day_reset()
    for i in range(0, cycle):
        functions.day_changed()
    start = int(request.form['start'])
    time = int(request.form['time'])
    id = request.form['uid']
    room = request.form['reserve_form_room']
    day = request.form['reserve_form_day']
    print(room)
    print(day)

    logging.error('reserve 함수 실행6')
    logging.error(id)
    end = time/30 - 1 + start
    logging.error('reserve 함수 실행7')
    if end>27:
        error='최대시간을 초과했습니다'
        logging.error(error)
        return render_template('reserve.html', uid=id, error=error)


    user_dic = functions.infrom_by_id(id)
    #예약가능 횟수:0
    if user_dic['check'] == 0:
        logging.error('오늘은 더 이상 예약 불가')
        error = '오늘은 더 이상 예약안됨'
        return render_template('reserve.html', uid=id, error=error)

    if request.method == 'POST':
        logging.error('post')
        room = request.form['room']
        day = request.form['day']
        already_reserved = functions.already_reserved(room, day, start, end+1)
        #이미 예약된 경우
        if already_reserved:
            logging.error('이미 예약된 시간')
            error = '이미 예약이 되어 있음'
            return render_template('reserve.html', uid=id, error=error)
        #예약을 하는 경우
        logging.error("예약하기 들어감")
        for i in range(start, end +1):
            functions.booking_room(room, day, str(i), str(user_dic['name']))
        functions.user_check(id, 0)
        logging.error('마이페이지로!!')
        return render_template('reserve.html', uid=id)

#id로 login 하기
if __name__ == "__main__":
    app.run()