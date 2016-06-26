#!/usr/bin/env python
#-*- coding:utf-8 -*-
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

if __name__ == '__main__':
	rlist = [(1,4), (2, 8), (3,5),(3,2), (9,16)]
	print my_sort(rlist, key=is_max, cmp=cmpp)