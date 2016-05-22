#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask, render_template
from logs_count import log_count
from flask import request, redirect
import user_action, user_action

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('user_login.html')

@app.route('/logs/')

def log1_count():
	#return number
	number = request.args.get('number', 10)
	number = int(number) if str(number).isdigit() else 10
	fpath = '/Users/yhzhao/Downloads/www_access_20140823.log'
	title = 'Top{number}'.format(number=number)
	result = log_count(fpath=fpath, number=number)
	return render_template('templ.html',title=title, content=result)

@app.route('/login/', methods=['POST', 'GET'])
def login():
	if request.method == 'GET':
		#获取POST传过来的参数
		parms = request.args
	else:
		#获取POST传过来的参数
		parms = request.form
	username = parms.get('username', '')
	password = parms.get('password', '')
	#return '%s:%s'%(username,password)
	if user_action.validate_login(username, password):
		return redirect('/logs/')
	else:
		#登陆失败，返回错误信息回页面
		return render_template('user_login.html', username=username, error="username or password error!!")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)

