# -*- coding: utf-8 -*-
import sqlite3

def initialize_db():
    con = sqlite3.connect("sqlite.db")
    cur = con.cursor()
    # sql = "CREATE TABLE IF NOT EXISTS Room0_Timetable0(z_0 TEXT,z_1 TEXT,z_2 TEXT,z_3 TEXT,z_4 TEXT,z_5 TEXT,z_6 TEXT,z_7 TEXT,z_8 TEXT,z_9 TEXT,z_10 TEXT,z_11 TEXT,z_12 TEXT,z_13 TEXT,z_14 TEXT,z_15 TEXT,z_16 TEXT,z_17 TEXT,z_18 TEXT, z_19 TEXT,z_20 TEXT,z_21 TEXT,z_22 TEXT,z_23 TEXT,z_24 TEXT,z_25 TEXT);"
    # cur.execute(sql)
    # sql = "CREATE TABLE IF NOT EXISTS Room0_Timetable1(z_0 TEXT,z_1 TEXT,z_2 TEXT,z_3 TEXT,z_4 TEXT,z_5 TEXT,z_6 TEXT,z_7 TEXT,z_8 TEXT,z_9 TEXT,z_10 TEXT,z_11 TEXT,z_12 TEXT,z_13 TEXT,z_14 TEXT,z_15 TEXT,z_16 TEXT,z_17 TEXT,z_18 TEXT, z_19 TEXT,z_20 TEXT,z_21 TEXT,z_22 TEXT,z_23 TEXT,z_24 TEXT,z_25 TEXT);"
    # cur.execute(sql)
    # sql = "CREATE TABLE IF NOT EXISTS Room0_Timetable2(z_0 TEXT,z_1 TEXT,z_2 TEXT,z_3 TEXT,z_4 TEXT,z_5 TEXT,z_6 TEXT,z_7 TEXT,z_8 TEXT,z_9 TEXT,z_10 TEXT,z_11 TEXT,z_12 TEXT,z_13 TEXT,z_14 TEXT,z_15 TEXT,z_16 TEXT,z_17 TEXT,z_18 TEXT, z_19 TEXT,z_20 TEXT,z_21 TEXT,z_22 TEXT,z_23 TEXT,z_24 TEXT,z_25 TEXT);"
    # cur.execute(sql)
    # sql = "CREATE TABLE IF NOT EXISTS Room1_Timetable0(z_0 TEXT,z_1 TEXT,z_2 TEXT,z_3 TEXT,z_4 TEXT,z_5 TEXT,z_6 TEXT,z_7 TEXT,z_8 TEXT,z_9 TEXT,z_10 TEXT,z_11 TEXT,z_12 TEXT,z_13 TEXT,z_14 TEXT,z_15 TEXT,z_16 TEXT,z_17 TEXT,z_18 TEXT, z_19 TEXT,z_20 TEXT,z_21 TEXT,z_22 TEXT,z_23 TEXT,z_24 TEXT,z_25 TEXT);"
    # cur.execute(sql)
    # sql = "CREATE TABLE IF NOT EXISTS Room1_Timetable1(z_0 TEXT,z_1 TEXT,z_2 TEXT,z_3 TEXT,z_4 TEXT,z_5 TEXT,z_6 TEXT,z_7 TEXT,z_8 TEXT,z_9 TEXT,z_10 TEXT,z_11 TEXT,z_12 TEXT,z_13 TEXT,z_14 TEXT,z_15 TEXT,z_16 TEXT,z_17 TEXT,z_18 TEXT, z_19 TEXT,z_20 TEXT,z_21 TEXT,z_22 TEXT,z_23 TEXT,z_24 TEXT,z_25 TEXT);"
    # cur.execute(sql)
    # sql = "CREATE TABLE IF NOT EXISTS Room1_Timetable2(z_0 TEXT,z_1 TEXT,z_2 TEXT,z_3 TEXT,z_4 TEXT,z_5 TEXT,z_6 TEXT,z_7 TEXT,z_8 TEXT,z_9 TEXT,z_10 TEXT,z_11 TEXT,z_12 TEXT,z_13 TEXT,z_14 TEXT,z_15 TEXT,z_16 TEXT,z_17 TEXT,z_18 TEXT, z_19 TEXT,z_20 TEXT,z_21 TEXT,z_22 TEXT,z_23 TEXT,z_24 TEXT,z_25 TEXT);"
    # cur.execute(sql)
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
    name_ = cur.execute('select name from userdata where id = \''+id+'\'').fetchone()
    pw_ = cur.execute('select pw from userdata where id = \''+id +'\'').fetchone()
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
        if cur.execute('SELECT name FROM Room'+room+'_timetable'+date+' where time = t_'+str(i)).fetchone()[0] != 'NULL':
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
    for i in range(0,28)
    cur.execute('UPDATE Room0_timetable0 SET ')