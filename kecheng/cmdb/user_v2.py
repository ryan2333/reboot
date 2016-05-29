#!/usr/bin/env python
#-*- coding:utf-8 -*-


import json, gconfig
import MySQLdb as db
from flask import request


def get_user():
	_cols = ('id', 'username', 'password', 'age', 'phone', 'email')
	_sql = 'select * from user'
	_conn = None
	_cur = None
	_rt = []
	try:
		print _sql
		_conn = db.connect(host=gconfig.MySQL_HOST, port=gconfig.MySQL_PORT, user=gconfig.MySQL_USER,\
							passwd=gconfig.MySQL_PASSWD, db=gconfig.MySQL_DB, charset=gconfig.MySQL_CHARSET)
		_cur = _conn.cursor()
		_count = _cur.execute(_sql)
		_rt_list = _cur.fetchall()
		print _rt_list
		for i in _rt_list:
			_rt.append(dict(zip(_cols, i)))
	except Exception, e:
		print e

	finally:
		if _cur:
			_cur.close()
		if _conn:
			_conn.close()
	return _rt

def file_read(file):
	try:
		f = open(file, 'r')
		content = f.read()
		f.close()
		return content
	except Exception, e:
		print e
		return e

def file_write(file, content):
	try:
		f = open(file, 'wb')
		f.write(content)
		f.close()
		return 'sucess'
	except Exception, e:
		print e
		return False


def validate_login(username, password):
	#_sql = 'select * from user where username="{username}" and password=md5("{password}")'.format(username=username, password=password)
	#为了预防SQL注入，SQL语句写成如下：
	_sql1 = 'select * from user where username=%s and password=md5(%s)'
	_conn = None
	_cur = None
	_count = 0
	try:
		print _sql1
		_conn = db.connect(host=gconfig.MySQL_HOST, port=gconfig.MySQL_PORT, user=gconfig.MySQL_USER,\
							passwd=gconfig.MySQL_PASSWD, db=gconfig.MySQL_DB, charset=gconfig.MySQL_CHARSET)
		_cur = _conn.cursor()
		#为了预防SQL注入，执行语句写成如下：
		#_count = _cur.execute(_sql)
		_count = _cur.execute(_sql1, (username, password))
	except Exception, e:
		print e
	finally:
		if _cur:
			_cur.close()
		if _conn:
			_conn.close()
	return _count != 0


def user_list(number):
	users = get_user()
	userlist = sorted(users, key=lambda x:x['username'])
	if len(userlist) > number:
		return userlist[:number]
	else:
		return userlist
def add_user(username, password, age, phone, email):
	userlist = get_user()
	userinfo = {'username': username, 'password': password, 'age': age, 'phone': phone, 'email': email}
	userlist.append(userinfo)
	result = file_write(gconfig.USER_FILE, json.dumps(userlist))
	return result
	# f = open(gconfig.USER_FILE, 'wb')
	# f.write(json.dumps(userlist))
	# f.close()

def delUser(username):
	users = get_user()
	for i in range(0, len(users)):
		if users[i]['username'] == username:
			users.pop(i)
			break
	result = file_write(gconfig.USER_FILE, json.dumps(users))
	return result

def modifyUser(username, password, age, phone, email):
	users = get_user()
	for i in range(0,len(users)):
		if users[i]['username'] == username:
			users[i].update({'password': password, 'age': age, 'phone': phone, 'email': email})

	result = file_write(gconfig.USER_FILE, json.dumps(users))
	return result

if __name__ == '__main__':
	delUser('user2')