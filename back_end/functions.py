# -*- coding: utf-8 -*-
import sqlite3
import datetime
import logging
def initialize_db():
    con = sqlite3.connect("sqlite.db")
    cur = con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS Room0_timetable0(time TEXT, name TEXT);"
    cur.execute(sql)
    sql = "CREATE TABLE IF NOT EXISTS Room0_timetable1(time TEXT, name TEXT);"
    cur.execute(sql)
    sql = "CREATE TABLE IF NOT EXISTS Room0_timetable2(time TEXT, name TEXT);"
    cur.execute(sql)
    sql = "CREATE TABLE IF NOT EXISTS Room1_timetable0(time TEXT, name TEXT);"
    cur.execute(sql)
    sql = "CREATE TABLE IF NOT EXISTS Room1_timetable1(time TEXT, name TEXT);"
    cur.execute(sql)
    sql = "CREATE TABLE IF NOT EXISTS Room1_timetable2(time TEXT, name TEXT);"
    cur.execute(sql)
    sql = '''CREATE TABLE IF NOT EXISTS userdata (
    	idn INTEGER PRIMARY KEY AUTOINCREMENT,
        id TEXT NOT NULL,
    	username TEXT NOT NULL,
    	password TEXT NOT NULL, 
    	check_ INTEGER
        );'''
    cur.execute(sql)
    sql = "CREATE TABLE IF NOT EXISTS day(key_ INTEGER, today TEXT);"
    cur.execute(sql)
    con.commit()
    con.close()
    return
def initialize_time():
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    for i in range(0, 28):
        cur.execute("INSERT INTO Room0_timetable0(time, name) VALUES (?, ?)", ['t_' + str(i), 'NULL'])
        cur.execute("INSERT INTO Room0_timetable1(time, name) VALUES (?, ?)", ['t_' + str(i), 'NULL'])
        cur.execute("INSERT INTO Room0_timetable2(time, name) VALUES (?, ?)", ['t_' + str(i), 'NULL'])
        cur.execute("INSERT INTO Room1_timetable0(time, name) VALUES (?, ?)", ['t_' + str(i), 'NULL'])
        cur.execute("INSERT INTO Room1_timetable1(time, name) VALUES (?, ?)", ['t_' + str(i), 'NULL'])
        cur.execute("INSERT INTO Room1_timetable2(time, name) VALUES (?, ?)", ['t_' + str(i), 'NULL'])
    con.commit()
    con.close()
    return

#id를 받고 그 유저의 inform을 딕셔너리로 출력
def infrom_by_id(id):
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    name_ = cur.execute('select username from userdata where id = \''+id+'\'').fetchone()
    pw_ = cur.execute('select password from userdata where id = \''+id +'\'').fetchone()
    check_ = cur.execute('SELECT check_ from userdata where id = \''+id+'\'').fetchone()
    con.close()
    return {'name':name_[0], 'id':id, 'pw':pw_[0], 'check':check_[0]}

def user_check(id, check):
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    cur.execute('UPDATE userdata SET check_='+str(check)+' WHERE id = \'' + id + '\'')
    con.close()
    return

def booking_room(room, date, time, name):
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    cur.execute('UPDATE Room' + room + '_timetable' + date + 'SET name = \''+name+'\' WHERE time=\'t_'+str(time)+'\'')
    con.close()
    return

def already_reserved(room, date, start_time, end_time):
    already = 0
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    for i in range(start_time, end_time+1):
        if cur.execute('SELECT name FROM Room'+room+'_timetable'+date+' where time = \'t_'+str(i)+'\'').fetchone()[0] != 'NULL':
            already = 1
            break
    con.close()
    return already

