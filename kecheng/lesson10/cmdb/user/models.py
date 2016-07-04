#coding: utf-8

from dbutils import MySQLConnection

class User(object):

    def __init__(self, id, username, password, age, phone, email):
        self.id = id
        self.username = username
        self.password = password
        self.age = age
        self.phone = phone
        self.email = email

    '''
    验证用户名和密码
    '''
    @classmethod
    def validate_login(cls, username, password):
        _column = ('id', 'username')
        _sql = 'select id, username from user where username=%s and password = md5(%s)'
        _cnt, _rt_list = MySQLConnection.execute_sql(_sql, (username, password))
        return dict(zip(_column, _rt_list[0])) if _cnt != 0 else None

    @classmethod
    def get_users(cls, wheres=[]):
        _columns = ('id', 'username', 'password', 'age', 'phone', 'email')
        _sql = 'select * from user where 1=1'
        _args = []
        print wheres
        for _key, _value in wheres:
            _sql += ' AND {key} = %s'.format(key=_key)
            _args.append(_value)

        _count, _rt_list = MySQLConnection.execute_sql(_sql, _args)
        _rt = []
        for _line in _rt_list:
            # (6L, u'kk4', u'e10adc3949ba59abbe56e057f20f883e', 29L)
            _rt.append(dict(zip(_columns, _line)))
        return _rt



    @classmethod
    def validate_add_user(cls, username, password, passwordrep, age, phone, email):
        if username.strip() == '':
            return False, u'用户名不能为空'

        # 检查用户名是否重复
        # get_user_by_name()
        if cls.get_user_by_name(username):
            return False, u'用户名已存在'

        # 密码要求长度必须大于等于6
        if len(password) < 6:
            return False, u'密码必须大于等于6'
        if password != passwordrep:
            return False, u'两次输入密码不一致'

        if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:
            return False, u'年龄必须是0到100的数字'

        return True, ''

    '''添加用户信息
    '''
    @classmethod
    def add(cls,username, password, age, phone, email):
        _sql = 'insert into user(username, password, age, phone, email) values(%s, md5(%s), %s, %s, %s)'
        _args = (username, password, age, phone, email)
        MySQLConnection.execute_sql(_sql, _args, False)


    def validate_add2(self, username, password, passwordrep, age, phone, email):
        self.username = username
        self.password = password
        self.passwordrep = passwordrep
        self.age = age
        self.phone = phone
        self.email = email
        if self.username.strip() == '':
            return False, u'用户名不能为空'

        # 检查用户名是否重复
        # get_user_by_name()
        if self.get_user_by_name(self.username):
            return False, u'用户名已存在'

        # 密码要求长度必须大于等于6
        if len(self.password) < 6:
            return False, u'密码必须大于等于6'
        if self.password != self.passwordrep:
            return False, u'两次输入密码不一致'

        if not str(self.age).isdigit() or int(self.age) <= 0 or int(self.age) > 100:
            return False, u'年龄必须是0到100的数字'

        return True, ''

    def save(self):
        _sql = 'insert into user(username, password, age, phone, email) values(%s, md5(%s), %s, %s, %s)'
        _args = (self.username, self.password, self.age, self.phone, self.email)
        MySQLConnection.execute_sql(_sql, _args, False)

    @classmethod
    def get_user_by_name(cls, username):
        _rt = cls.get_users([('username',username)])
        return _rt[0] if len(_rt) > 0 else None


    @classmethod
    def validate_update_user(cls, uid, username, password, age, phone, email):
        if cls.get_users([('id',uid)]) is None:
            return False, u'用户信息不存在'

        if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:
            return False, u'年龄必须是0到100的数字'

        return True, ''

    @classmethod
    def get_user_by_id(cls,uid):
        _rt = cls.get_users([('id', uid)])
        return _rt[0] if len(_rt) > 0 else None

    '''更新用户信息
    '''
    @classmethod
    def update_user(cls,uid, password, age, phone, email):
        _sql = 'update user set password=md5(%s), age=%s, phone=%s, email=%s where id=%s'
        MySQLConnection.execute_sql(_sql, (password, age, phone, email, uid),False)

    @classmethod
    def validate_change_user_password(cls, uid, upasswd, musername, mpasswd):
        if not cls.validate_login(musername, mpasswd):
            return False, '管理员密码错误'

        if cls.get_user_by_id(uid) is None:
            return False, u'用户信息不存在'

        if len(upasswd) < 6:
            return False, u'密码长度必须大于6'

        return True, ''

    @classmethod
    def change_user_password(cls,uid, upassword):
        _sql = 'update user set password=md5(%s) where id=%s'
        MySQLConnection.execute_sql(_sql, (upassword, uid), False)

if __name__ == '__main__':
    print User.validate_login('user1', '123456')
    print User.validate_login('user1', '12345678')