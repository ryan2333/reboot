#!/usr/bin/env python


sfile = '/Users/yhzhao/Downloads/Tcolor/b.log'

rt = {}

f = open(sfile, 'r')

for i in f:
	a = i.split()[11:14]
	a[0] = a[0].split(":")[0]
	a[2] = a[2].strip(',')
	k = " ".join(a)
#	print k
	rt[k] = rt.get(k,0) + 1


result = rt.items()
r = sorted(result, key=lambda x:x[1],reverse=True)[:20]

for i in r:
	print i