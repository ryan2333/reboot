#coding:utf-8

'''
异常：在运行时不可预知的一些错误，当发生错误时，以想让程序‘正常’运行

语法示例：

try:
	可能出错的代码
except Exception, e:
	运行错误代码
else:
	代码没有异常时执行
finally:
	代码不管有没有异常最后都执行
'''

f_lsit = [('/bin/abc', 'abc'), ('/bin/ls', 'ls')]

for src, dst in f_lsit:
	f_file = None
	d_file = None
	try:
		f_file = open(src, 'rb')
		d_file = open(dst, 'wb')
		size = 5
		while True:
			context = f_file.read(size)
			if not context:
				break
			d_file.write(context)
	except BaseException as e:
		print e
		print 'copy file %s failed!!'%src
	finally:
		if f_file:
			f_file.close()
		if d_file:
			d_file.close()
