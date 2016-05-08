#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
字符串：定义：'' ,"" ,'''''', """ """
    访问：可通过索引访问，从左到右0...len(str)-1,从右到左-1...-len(str)
    不可更改，
    可以使用切片
    方法：
        in:查看子字符串是否包含在原字符串中
        join:将list用指定字符连接
        split：将字符中按指定字符分隔开来，默认为空格
        find: 查找指定字符串在原字符串中的第一个位置，如果字符串不存在返回-1
        index: 查找指定了符串在原字符串中的第一个位置，如果不存在则报错
        capitalize ：首字母大小，其它字母小写
        lower: 所有字母转换为小写
        upper：所有字母大写
        count: 统计字母在字符串中出现的次数
        strip(): 删除字符串两侧的指定字符，默认为空格
        rstrip()：删除字符串右侧的指定字符，默认为空格
        lstrip()：删除字符串左侧的指定字符，默认为空格
        swapcase()：将字符串大写变为小写，小写变为大写
        
'''
chars = 'skdfjas;dfjsl;dfkjs;d'
print chars[0], chars[-1]
print chars[3:7:2]
print 'k' in chars
print 'kf' in chars
print 'kdf' in chars

#字符串分割成列表
rt_list = chars.split(';')
print rt_list

#将列表用_连接成一个字符串，注意，列表中元素必须都为字符串
rt_char = "_".join(rt_list)
print rt_char

#字符串查找
chars = 'sdjfdslkjlkfdjfjd'
#print chars.find('sdj')
#print chars.find('djfg')
#print chars.index('fds')
#print chars.index('fdjfg')
#首字母大写实现
chars = 'dflksjdflKKDDKKDskdfjsdlkfj'
chars = chars[:1].upper() + chars[1:].lower()
print chars

#字符串统计
print chars.count('d')

#字符串替换
rt_str = chars.replace('d', 'F')
print rt_str

#查找字符串的的d字符，并替换前3个为F
rt_str1 = chars.replace('d', 'F', 3)
print rt_str1

#字符串删除
chars = '   jdfks;dkfjs;kfjs;dfkjsd;lkfjsd;   '
rt_str1 = chars.strip()
print rt_str1
rt_str2 = rt_str1.rstrip(';')
print rt_str2
rt_str3 = rt_str2.lstrip('jdf')
print rt_str3

#字符串反转：
chars = 'ijsf;skjdf;oskjdflks;kdjfs;'
#方法1：
str_list = list(chars)
str_list.reverse()
rt_str = "".join(str_list)
print rt_str
#方法2：
s = ''
for i in chars:
    s = i + s

print s

#分割用户
s = raw_input("Enter usernmae1:id1, username2:id2:")
s = s.strip()
rt_list = []
rt_names = s.split(',')
for i in rt_names:
    i = i.strip()
    name, uid = i.split(':')
    rt_list.append((name, int(uid)))
print rt_list


     


