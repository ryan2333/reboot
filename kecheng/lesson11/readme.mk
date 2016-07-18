1.复习
	class ClassName(object):
	    pass

2.作业
3.新课程
	a. 模块
	b. 监控，获取主机上的CPU，内存使用率，标识符IP
	c. agent===>server
	d. server接收，存储
	e. 展示


a. 模块：
	1. 安装：pip install xxx
	2. import xxxx
	3. dir()
	4. help()

	os:
		listdir
		system/popen
		path
	sys
	datetime
	time
	logging/trackback
	paramiko
	getpass
	argparse
	hashlib
	requests





	time:
		time.time():获取当前时间戳
		time.localtime: 将unix转换为struct_time
		
		
		time.localtime()
		time.struct_time(tm_year=2016, tm_mon=7, tm_mday=10, tm_hour=13, tm_min=46, tm_sec=41, tm_wday=6, tm_yday=192, tm_isdst=0)

		time.strptime(): 字符串时间转换为stuct_time时间
		time.strptime('2016-09-09', '%Y-%m-%d')
		time.struct_time(tm_year=2016, tm_mon=9, tm_mday=9, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=253, tm_isdst=-1)

		time.strftime():将struct_time转换为字符串时间
		time.strftime('%Y-%m-%d', time.localtime())
		'2016-07-10'

		datetime
		datetime.datetime.now() - datetime.timedelta(days=1)
		datetime.datetime(2016, 7, 9, 14, 7, 27, 809120)


		md5值计算：
		hashlib.md5()
		 _md5 = hashlib.md5()
		>>> _md5.update('123456')
		>>> _md5.hexdigest()

		注意：每次要重新计算MD5值需重新获取MD5


		getpass:
		pwd = getpass.getpass('please input password:')


restapi
	http请求规范
	一切皆资源
	resource


GET
	/resource/<pk>/		获取单条资源
	/resource/			获取所有资源


POST	/resource/
	/创建/添加资源


PUT 	/resource/<pk>/
	/创建/更新

DELETE




CREATE table performs(
    id bigint primary key auto_increment,
    ip varchar(128),
    cpu float,
    ram float,
    time datetime
)engine=innodb default charset=utf8;




作业：
1. assets的采购时间改成%Y-%m-%d
2. 添加用户，修改用户密码md5_str()函数
3. 课程上的流程做完
4. web执行命令
	from 提交ip,port, username,password, cmds==>ssh.py获取结果显示
	管理员密码验证













