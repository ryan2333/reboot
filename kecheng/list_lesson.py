#!/usr/bin/env python
#_*_coding:utf-8_*_
#判断用户名是否在列表中
 
names = ['woniu', 'wd', 'kk']
name = raw_input('print your name:')
 
status = False
for i in names:
    if i == name:
        status = True
        break
 
if status:
    print "yes"
else:
    print 'false'
  
names = ['a','b','c','c','d','a','a','b','c','c','d','a','a','b','c','c','d','a']
 
str1 = raw_input('Enter a letter:')
num = 0
for i in names:
    if i == str1:
        num += 1
print "The letter %s found %d times" % (str1, names.count(str1))
 
#队列：先进先出
seq1 = []
while True:
    str1 = raw_input("Enter action(add,do,exit):")
    if str1 == 'add':
        str2 = raw_input("Enter something:")
        seq1.append(str2)
    elif str1 == 'do':
        if len(seq1) != 0:  #if seq1
            print "work:",seq1.pop(0),"finished!!"
        else:
            print "no work to do"
    elif str1 == 'exit':
        if len(seq1) == 0: #if not seq1
            print "work is finished, exit"
            break
        else:
            print "work is not finished,please continue"
    else:
        print 'enter incorrect!!'
 
#堆栈：先进后出
seq1 = []
while True:
    str1 = raw_input("Enter action(add,do,exit):")
    if str1 == 'add':
        str2 = raw_input("Enter something:")
        seq1.append(str2)
    elif str1 == 'do':
        if len(seq1) != 0:  #if seq1
            print "work:",seq1.pop(),"finished!!"
        else:
            print "no work to do"
    elif str1 == 'exit':
        if len(seq1) == 0: #if not seq1
            print "work is finished, exit"
            break
        else:
            print "work is not finished,please continue"
    else:
        print 'enter incorrect!!'   
         
#列表反转
list1 = range(10)
for i in range(len(list1)/2):
    list1[i],list1[-1 - i] = list1[-1 - i], list1[i]
  
#冒泡
cnt = 0
heigh = ['160', '163', '155', '176', '175', '188', '170']
for i in range(len(heigh)-1):
    for j in range(len(heigh) - 1 - i): 
        cnt +=1  
        if heigh[j] > heigh[j + 1]:
            heigh[j], heigh[j+1] = heigh[j+1],heigh[j]
    print "第%s次排序后结果为：\n%s" %(i, heigh)
print cnt   
print "排序后的列表为:%s" %(heigh)
 
#列表去重,求共同的值
n1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
n3 = [2,1,3,2,43,234,454,452,234,14,21,14]
n2 = []
for i in n1:
    if i not in n2 and i in n3:
        n2.append(i)
print n2


 


