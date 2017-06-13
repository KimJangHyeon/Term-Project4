# -*- coding: utf-8 -*-
import sqlite3
import datetime
import logging
import unicodedata

import math

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
    con.commit()
    con.close()
    return

def booking_room(room, date, time, name):
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    str = 'UPDATE Room' + room + '_timetable' + date + ' SET name = ' + '\'' + name + '\' ' + 'WHERE time=' + '\'' + 't_'+time+'\''
    cur.execute(str)
    con.commit()
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
    if mon==1:
        return 31
    if mon == 2:
        return 28
    if mon == 3:
        return 31
    if mon == 4:
        return 30
    if mon == 5:
        return 31
    if mon == 6:
        return 30
    if mon == 7:
        return 31
    if mon == 8:
        return 31
    if mon == 9:
        return 30
    if mon == 10:
        return 31
    if mon == 11:
        return 30
    if mon == 12:
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
    arr_=[]
    now_arr_ = []
    arr_.append(int(unicodedata.normalize('NFKD', arr[0]).encode('ascii','ignore')))
    arr_.append(int(unicodedata.normalize('NFKD', arr[1]).encode('ascii','ignore')))
    arr_.append(int(unicodedata.normalize('NFKD', arr[2]).encode('ascii','ignore')))

    nowDate_arr = nowDate.split('-')

    now_arr_.append(int(nowDate_arr[0]))
    now_arr_.append(int(nowDate_arr[1]))
    now_arr_.append(int(nowDate_arr[2]))


    if nowDate == today_db[0]:
        con.close()
        return 0
    db_prior = priority(arr_)
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
            arr00.append(unicodedata.normalize('NFKD', row[1]).encode('ascii','ignore'))

    rows = cur.execute('SELECT * FROM Room0_timetable1').fetchall()
    for row in rows:
        if row[1] == "NULL":
            arr01.append(" ")
        else:
            arr01.append(unicodedata.normalize('NFKD', row[1]).encode('ascii','ignore'))

    rows = cur.execute('SELECT * FROM Room0_timetable2').fetchall()
    for row in rows:
        if row[1] == "NULL":
            arr02.append(" ")
        else:
            arr02.append(unicodedata.normalize('NFKD', row[1]).encode('ascii','ignore'))

    rows = cur.execute('SELECT * FROM Room1_timetable0').fetchall()
    for row in rows:
        if row[1] == "NULL":
            arr10.append(" ")
        else:
            arr10.append(unicodedata.normalize('NFKD', row[1]).encode('ascii','ignore'))

    rows = cur.execute('SELECT * FROM Room1_timetable1').fetchall()
    for row in rows:
        if row[1] == "NULL":
            arr11.append(" ")
        else:
            arr11.append(unicodedata.normalize('NFKD', row[1]).encode('ascii','ignore'))

    rows = cur.execute('SELECT * FROM Room1_timetable2').fetchall()
    for row in rows:
        if row[1] == "NULL":
            arr12.append(" ")
        else:
            arr12.append(unicodedata.normalize('NFKD', row[1]).encode('ascii','ignore'))

    arr = [arr00, arr01, arr02, arr10, arr11, arr12]

    con.close()
    return arr


def load_reserved_data(name):
    gathered_data = []

    reserved_data = get_reserved_data('Room0_timetable0', name, 0, 0)
    if reserved_data is not None:
        gathered_data.append(reserved_data)

    reserved_data = get_reserved_data('Room0_timetable1', name, 0, 1)
    if reserved_data is not None:
        gathered_data.append(reserved_data)

    reserved_data = get_reserved_data('Room0_timetable2', name, 0, 2)
    if reserved_data is not None:
        gathered_data.append(reserved_data)

    reserved_data = get_reserved_data('Room1_timetable0', name, 1, 0)
    if reserved_data is not None:
        gathered_data.append(reserved_data)

    reserved_data = get_reserved_data('Room1_timetable1', name, 1, 1)
    if reserved_data is not None:
        gathered_data.append(reserved_data)

    reserved_data = get_reserved_data('Room1_timetable2', name, 1, 2)
    if reserved_data is not None:
        gathered_data.append(reserved_data)

    return gathered_data

def get_reserved_data(table_name, name, room, day_plus):
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()

    now = datetime.datetime.today()
    now += datetime.timedelta(days=day_plus)
    now_tuple = now.timetuple()

    cnt = 0
    start = 0
    index_start = -1
    find = False

    rows = cur.execute('SELECT * FROM ' + table_name).fetchall()
    for row in rows:
        index_start = index_start + 1
        if name == unicodedata.normalize('NFKD', row[1]).encode('ascii', 'ignore'):
            if find is False:
                start = index_start
                find = True
            cnt = cnt + 1
        else:
            if find is False:
                continue
            if find is True:
                break

    con.close()

    tmp_arr = []
    date = str(now_tuple.tm_year) + "-" + str(now_tuple.tm_mon) + "-" + str(now_tuple.tm_mday)

    hour = (int(math.floor(start/2)) + 8)
    minute = ((start % 2) * 30)

    start_time = str(hour) + ':' + str(minute)

    hour = (int(math.floor((int(start) + int(cnt))/2)) + 8)
    minute = (((int(start) + int(cnt)) % 2) * 30)

    end_time = str(hour) + ':' + str(minute)

    if cnt != 0:
        tmp_arr.append(date)
        tmp_arr.append(room)
        tmp_arr.append(start_time)
        tmp_arr.append(end_time)
        return tmp_arr

    return None


def reserve_delete(room, date, name):
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    date_arr=date.split('-')
    date_arr_=[]
    date_arr_.append(int(unicodedata.normalize('NFKD', date_arr[0]).encode('ascii', 'ignore')))
    date_arr_.append(int(unicodedata.normalize('NFKD', date_arr[1]).encode('ascii', 'ignore')))
    date_arr_.append(int(unicodedata.normalize('NFKD', date_arr[2]).encode('ascii', 'ignore')))
    now_arr=nowDate.split('-')
    now_arr_=[int(now_arr[0]), int(now_arr[1]), int(now_arr[2])]
    num = priority(date_arr_)-priority(now_arr_)
    print num
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    print 'UPDATE Room'+room+'_timetable'+str(num)+' SET name='+'\''+'NULL'+'\'' + ' WHERE name = '+'\''+name+'\''
    cur.execute('UPDATE Room'+room+'_timetable'+str(num)+' SET name='+'\''+'NULL'+'\'' + ' WHERE name = '+'\''+name+'\'')

    con.commit()
    con.close()
