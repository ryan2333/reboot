#coding:utf-8

import csv, smtplib, xlrd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_mail(to_list):
	mailHost = 'smtp.aa.com.cn'
	mailUser = 'aaaa'
	mailPass = 'bbbbbbb'
	mailDomain = 'aa.com.cn'
	me = mailUser + '<' + mailUser+'@'+mailDomain+'>'

	#发送不带附件的邮件
	# msg = MIMEText('Hello %s:\n\t您的VPN帐号是：%s\n\t您的VPN密码是：%s\n'%('aa','aa','123456'),'plain','utf-8')
	# msg['Subject'] = 'test mail'
	# msg['To'] = '543551194@qq.com'
	# msg['From'] = mailUser

	#发送带附件邮件
	msg = MIMEMultipart()
	msg['Subject'] = '新VPN帐号信息'
	msg['To'] = to_list[1]
	msg['From'] = me
	msg.attach(MIMEText(u'HI %s:\n\t由于您的新VPN帐号是：%s\n\t您的VPN密码是：%s\n'%(to_list[0],to_list[2],to_list[3]),'plain','utf-8'))
	with open('vpn使用说明.docx','rb') as f:
		mime = MIMEBase('application','octet-stream',filename='vpn使用说明.docx')
		mime.add_header('Content-Disposition', 'attachment', filename='vpn使用说明.docx')
		mime.add_header('Content-ID', '<0>')
		mime.add_header('X-Attachment-ID', '<0>')
		mime.set_payload(f.read())
		encoders.encode_base64(mime)
		msg.attach(mime)

	#发送
        smtp_port = 25
        #加密端口为587
	_server = smtplib.SMTP(mailHost,smtp_port)
       #加密需在此增加一行：server.starttls()
#	_server.set_debuglevel(1)
	_server.ehlo()
	_server.login(mailUser,mailPass)
	print to_list
	_server.sendmail(me,to_list[1],msg.as_string())
	_server.quit()




if __name__ == '__main__':
	data = xlrd.open_workbook('vpnAccout.xlsx')
	table = data.sheets()[0]
	rows = table.nrows
	#to_list = []
	#for i in range(4,rows):
	#	value = table.row_values(i)
	#	if len(value) == 7:
	#		to_list.append((value[1], value[2].strip(),value[3],value[4]))
        to_list = [(u'aa', u'aa@cc.com', u'aa', u'sdfsdf'),(u'bb', u'bb@bb.com', u'bb', u'sdsfadfsdf')]
	for i in to_list:
		send_mail(i)
