#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
1.复习
2.列表推导式， sorted
3.模块，包
	包必须包含__init__.py文件
flask
json
	json.dumps():存储到文件
	json.loads():从文件读取
'''

#列表推导式
#[translate(x) for x in iterlist if filter(x)]
#前面做转换，后面做列表推导和过滤
#相当于
'''
def filter(x):
	return x % 2 = 0

def translate(x):
	return x * x
'''

print [x for x in range(11)]
print [x * x for x in range(11)]
print [x * x for x in range(11) if x % 2 == 0]
print [(x, x * 2, x * x) for x in range(11)]
#print [("%s * %s = %s"%(y, x, x * y)) for x in range(1,10) for y in range(1,x+1)]

#lambda函数

add = lambda x,y : x + y

print add(10, 25)


#提取最大值：
def is_max(t):
	result = None
	for i in range(len(t)):
		if t[i] > result:
			result = t[i]
	return result

#定义比较函数
def cmpp(x, y):
	if x > y:
		return True
	else:
		return False

#使用自定义求最大值函数进行冒泡排序
def my_sort(rlist, key=None, cmp=None):
	if key == None:
		key = is_max
	if cmp == None:
		cmp = cmpp
	for j in range(len(rlist) - 1):
		for k in range(len(rlist) - 1 - j):
			if cmp(key(rlist[k]), key(rlist[k + 1])):
				rlist[k], rlist[k + 1] = rlist[k + 1], rlist[k]
	return rlist

rlist = [(1, 4), (5, 1), (2, 3), (2, 1), (8, 5), (2, 3), (6, 4), (15, 8), (-10 ,2), (-8, -2)]
print my_sort(rlist, is_max, cmp)

rlist = [{'name': 'ryan'}, {'name': 'zz'}, {'name': 'cc'}]
print my_sort(rlist, key = lambda x: x['name'], cmp=cmpp)

rlist = [{'name': 'ryan'}, {'name': 'zz'}, {'name': 'cc'}]
print sorted(rlist, key = lambda x: x['name'])


