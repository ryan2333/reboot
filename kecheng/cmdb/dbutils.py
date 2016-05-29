#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb as db
import gconfig

def excute_mysql(sql, args=(), fetch=True):
	_conn = None
	_cur = None
	_rt_list = []
	_count = 0
	try:
		print sql
		_conn = db.connect(host=gconfig.MySQL_HOST, port=gconfig.MySQL_PORT, user=gconfig.MySQL_USER,\
							passwd=gconfig.MySQL_PASSWD, db=gconfig.MySQL_DB, charset=gconfig.MySQL_CHARSET)
		_cur = _conn.cursor()
		_count = _cur.execute(sql, args)
		if fetch:
			_rt_list = _cur.fetchall()
		else:
			_conn.commit()
	except Exception, e:
		print e

	finally:
		if _cur:
			_cur.close()
		if _conn:
			_conn.close()
	return _count, _rt_list