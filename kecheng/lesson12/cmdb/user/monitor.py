#encoding: utf-8

from dbutils import MySQLConnection
import logging, datetime
from mailutils import sendemail
import assets

logger = logging.getLogger(__name__)
CNT = 3
CPU_PERCENT = 25
MEM_PERCENT = 80
ALARM_RECIVERS = ['543551194@qq.com']

def has_alarm(ip):
	_sql = 'select cpu, mem from performs where ip = %s and time >=%s order by time desc limit %s'	
	_time = datetime.datetime.now() - datetime.timedelta(minutes=5)
	_args = (ip, _time.strftime('%Y-%m-%d %H:%M:%S'), CNT)
	_rt_cnt, _rt_list = MySQLConnection.execute_sql(_sql, _args)
	if _rt_cnt < CNT:
		return False, False
	_cpu_alarm  = True
	_mem_alarm = True

	for cpu, mem in _rt_list:
		if cpu < CPU_PERCENT:
			_cpu_alarm = False

		if mem < MEM_PERCENT:
			_mem_alarm = False

	return _cpu_alarm, _mem_alarm


def monitor():
	_assets_list  = assets.get_list()
	_title = 'cpu & mem warning'
	for _assets in _assets_list:
		ip = _assets['ip']
		_cpu_alarm, _mem_alarm = has_alarm(ip)
		_content_list = ['主机{ip}告警'.format(ip=ip)]
		if _cpu_alarm:
			_content_list.append('CPU连续{cnt}次超过{percent}%'.format(cnt=CNT, percent=CPU_PERCENT))
		if _mem_alarm:
			_content_list.append('MEM连续{cnt}次超过{percent}%'.format(cnt=CNT, percent=MEM_PERCENT))
	if len(_content_list) >= 2:
		sendemail(ALARM_RECIVERS, _title, ','.join(_content_list))
		logger.info('send mail to:%s, title:%s, msg:%s',ALARM_RECIVERS, _title, ','.join(_content_list) )


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(lineno)d %(message)s",
		filename='monitor.log')
	monitor()