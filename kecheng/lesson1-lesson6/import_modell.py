#coding:utf-8

#import modell
from modell import my_sort, is_max, cmpp

rlist = [(1,4), (2, 8), (3,5),(3,2)]

print my_sort(rlist, key=is_max, cmp=cmpp)