# -*- coding: utf-8 -*-
import sqlite3

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

#id를 받고 그 유저의 inform을 딕셔너리로 출력
def infrom_by_id(id):
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    name_ = cur.execute('select name from userdata where id = \''+id+'\'').fetchone()
    pw_ = cur.execute('select pw from userdata where id = \''+id +'\'').fetchone()
    return {'name':name_[0], 'id':id, 'pw':pw_[0]}

