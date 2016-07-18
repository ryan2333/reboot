#coding: utf-8

from dbutils import MySQLConnection
import utils, time, ssh_collection
import paramiko

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
        _sql = 'select id, username from user where username=%s and password = %s'
        _cnt, _rt_list = MySQLConnection.execute_sql(_sql, (username, utils.md5_str(password)))
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
        _sql = 'insert into user(username, password, age, phone, email) values(%s, %s, %s, %s, %s)'
        _args = (username, utils.md5_str(password), age, phone, email)
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
        _sql = 'insert into user(username, password, age, phone, email) values(%s, %s, %s, %s, %s)'
        _args = (self.username, utils.md5_str(self.password), self.age, self.phone, self.email)
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
        _sql = 'update user set password=%s, age=%s, phone=%s, email=%s where id=%s'
        MySQLConnection.execute_sql(_sql, (utils.md5_str(password), age, phone, email, uid),False)

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
        _sql = 'update user set password=%s where id=%s'
        MySQLConnection.execute_sql(_sql, (utils.md5_str(upassword), uid), False)

class Assets(object):
    """docstring for Assets"""
    def __init__(self, sn, ip, hostname, os, purchase_date, warranty, vendor, model, idc_id, admin,application, business, cpu, mem, disk,status=0):
        #super(Assets, self).__init__()
        self.sn = sn
        self.ip = ip
        self.hostname = hostname
        self.os = os
        self.purchase_date = purchase_date
        self.warranty = warranty
        self.vendor = vendor
        self.model = model
        self.idc_id = idc_id
        self.admin = admin
        self.business = business
        self.cpu = cpu
        self.mem = mem
        self.disk = disk
        self.status = status


    @classmethod
    def get_by_id(cls,key, value):
        _column = 'id,sn,ip,hostname,os,purchase_date,warranty,vendor,model,idc_id,admin,application,business,cpu,mem,disk'
        _columns = _column.split(',')
        _sql = 'select * from assets where {key}=%s'.format(key=key)
        _cnt, _rt_list = MySQLConnection.execute_sql(_sql, (value,))
        if _cnt !=0:
            return _cnt, dict(zip(_columns,_rt_list[0]))
        else:
            return _cnt, _rt_list


    @classmethod
    def validate_assets_add(cls,sn, ip, hostname, os, purchase_date, warranty, vendor, model, idc_id, admin,application, business, cpu, mem, disk):
        _cnt, _rt_list=cls.get_by_id('sn',sn)
        error = {'error':[]}
        rt = True
        if _cnt:
            error['error'].append('SN号已存在')
            rt = False
            return rt, error
        iplist = ip.split('.')
        if len(iplist) == 4:
            for i in iplist:
                if 0<int(i)<255 and i != '':
                    pass
                else:
                    rt = False
                    error['error'].append('ip地址不符合规范')
        else:
            rt = False
            error['error'].append('ip地址不符合规范')

        if hostname == '' or os == '' or admin == '':
            rt = False
            error['error'].append('主机或操作系统或使用人不能为空')
        if warranty.isdigit() and idc_id.isdigit() and cpu.isdigit() and mem.isdigit() and disk.isdigit():
            pass
        else:
            rt = False
            error['error'].append('保修时长或机房ID或cpu或内存或磁盘不是整数')
        return rt, error
    @classmethod
    def Assets_create(cls,sn, ip, hostname, os, purchase_date, warranty, vendor, model, idcs, admin, application,business, cpu, mem, disk):
        _sql = 'insert into assets(sn, ip, hostname, os, purchase_date, warranty, vendor, model, idc_id, admin, application,business, cpu, mem, disk) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s)'
        args = (sn, ip, hostname, os, purchase_date, warranty, vendor, model, idcs, admin, application,business, cpu, mem, disk)
        MySQLConnection.execute_sql(_sql, args, False)
        return True



class Performs(object):

    @classmethod
    def add(cls, req):
        _ip = req.get('ip')
        _cpu = req.get('cpu')
        _mem = req.get('mem')
        _time =req.get('time')
        _sql = 'insert into performs(ip, cpu, mem, time)values(%s,%s,%s,%s)'
        MySQLConnection.execute_sql(_sql, (_ip, _cpu, _mem, _time), False)


    @classmethod
    def get_list(cls, ip):
        _sql = 'select cpu, mem, time from performs where ip=%s and time >=%s order by time asc'
        _args = (ip, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()-60 * 60)))
        _count, _rt_list = MySQLConnection.execute_sql(_sql, _args)
        datetime_list = []
        cpu_list = []
        mem_list = []
        for _cpu, _mem, _time in _rt_list:
            cpu_list.append(_cpu)
            mem_list.append(_mem)
            datetime_list.append(_time.strftime('%H:%M'))
        return datetime_list, cpu_list, mem_list



    @classmethod
    def validate_execute(cls, musername,mpasswd, ip, port, ruser):
        error = {'error':[]}
        print musername, mpasswd, ip, port, ruser
        rt = True
        if not User.validate_login(musername, mpasswd):
            error['error'].append('administrator password error!!')

        iplist = ip.split('.')
        if len(iplist) == 4:
            for i in iplist:
                if 0<int(i)<255 and i != '':
                    pass
                else:
                    rt = False
                    error['error'].append('ip address is incorrect')
        if not port.isdigit() or not 0 < int(port) <= 65536:
            rt = False
            error['error'].append('port is not between 0 ~ 65535')

        if len(ruser) == 0:
            rt = False
            error['error'].append('login user cant be empty!')

        return rt, error


    @classmethod
    def exectue_cmds(cls, host, username, cmds=[], port=22):
        pkey_file = '/root/.ssh/id_rsa'
        key = paramiko.RSAKey.from_private_key_file(pkey_file)
        _rt_list = ssh_collection.ssh_execute(host, username, cmds=cmds, pkey=key, port=port)
        print _rt_list
        return _rt_list


















if __name__ == '__main__':
    print User.validate_login('user1', '123456')
    print User.validate_login('user1', '12345678')