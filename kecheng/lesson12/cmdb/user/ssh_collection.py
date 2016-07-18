#!/usr/bin/python
#coding:utf8
import paramiko
import getpass

'''
手动连接

'''

def ssh_execute(host,username,cmds=[], pkey='key', port=22):
	_rt_list = []
	#创建连接对象
	ssh = paramiko.SSHClient()

	#设置客户端登陆验证方式
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	#连接服务器信息
	ssh.connect(host, port, username, pkey=pkey)

	for _cmd in cmds:
		#操作
		stdin, stdout, stderr = ssh.exec_command(_cmd)

		#读取返回信息
		_rt_list.append((_cmd, stdout.readlines(), stderr.readlines()))

	ssh.close()
	return _rt_list


def sftp_execute(host, username, action, localpath, remotepath, pkey='key', port=22):
	t = paramiko.Transport((host,port))

	t.connect(username = username, pkey = pkey)

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
	host = '10.13.3.13'
	port = 22
	user = 'root'
	pkey_file = '/root/.ssh/id_rsa'
	key = paramiko.RSAKey.from_private_key_file(pkey_file)
#	password = getpass.getpass('please input password:')
	localpath = '/Users/yhzhao/test.py'
	remotepath = '/tmp/yhzhao.py'
	action = 'put'

#	print sftp_execute(host,user,password,action,localpath,remotepath,port)

	_rt_list = ssh_execute(host, user, ['df -h', 'ls'], key, port)
	for _cmd, _out, _err in _rt_list:
		print _cmd.strip(), [x.strip() for x in _out], [x.strip() for x in _err]