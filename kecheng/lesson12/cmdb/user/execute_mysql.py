#coding:utf8

import MySQLdb

import gconf


def execute_sql(sql, args=(), fetch=True):
    _conn = None
    _cur = None
    _count = 0
    _rt_list = []
    try:''
                _conn = MySQLdb.connect(host='10.13.3.12', port=3306, \
                        user='cmdbuser', passwd='homelinkcmdb', \
                        db='cmdb', charset='utf8')

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



    if __name__ == '__main__':
        sql = 'insert into table() value()'
        args = ()
        execute_sql(sql, args, False)




