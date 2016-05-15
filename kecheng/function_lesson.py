#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
函数：对一堆代码进行命名，这堆代码功能和名字对应，在以后使用时，只使用函数名称进行代码一调用
好处：代码复用，见名知意（易读）
定义：def function_name():  代码块。。。
返回值：python中函数返回值可以为多个，返回的数据结构为元组
	return a,b,c
作用域：LGB  优先级：L=>local ---> G=>global ---> B=>built
查看built变量
	dir(__builtins__)
传值与传址：值：元组和字典，址：列表
可变参数：*args,参数组成元组
		**kwargs,参数为字典

作业：
一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
期待结果：[(2,3),(1,4),(5,1)]
'''

import time

def logs_function(fpath, dpath, number=10):

	Ngx_cnt = {}

	t = time.time()
	f = open(fpath, 'r')
	for i in f:
	    flist = i.split()
	    #print flist
	    Ngx_cnt[(flist[0], flist[6], flist[8])] = Ngx_cnt.get((flist[0], flist[6], flist[8]),0) + 1
	    #print "访问IP：%s，访问文件：%s, 返回状态: %s" %(flist[0], flist[6], flist[8])
	f.close()
	t1 = time.time()
	print "统计使用时间 ：%s 秒" %(t1 - t)

	Ngx_list = Ngx_cnt.items()

	#全部排序后取访问次数最高的10个
	# for i in range(len(Ngx_list) - 1):
	#     for j in range(len(Ngx_list) - 1 - i):
	#         if Ngx_list[j][1] > Ngx_list[j + 1][1]:
	#             Ngx_list[j], Ngx_list[j+1] = Ngx_list[j+1], Ngx_list[j]

	#最排访问次数最高的10个，然后返回后10个
	# t = time.time()
	# for i in range(number):
	#     for j in range(len(Ngx_list) - 1 - i):
	#         if Ngx_list[j][1] > Ngx_list[j + 1][1]:
	#             Ngx_list[j], Ngx_list[j+1] = Ngx_list[j+1], Ngx_list[j]
	# 
	# Ngx_top10 = Ngx_list[-1:-number:-1]
	# t1 = time.time()
	# print "排序使用时间 ：%s 秒" %(t1 - t)
	# j = 1
	# for i in Ngx_top10:
	#     print "排名%s: 访问IP：%s, 访问文件：%s，访问状态：%s，访问次数：%s;" %(j, i[0][0], i[0][1], i[0][2], i[1])
	#     j += 1

	#python 字典排序
	Ngx_dic = sorted(Ngx_list, key=lambda x:x[1], reverse = True)
	d = open(dpath, 'w')
	str1='''
	<!DOCTYPE html>
	<html>
	<head>
	    <meta charset="utf-8" />
	    <title>{title}</title>
	</head>
	<body>
	    <table border="1">
	        <th>
	            <tr>
	                <td align="center">排名</td>
	                <td>IP</td>
	                <td>Url</td>
	                <td>Code</td>
	                <td>Count</td>
	            </tr>
	        </th>
	        <tbody>
	            {content}
	        </tbody>
	    </table>
	</body>
	</html>
	'''
	title = 'Top{number} access page'.format(number=number)
	content=''
	for i in range(number):
	    print "排名%s: 访问IP：%s, 访问文件：%s，访问状态：%s，访问次数：%s;" %(i + 1, Ngx_dic[i][0][0], Ngx_dic[i][0][1], Ngx_dic[i][0][2], Ngx_dic[i][1])
	#    d.write('%s %s %s %s %s\n'%(i, Ngx_dic[i][0][0], Ngx_dic[i][0][1], Ngx_dic[i][0][2], Ngx_dic[i][1]))
	    content += '<tr><td align="center">%s</td><td>%s</td><td>%s</td><td align="center">%s</td><td align="center">%s</td></tr>'%((i + 1, Ngx_dic[i][0][0], Ngx_dic[i][0][1], Ngx_dic[i][0][2], Ngx_dic[i][1]))

	d.write(str1.format(title=title,content=content))
	d.close()


# number=20
# fpath = '/Users/yhzhao/Downloads/www_access_20140823.log'
# dpath = '/Users/yhzhao/Downloads/Ngx_access_top{number}.html'.format(number=number)
# logs_function(dpath = dpath, fpath = fpath,number=number)

def add(x, y):
	return "%-5s + %-5s is : %s"%(x, y, x + y)


def jian(x, y):
	return "%-5s - %-5s is : %s"%(x, y, x + y)


def chen(x, y):
	return "%-5s * %-5s is : %s"%(x, y, x + y)


def chu(x, y):
	return "%-5s / %-5s is : %s"%(x, y, x + y)

print add(2, 5)
print jian(33, 15)
print chen(3, 7)
print chu(10, 5)


def jiecheng(n):
	if n < 0:
		result = "your number is error!1"
	elif n == 1 or n == 0:
		result = 1
	else:
		result = 1
		for i in range(1,n + 1):
			result *= i
	return "%-5s的阶乘结果为：%s"%(n, result)

print jiecheng(5)

#函数递归调用
def fab(n):
	if n == 0:
		return 1
	return n * fab(n - 1)

print fab(5)

#函数作用域lGB
gname = 'abc'

def test1():
	lname = 'localname'
	print "test1"
	print lname
	print gname


def test2():
	gname = 'localgname'
	lname = 'localname'
	print "test2"
	print lname
	print gname

test1()
print gname
test2()
print gname

def test3():
	global gname
	print gname
	gname = 'dddddd'
	print test3
	print gname
test3()
print gname


def test4(gname):
	print gname
	gname = 'localgname'
	print gname

test4(gname)
print gname

gname = ['globalname']
def test5(gname):
	print gname
	gname[0] = 'localname'
	print gname

test5(gname)
print gname

#可变参数*args
def test6(*args):
	result = 0
	for i in args:
		result += i
	return result

print test6(1,4,6,7)

#可变参数**kwargs

def test7(**kwargs):
	result = 0
	print kwargs

test7(a=1, b=2, c=3)

#可变参数组合,注意列表放前(*args)，字典放后(**kwargs)
def test8(*args, **kwargs):
	print args
	print kwargs

test8(1, 2, 3, 4, a=1, b=2, c=3)



