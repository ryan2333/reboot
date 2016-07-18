#coding:utf8

import logging
import time, os
from flask import request
import traceback
import requests
import json


logger = logging.getLogger(__name__)

APP_KEY = 'e99a18c428cb38d5f260853678922e03'
APP_SECRET = 'b2332aa78d83be6ba6d2993d5c7ec69d'
def execute_cmd(cmd):
	_fh = os.popen(cmd)
	_cxt = _fh.read().strip()
	_fh.close()
	return _cxt


def get_ip():
    _cmd = "ifconfig eth0 |grep 'inet addr' |awk '{print $2}'"
    _cxt = execute_cmd(_cmd)
    return _cxt.split(':')[-1]


def collect_cpu():
	_cmd = "top -n 1 |grep Cpu |awk '{print $5}' |awk -F% '{print $1}'"
	_cxt = execute_cmd(_cmd)
	return "%.2f" % float(100 - float(_cxt))

def collect_mem():
	_fh = open('/proc/meminfo')
	_total = float(_fh.readline().split()[1])
	_free = float(_fh.readline().split()[1])
	_buffer = float(_fh.readline().split()[1])
	_fh.close()
	return "%.2f" % float(100 - 100 * (_free + _buffer) / _total)

def collect():
	_rt = {}
	_rt['ip'] = get_ip()
	_rt['cpu'] = collect_cpu()
	_rt['mem'] = collect_mem()
	_rt['time'] = time.strftime('%Y-%m-%d %H:%M:%S')
	return _rt

def send(msg):
	try:
		_response = requests.post('http://localhost:9005/performs/', data=json.dumps(msg), headers={'Content-Type':'application/json', 'app_key': APP_KEY, 'app_secret': APP_SECRET})
		if not _response.ok:
			logger.error('error send msg:%s', msg)
		else:
			_json = _response.json()
			if _json.get('code') != 200:
				logger.error('error send msg:%s, result:%s', msg, _json)
	except BaseException as e:
		logger.error(traceback.format_exc())


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(lineno)d %(message)s",
		filename='agent.log')
#	print collect()
	while True:
		_info = collect()
		logger.debug(_info)
		send(_info)
		time.sleep(60)
