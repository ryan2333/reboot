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
        endswith():以子串结束的字符串
        startswith():以子串开头的字符串
        isalnum():判断是否为数字和字母
        isdigit():判断是否为数字
        isalpha():判断是否为字母
        ...
        splitlines():按换行符分割字符串
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
#s = raw_input("Enter usernmae1:id1, username2:id2:")
s = 'ryan1:10,ryan2:20,ryan3:30'
s = s.strip()
rt_list = []
rt_names = s.split(',')
for i in rt_names:
    i = i.strip()
    name, uid = i.split(':')
    rt_list.append((name, int(uid)))
print rt_list

#取字符串中字母出现次数的top10
#1.采用冒泡排序，生成有序列表
#2.采最后10个元素
read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
dic_count1 = {}
for x in read_me:
    dic_count1[x] = dic_count1.get(x, 0) +  1
print dic_count1


dict_list = dic_count1.items()
#方法1：全部排序
for i in range(len(dict_list)-1):
    for j in range(len(dict_list) - 1 - i):
        if dict_list[j][1] > dict_list[j + 1][1]:
            dict_list[j],dict_list[j + 1] = dict_list[j + 1],dict_list[j]
print dict_list
print dict_list[-1:-11:-1]

#方法2：只冒泡前10个   
for i in range(11):
    for j in range(11 - 1 - i):
        if dict_list[j][1] > dict_list[j + 1][1]:
            dict_list[j],dict_list[j + 1] = dict_list[j + 1],dict_list[j]
print dict_list
print dict_list[-1:-11:-1]

#字符串格式化format
#左对齐
print 'my name is {name: <5}, my age is {age:<5}'.format(name = 'kk', age = '20')
#右对齐
print 'my name is {name: >5}, my age is {age:>5}'.format(name = 'kk', age = '20')
