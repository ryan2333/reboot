#coding:utf-8

class Animail(object):
    atype = 'dog'
    @classmethod
    def run(cls):
        print cls.atype, ' running'

print Animail.atype
Animail.run()

animal = Animail()
print animal.atype

animal.atype = 'big'
animal.run()
print animal.atype

class Utils(object):
    @staticmethod
    def md5(text):
        return 'ssddsfsadfsdf'


print Utils.md5('sadfasdkf;sadf')


class anal(object):
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def get_name(self):
        return  self.__name

anl = anal('ww', 5)

print anl.age
print anl.get_name()

class dog(Animail):
    def run(self):
        print 'asdfasdfasd'

dd = dog()

dd.run()


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print self.name + ' is saying'

    def run(self):
        print self.name + ' is running'


class Dog(Animal):
    def __init__(self, name, age, variety):
        super(Dog, self).__init__(name, age)
        self.variety = variety

    def run(self):

        print self.variety ,self.name ,' running'

dd = Dog('hh', 1, 'hsq')

dd.run()
print dd.age


class Test(object):
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def aa(self):
    print self.name, self.age

df = Test('ww',11)
df.aa()
