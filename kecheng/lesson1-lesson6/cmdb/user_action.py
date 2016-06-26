#!/usr/bin/env python
#-*- coding:utf-8 -*-
import gconfig
import json


def get_user():
	try:
		f = open(gconfig.USER_FILE, 'rb')
		content = f.read()
		f.close()
		return json.loads(content)
	except BaseException as e:
		print e
		return []
def validate_login(username, password):

	users = get_user()
	for user in users:
		if user.get('username') == username and user.get('password') == password:
			return True
	return False

print validate_login('user1', '123456')


