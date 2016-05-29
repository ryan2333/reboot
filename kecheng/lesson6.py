#-*- coding:utf-8 -*-
import time
import MySQLdb
'''
1.复习
2.作业
3.今天课程
	a. 用户身份认证
		session, cookie
		装饰器
			在所有函数之前执行一块代码
			在所有函数之后执行一块代码
			外层函数返回内层函数，外层函数必段有一个参数，内层函数执行外层函数传入的参数函数
			多个装饰器需引入模块functools
				from functools import wraps

		session  ---》服务器端一块存储：认证通过后，把认证信息发到Session中，每次请求来了以后，根据Session ID获取session中的认证信息，如果认证信息，继续访问，否则，跳转到登陆页面
		    导入session模块：from flask import session
		    	存session session['session_name'] = session_value
		    		app.secret_key = 'sdfjsd;fsd'
		    	取session session.get('session_name', None)

		cookie  ----》浏览器端一块存储

		消息闪现：
			app flash传递===》写到session
			在模块中，get_flashed_messages()引用，get_flashed_message()返回结果是一个list

	b. 数据库
		sql
		python --> mysql
		改上周作业

作业：
	1.修改，删除改为ID
	2.修改和删除唯一标训修改为id
	3.loganaly ===>入库
	url,ip,code,count
'''

'''
计算函数执行时间 
'''

def time_wrapper(func):  #传入函数
	def wrapper(): #计算函数计时
		print '开始计时: %s'%func.__name__
		start_time = time.time()  #计时开始
		rt = func()  #执行函数
		exec_time = time.time() - start_time  #计算时间 
		print '结束计时: %s'%func.__name__
		return exec_time  #返回执行时间
	return wrapper  #返回内层函数


def test1():
	print 'test1'

def test2():
	print 'test2'


def test3():
	print 'test3'
@time_wrapper
def test4():
	time.sleep(1)
	print 'test4'
@time_wrapper
def test5():
	time.sleep(2)
	print 'test5'

test4()
test5()

'''
数据库
show databases;
create database dbname;
use dbname;
show tables;
create table tbname(
	attrname attrtype
)
attrtype====>int
			varchar(n)

创建user数据库
create table user(
	id int primary key auto_increment,
	username varchar(25),
	password varchar(32),
	age int,
	phone varchar(15),
	email varchar(20)
);

查看表结构：
desc tablename;

查看创建表语句
show create table tableName

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8；

存数据
当所有列都插入数据时可以省略column，如insert into user values(10, 'user10', '123456', 18, '11111111111', 'user10@mail.com')
insert into tbname(column1, column2 ...) values (value1, value2 ...)
insert into tbname(username, password, age, phone, email) values ('user1', '123456' , 22, '110', 'user1@mail.com')

#查询：
select column1, column2 from user;
select * from user;
select * from user where username='user1';
select * from user where username='user1' and password='123456';

模糊查询
select * from user where username like '%user%';
select * from user where age > 20;
select * from user where age > 20 and age < 30;

更新：
update user set age=22 where username='user1';

mysql生成md5值
select md5('abc')

删除表：
drop table table name;

mysql统计：
select col1, col2, col3 count(*) from tableName group by col2,col3
select * count(*) from tableName group by col1, col2, col3 

排序：
select col1, col2, col3 count(*) as cnt from tableName group by col2,col3 order by cnt

'''

'''
python 操作mysql
import MySQLdb

1.创建连接
conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='pip123', db='mydb', charset='utf8')

2.创建游标
cur = conn.cursor()

3.执行语句
cur.execute('insert into user(username, password, age, phone, email) values("user1", md5("123456", 22, "11011011011", "user1@mail.com"))')

4.提交
conn.commit()

设置自动提交在执行操作前
conn.autocommit(True)

取消自动提交在执行操作前
conn.autocommit(False)

回滚在执行提交前，提交后不能生效
conn.rollback()

5.查询
cur.execute('select * from user')

取结果：
取一行
cur.fetchone()

取所有：
cur.fetchall()

7.关闭连接
cur.close()
conn.close()

'''
conn = MySQLdb.connect(host='localhost', passwd='pip123', user='root', db='mydb', charset='utf8')
cur = conn.cursor()
cur.execute('select * from user;')
for i in  cur.fetchall():
	print i