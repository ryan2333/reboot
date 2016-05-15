#!/usr/loca/env python
# -*- coding:utf-8 -*-

fpath = '/Users/yhzhao/Downloads/test.txt'
dpath = '/Users/yhzhao/Downloads/text.txt'

f = open(fpath, 'r')
d = open(dpath, 'w')
f_list = f.readlines()

print f_list
for i in range(len(f_list)):
	print f_list[i]
	if i == 1:
		d.write('wd')
	else:
		d.write(f_list[i].strip().replace('reboot', 'hello'))

d.close()
f.close()

