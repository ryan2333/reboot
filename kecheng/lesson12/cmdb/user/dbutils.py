#encoding: utf-8

import MySQLdb

import gconf

class MySQLConnection(object):
    def __init__(self, host, port, user, passwd, db, charset='utf8'):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__passwd = passwd
        self.__db = db
        self.__charset = charset
        self.__conn = None
        self.__cur = None
        self.__connect()


    def __connect(self):
        try:
            self.__conn = MySQLdb.connect(host=self.__host, port=self.__port, \
                                        user=self.__user, passwd=self.__passwd, \
                                        db=self.__db, charset=self.__charset)
            self.__cur = self.__conn.cursor()
        except BaseException as e:
            import traceback
            print traceback.format_exc()
            print e

    def execute(self, sql, args=()):
        _cnt = 0
        if self.__cur:
            _cnt = self.__cur.execute(sql, args)
        return _cnt

    def fetchall(self, sql, args=()):
        _cont = 0
        _rt_list = []



        if self.__cur:
            _cnt = self.__cur.execute(sql, args)
            _rt_list = self.__cur.fetchall()
        # _cnt = self.execute(sql, args)
        # if _cnt:
        #     _rt_list = self.__cur.fetchall()
        return _cnt, _rt_list

    def commit(self):
        if self.__conn:
            self.__conn.commit()

    def close(self):
        self.commit()
        if self.__cur:
            self.__cur.close()
            self.__cur = None

        if self.__conn:
            self.__conn.close()
            self.__conn = None


    @classmethod
    def execute_sql(cls, sql, args=(), fetch=True):
        _cnt = 0
        _rt_list = []

        _conn = MySQLConnection(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, \
                               user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD, \
                               db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)

        if fetch:
            _cnt, _rt_list = _conn.fetchall(sql, args)
        else:
            _cnt = _conn.execute(sql, args)
        _conn.close()
        return _cnt, _rt_list


#
def execute_fetch_sql(sql, args=()):
    print args
    return execute_sql(sql, args, True)

def execute_commit_sql(sql, args=()):
    return execute_sql(sql, args, False)

#
def execute_sql(sql, args=(), fetch=True):
    _conn = None
    _cur = None
    _count = 0
    _rt_list = []
    try:
        _conn = MySQLdb.connect(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, \
                        user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD, \
                        db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)

        #_conn.autocommit(True)              #autocommit
        _cur = _conn.cursor()
        _count = _cur.execute(sql, args)
        if fetch:
            _rt_list = _cur.fetchall()
        else:
            _conn.commit()                      #commit, 和autocommit任选其一
    except BaseException as e:
        print e
    finally:
        if _cur:
            _cur.close()
        if _conn:
            _conn.close()
    return _count, _rt_list

def bulker_commit_sql(sql, args_list=[]):
    _conn = None
    _cur = None
    _count = 0
    _rt_list = []
    try:
        _conn = MySQLdb.connect(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, \
                        user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD, \
                        db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)

        #_conn.autocommit(True)              #autocommit
        _cur = _conn.cursor()
        for _args in args_list:
            _count += _cur.execute(sql, _args)
        _conn.commit()                      #commit, 和autocommit任选其一
    except BaseException as e:
        print e
    finally:
        if _cur:
            _cur.close()
        if _conn:
            _conn.close()

    return _count, _rt_list



if __name__ == '__main__':
    conn = MySQLConnection(host=gconf.MYSQL_HOST, port=gconf.MYSQL_PORT, \
                        user=gconf.MYSQL_USER, passwd=gconf.MYSQL_PASSWD, \
                        db=gconf.MYSQL_DB, charset=gconf.MYSQL_CHARSET)

    #print conn.execute_sql('insert into user(username, password, age, phone, age, mail) values(%s, md5(%s), 11, 11012343212, %s)', args=('user6', '123456', 11, '12345632143', 'user6@mail.com'))
