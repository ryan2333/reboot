#!/usr/bin/python
#coding:utf8
import paramiko
import getpass

'''
手动连接

'''

def ssh_execute(host,username,password,cmds=[],port=22):
	_rt_list = []
	#创建连接对象
	ssh = paramiko.SSHClient()

	#设置客户端登陆验证方式
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	#连接服务器信息
	ssh.connect(host,port,username,password)

	for _cmd in cmds:
		#操作
		stdin, stdout, stderr = ssh.exec_command(_cmd)

		#读取返回信息
		_rt_list.append((_cmd,stdout.readlines(), stderr.readlines()))

	ssh.close()
	return _rt_list


def sftp_execute(host,username,password,action,localpath, remotepath, port=22):
	t = paramiko.Transport((host,port))

	t.connect(username = username, password = password)

	sftp = paramiko.SFTPClient.from_transport(t)

	remotepath = remotepath

	localpath = localpath

	if action == 'put':
		sftp.put(localpath,remotepath)
	else:
		sftp.get(localpath,remotepath)

	t.close()
	return 'success'


if __name__ == '__main__':
	host = '182.61.42.4'
	port = 22
	user = 'root'
	password = getpass.getpass('please input password:')
	localpath = '/Users/yhzhao/test.py'
	remotepath = '/tmp/yhzhao.py'
	action = 'put'

	print sftp_execute(host,user,password,action,localpath,remotepath,port)

	_rt_list = ssh_execute(host,user,password,['python /tmp/yhzhao.py'],port)
	for _cmd, _out, _err in _rt_list:
		print _cmd, _out, _err
