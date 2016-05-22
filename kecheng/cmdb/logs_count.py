#!/usr/bin/env python
# -*- coding:utf-8 -*-

def log_count(fpath, number):
    Ngx_cnt = {}
    f = open(fpath, 'r')
    for i in f:
        flist = i.split()
        #print flist
        Ngx_cnt[(flist[0], flist[6], flist[8])] = Ngx_cnt.get((flist[0], flist[6], flist[8]),0) + 1
        #print "访问IP：%s，访问文件：%s, 返回状态: %s" %(flist[0], flist[6], flist[8])
    f.close()

    Ngx_list = Ngx_cnt.items()
    Ngx_dic = sorted(Ngx_list, key=lambda x:x[1], reverse = True)
    result_list = Ngx_dic[:number]
    return result_list

if __name__ == '__main__':
    print log_count(fpath='/Users/yhzhao/Downloads/www_access_20140823.log', number=10)