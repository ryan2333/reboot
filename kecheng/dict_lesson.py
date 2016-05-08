#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
字典:
    定义：{}包含，每个元素都是一个key,value键值对，每个元素也是通过逗号分隔，key==>不可变（字符串、None, tuple,数字，bool类型），唯一，无序
    访问：通过key访问元素，删除元素，修改元素(dict中有存在的key)，添加元素(dict中不存在元素)
    函数：dict(list/tuple(每一个元素是只有两个元素的list/tuple))
        [['kk',28],['woniu', [1,2,3]]]
        in, del, len
    遍历：for user in users:
            print user, users['user']
         for user, value in users.items():
             print user, value
    方法：get:判断key是否存在于字典中，如果在返回值，不在返回默认值 print users.get('c', False)
        copy: user1 = users.copy()  浅拷贝
        clear:清除字典所有元素, users.clear()
        fromkey: 初始化dict,
        dict.fromkeys([1,2,3], [4,5,6])
            {1: [4, 5, 6], 2: [4, 5, 6], 3: [4, 5, 6]}
        has_key: 判断字典是否包含key
        items: 取出字典中所有键值对
        keys： 取出字典中所有键，生成一个列表
        values： 取出字典中所有值，生成一个列表
        pop: dict.pop(k, v):如果key存在，则移除key并返回key的值，如果不存在，则返回指定的默认值，否则报错
        popitems:随出移出字典中一个键值对，并返回键值对组成的元组，如果字典为空，则报错
        update: a.update({'a':20, 'c':25}),向原有字典中更新键值对，如果存在key，则更新值，如果不存在则添加键值 对
        
字符串
文件
'''


dic1 = {'a': 10, 'b': 20, 'c':30}
print dic1
dic1['b'] = 50
dic1['d'] = 100
del dic1['c']
print dic1
print dic1['d']

#生成字典
tuple1 = (('name', 'ryan'), ('scroes', [99,82,90]))
dic2 = dict(tuple1)
print dic2

#打印字典长度
print len(dic2)

#判断key是否在字典中
print 'name' in dic2

#判断值是否在字典中
print 'ryan' in dic2

#遍历：
for i in dic2:
    print i, dic2[i]

for k,v in dic2.items():
    print k, v
    
#获取键===>值，如果不存在返回指定的默认值
print dic2.get('ryan', False)
print dic2.get('name', False)

#传值与传址
dic3 = dic1
dic3['d'] = 50
print dic1
print dic3

#字典复制
dic4 = dic3.copy()
dic4['a'] = 800
print dic3
print dic4

#初始化dict值
dic5 = dict.fromkeys([1,2,3],True)
print dic5

#组合key,value值，并转化为字典
dic6 = dict(zip(['a','b','c'], [4,5,6]))
print dic6
print dic6.keys()
print dic6.values()
print dic6.items()
for k,v in dic6.items():
    print k, '====>', v

#copy功能实现
'''
定义空字典---》遍历原字典---》添加到空字典
'''
dic_old = {'name': 'ryan', 'score': [66, 77, 88, 99], 'sex': 'male'}
dic_new = {}
for k,v in dic_old.items():
    dic_new[k] = v   
print dic_new

#zip
dic7 = dict(zip(dic_old.keys(), dic_old.values()))
print dic7
    
#字符计数方法
read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
#方法1：
dic_count = {}
for x in read_me:
    if not dic_count.has_key(x):
        dic_count[x] = 0
    dic_count[x] += 1
print dic_count

#方法2：
dic_count2 = {}
for x in read_me:
    if x not in dic_count2:
        dic_count2[x] = 0
    dic_count2[x] += 1
print dic_count2

#方法3：
dic_count1 = {}
for x in read_me:
    dic_count1[x] = dic_count1.get(x, 0) +  1
print dic_count1

#方法4：
dic_count3 = {}
for x in read_me:
    dic_count3.setdefault(x, 0)
    dic_count3[x] += 1
print dic_count3

##统计每个学科每个区间的人数：
stus = [
    {'name' : 'kk', 'score' : [61, 72, 80]},
    {'name' : 'kk2', 'score' : [52, 62, 60]},
    {'name' : 'kk3', 'score' : [43, 81, 64]},
    {'name' : 'kk4', 'score' : [64, 75, 65]},
    {'name' : 'kk5', 'score' : [75, 95, 66]},
    {'name' : 'kk6', 'score' : [82, 80, 72]},
    {'name' : 'kk7', 'score' : [61, 72, 90]},
    {'name' : 'kk8', 'score' : [82, 52, 73]},
    {'name' : 'kk9', 'score' : [73, 71, 74]},
    {'name' : 'kk10', 'score' : [64, 95, 85]},
    {'name' : 'kk11', 'score' : [65, 85, 66]},
    {'name' : 'kk12', 'score' : [92, 70, 82]},
]
scores = {}
class_dic = {0: 'math', 1: 'chinese', 2: 'Englist'}
for u in stus:
    for class_type in range(3):
        score_prefix = u['score'][class_type] / 10
        key = (class_dic[class_type], '%s0-%s9' %(score_prefix, score_prefix))
        scores[key] = scores.get(key, 0) + 1
print scores
scores_list = []
for k,v in scores.items():
    scores_list.append(k + (v,))
    #scores_list.append([k[0], k[1], v])

print scores_list

#将key/value值反转
#方法一：
revse_dic = {'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}
revse_new = {}
for k, v in revse_dic.items():
    if not revse_new.has_key(v):
        revse_new[v] = k
    else:
        if isinstance(revse_new[v], list):
            revse_new[v].append(k)
        else:
            revse_new[v]=[revse_new[v],k]
print revse_new

#方法2：
revse_new1 = {}
for k, v in revse_dic.items():
    _rvalue = revse_new1.get(v)
    if _rvalue is None:
        revse_new1[v] = k
    elif isinstance(revse_new1[v], list):
        _rvalue.append(k)
    else:
        revse_new1[v] = [_rvalue, k]
print revse_new1