#날짜가 바뀌면 room과 유저 update
def day_changed():
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    #유저 check 1로 전환
    cur.execute('UPDATE userdata SET check_ = 1 WHERE idn >= 1')

    #timetable 전환
    for i in range(0,28):
        name_0 = cur.execute('SELECT name from Room0_timetable1 WHERE time=\'t_'+str(i)+'\'').fetchone()
        cur.execute('UPDATE Room0_timetable0 SET name=\'' + name_0[0] + '\' WHERE time = \'t_'+str(i)+'\'')

        name_1 = cur.execute('SELECT name from Room0_timetable2 WHERE time=\'t_' + str(i) + '\'').fetchone()
        cur.execute('UPDATE Room0_timetable1 SET name=\'' + name_1[0] + '\' WHERE time = \'t_' + str(i) + '\'')

        cur.execute('UPDATE Room0_timetable2 SET name=\'NULL\' WHERE time = \'t_' + str(i) + '\'')

        name_2 = cur.execute('SELECT name from Room1_timetable1 WHERE time=\'t_'+str(i)+'\'').fetchone()
        cur.execute('UPDATE Room1_timetable0 SET name=\'' + name_2[0] + '\' WHERE time = \'t_'+str(i)+'\'')

        name_3 = cur.execute('SELECT name from Room1_timetable2 WHERE time=\'t_' + str(i) + '\'').fetchone()
        cur.execute('UPDATE Room1_timetable1 SET name=\'' + name_3[0] + '\' WHERE time = \'t_' + str(i) + '\'')

        cur.execute('UPDATE Room1_timetable2 SET name=\'NULL\' WHERE time = \'t_' + str(i) + '\'')
    con.commit()
    con.close()
    return

def month(mon):
    if mon=='01':
        return 31
    if mon == '02':
        return 28
    if mon == '03':
        return 31
    if mon == '04':
        return 30
    if mon == '05':
        return 31
    if mon == '06':
        return 30
    if mon == '07':
        return 31
    if mon == '08':
        return 31
    if mon == '09':
        return 30
    if mon == '10':
        return 31
    if mon == '11':
        return 30
    if mon == '12':
        return 31


def priority(arr):
    return int(arr[0])*365 + month(arr[1]) + int(arr[2])

def day_reset():
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    nowYear = now.strftime('%Y')
    nowMonth = now.strftime('%m')
    nowDay = now.strftime('%d')

    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    today_db = cur.execute('SELECT today from day').fetchone()
    arr = today_db[0].split('-', 2)
    if nowDate == today_db[0]:
        con.close()
        return 0
    db_prior = priority(arr)
    to_prior = priority(nowDate.split('-', 2))
    cur.execute('UPDATE day SET today=\''+nowDate+'\' WHERE key_=1')
    con.commit()
    con.close()
    if to_prior-db_prior >= 3:
        return 3
    elif to_prior-db_prior == 2:
        return 2
    else:
        return 1

def timetable_into_arr():
    con =sqlite3.connect('sqlite.db')
    cur =con.cursor()
    #arr00 = cur.execute('SELECT * FROM Room0_timetable0').fetchall()
    arr00 = []
    arr01 = []
    arr02 = []
    arr10 = []
    arr11 = []
    arr12 = []

    rows = cur.execute('SELECT * FROM Room0_timetable0').fetchall()
    for row in rows:
        if row[1] == "NULL":
            arr00.append(" ")
        else:
            arr00.append(row[1])

    rows = cur.execute('SELECT * FROM Room0_timetable1').fetchall()
    for row in rows:
        if row[1] == "NULL":
            arr01.append(" ")
        else:
            arr01.append(row[1])

    rows = cur.execute('SELECT * FROM Room0_timetable2').fetchall()
    for row in rows:
        if row[1] == "NULL":
            arr02.append(" ")
        else:
            arr02.append(row[1])

    rows = cur.execute('SELECT * FROM Room1_timetable0').fetchall()
    for row in rows:
        if row[1] == "NULL":
            arr10.append(" ")
        else:
            arr10.append(row[1])

    rows = cur.execute('SELECT * FROM Room1_timetable1').fetchall()
    for row in rows:
        if row[1] == "NULL":
            arr11.append(" ")
        else:
            arr11.append(row[1])

    rows = cur.execute('SELECT * FROM Room1_timetable2').fetchall()
    for row in rows:
        if row[1] == "NULL":
            arr12.append(" ")
        else:
            arr12.append(row[1])

    arr = [arr00, arr01, arr02, arr10, arr11, arr12]

    con.close()
    return arr


