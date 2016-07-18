#!/usr/bin/env python

#encoding: utf-8

import smtplib
from email.mime.text import MIMEText
from datetime import datetime

from gconf import SMTP_SERVER_HOST, SMTP_SERVER_PORT, SMTP_USER, SMTP_PWD


def sendemail(to_list, title, content):
	_server = smtplib.SMTP(SMTP_SERVER_HOST, SMTP_SERVER_PORT)
	_server.set_debuglevel(True)
	_server.ehlo()
	#_server_conn.starttls()  #
	_server.login(SMTP_USER, SMTP_PWD)
	_msg = MIMEText(content, 'html', 'utf-8')
	_msg['Subject'] = title
	_msg['To'] = ";".join(to_list)
	_msg['From'] = SMTP_USER
	_msg['Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	_server.sendmail(SMTP_USER, to_list, _msg.as_string())
	_server.quit()


if __name__ == '__main__':
	sendemail(['543551194@qq.com'], 'alert email', 'cpu or mem warning')