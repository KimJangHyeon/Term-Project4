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
    functions.day_reset()
    #functions.initialize_time()
    return render_template('signin.html')

# sign up page 실행
@app.route("/signup", methods=['GET', 'POST'])
def go_signup():
    return render_template('signup.html')

@app.route("/qwe", methods=['GET', 'POST'])
def go_signin():
    print("A")
    return render_template('signin.html')

# sign up 에서 sign up 버튼을 누른 경우
@app.route("/sad", methods=['GET', 'POST'])
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
            name_ = cur.execute(u'SELECT EXISTS (SELECT username FROM userdata WHERE username = ?)', (name,)).fetchone()
            logging.error(id_[0])
            # id 중복
            if (id_[0] != 0):
                logging.error('아이디 중복')
                error = 'Same ID Exists'

            #
            if (name_[0] != 0):
                logging.error('이름 중복')
                error = 'Same name Exists'
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
            error = 'you should input id'
            return render_template('signin.html', error=error)

        login_pw = cur.execute('SELECT password FROM userdata WHERE id = \''+ id + '\'').fetchone()

        if login_pw is None:
            error = 'There is no such id'
            return render_template('signin.html', error=error)

        con.close()
        if(login_pw[0] != pw):
            error = 'check your pw'
            return render_template('signin.html', error=error)
        else:
            now = datetime.datetime.now()
            nowDate = now.strftime('%Y-%m-%d')

            t_year = now.strftime('%Y')
            t_month = now.strftime('%m')
            t_day = now.strftime('%d')

            return render_template('reserve.html', uid=id, date=nowDate, m_year=t_year,
                                   m_month=t_month, m_day=t_day, arr=functions.timetable_into_arr())

# mypage 실행
@app.route("/mypagee", methods=['GET', 'POST'])
def go_mypage():
    logging.error("dsfkljsdklfjlsdkjf")
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    id = request.form['uid']
    user= functions.infrom_by_id(id)
    name = user['name']
    arr = functions.load_reserved_data(name)
    return render_template('mypage.html', uid=id, reserved=arr)

@app.route("/mypage", methods=['GET', 'POST'])
def btn_reserve():
    now = datetime.datetime.now()

    # year = now.strftime('%Y')
    # month = now.strftime('%m')
    # day = now.strftime('%d')
    nowDate = now.strftime('%Y-%m-%d')
    t_year = now.strftime('%Y')
    t_month = now.strftime('%m')
    t_day = now.strftime('%d')


    logging.error('reserve 함수 실행1')
    cycle = functions.day_reset()
    for i in range(0, cycle):
        functions.day_changed()
    start = int(request.form['start'])
    time = int(request.form['time'])
    id = request.form['uid']
    room = request.form['reserve_form_room']
    day = request.form['reserve_form_day']

    logging.error('reserve 함수 실행6')
    logging.error(id)
    user_dic = functions.infrom_by_id(id)
    end = time/30 - 1 + start
    logging.error('reserve 함수 실행7')
    if end>27:
        error='exceed maxium count'
        logging.error(error)
        #return render_template('reserve.html', uid=id, error=error, arr=functions.timetable_into_arr())
        return render_template('reserve.html', error=error, uid=id, date=nowDate, m_year=t_year, m_month=t_month, m_day = t_day, arr = functions.timetable_into_arr())

     #예약가능 횟수:0
    if user_dic['check'] == 0:
        logging.error('오늘은 더 이상 예약 불가')
        error = 'today you can\'t reserve'
        #return render_template('reserve.html', uid=id, error=error, arr=functions.timetable_into_arr())
        return render_template('reserve.html', error=error, uid=id, date=nowDate, m_year=t_year,m_month=t_month, m_day = t_day, arr = functions.timetable_into_arr())
    if request.method == 'POST':
        logging.error('post')

        already_reserved = functions.already_reserved(room, day, start, end+1)
        #이미 예약된 경우
        if already_reserved:
            logging.error('이미 예약된 시간')
            error = 'that time is already reserved'
            #return render_template('reserve.html', uid=id, error=error, arr=functions.timetable_into_arr())
            return render_template('reserve.html', error=error, uid=id, date=nowDate, m_year=t_year,m_month=t_month, m_day = t_day, arr = functions.timetable_into_arr())
        #그 날짜에 이미 예약을 1번한 경우
        if functions.sameday_booked(room, day, user_dic['name']):
            error = 'reserved this day'
            return render_template('reserve.html', uid=id, error=error, arr=functions.timetable_into_arr())
        #예약을 하는 경우
        logging.error("예약하기 들어감")
        for i in range(start, end +1):
            functions.booking_room(room, day, str(i), str(user_dic['name']))
        functions.user_check(id, 0)
        logging.error('마이페이지로!!')
        #return render_template('reserve.html', year=year, month=month, day=day, uid=id, arr=functions.timetable_into_arr())
        return render_template('reserve.html', uid=id, date=nowDate, m_year=t_year,m_month=t_month, m_day = t_day, arr = functions.timetable_into_arr())
@app.route("/delete", methods=['GET', 'POST'])
def btn_delete():
    id = request.form['uid']
    date = request.form['date']
    room = request.form['room']
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    id = request.form['uid']
    user= functions.infrom_by_id(id)
    name = user['name']
    functions.reserve_delete(room, date, user['name'])
    arr = functions.load_reserved_data(name)
    return render_template('mypage.html', uid=id, reserved=arr)

@app.route("/reserved", methods=['GET', 'POST'])
def go_reserved():
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()

    if request.method == 'POST':
        id = request.form['uid']
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')

        t_year = now.strftime('%Y')
        t_month = now.strftime('%m')
        t_day = now.strftime('%d')

        print t_year
        return render_template('reserve.html', uid=id, date=nowDate, m_year=t_year,
                               m_month=t_month, m_day=t_day, arr=functions.timetable_into_arr())

#id로 login 하기
if __name__ == "__main__":
    app.run()