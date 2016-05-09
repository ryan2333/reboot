#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
1.文件路径：
    绝对路径和相对路径
    绝对路径：/ c:/
    相对路径：当前进程启动目录
2.文件操作：
读、写
    找到文件，==》文件路径
    打开文件 ==》open(path,mode)
        mode:
            r：读
            w：写
            a：追加
    查看、修改，删除,保存
        读：
        read(),readlines(),readline()
    关闭文件
        close()
写：
    write:只能写字符串
    writeline:列表里元素必须为字符串

'''

path = '/Users/yhzhao/Documents/reboot/a.txt'

#read读文件，一次性将文件全读出
f = open(path, 'r')
text = f.read()
f.close()
print text

#指定每次读出的字节数：
f = open(path, 'r')
while True:
    text = f.read(2)
    if len(text) == 0:
        break
    print text
f.close()

#readline:每次读取一行，可指定参数，每次读取多少字节后换行，或读到换行符后进行换行
f = open(path, 'r')
while True:
    text = f.readline(2)
    if len(text) == 0:
        break
    print text
f.close()

#readlines: 每次读取所有行，按换行符分隔读入一个列表,保留行尾的换行符
f = open(path, 'r')
#text = f.readlines()
for i in f:
    print i
f.close()
print text

#读取文件，分割字符串
'''
文件内容：
ryan1:10,ryan2:20,ryan3:30
ryan4:40,ryan5:50,ryan6:60
ryan7:70,ryan8:80,ryan9:90
'''
f = open(path, 'r')
rt_list = []
for s in f:
    rt_names = s.split(',')
    for i in rt_names:
        i = i.strip()
        name, uid = i.split(':')
        rt_list.append((name, int(uid)))
f.close()
print rt_list

#写文件write
path = '/Users/yhzhao/Documents/reboot/ab.txt'
f = open(path, 'w')
f.write('ryan1:11,ryan2:12,ryan3:13')
f.close()
f = open(path, 'r')
rt_list = []
for s in f:
    rt_names = s.split(',')
    for i in rt_names:
        i = i.strip()
        name, uid = i.split(':')
        rt_list.append((name, int(uid)))
f.close()
print rt_list

#写文件writelines,写入list
path = '/Users/yhzhao/Documents/reboot/ab.txt'
f = open(path, 'w')
f.writelines(['ryan1:11,ryan2:12,ryan3:13','ryan1:11,ryan2:12,ryan3:13','ryan1:11,ryan2:12,ryan3:13'])
f.close()