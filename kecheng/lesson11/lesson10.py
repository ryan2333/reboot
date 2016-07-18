#coding:utf8
import os
import sys
import argparse
import hashlib
import logging

logger = logging.getLogger(__name__)

def getfile(dirpath):
	rt_list = []
	if os.path.isdir(dirpath):
		if len(os.listdir(dirpath)) != 0:
			for name in os.listdir(dirpath):
				rpath = dirpath + '/' + name
				if os.path.isdir(rpath):
					rt_list.extend(getfile(rpath))
				else:
					rt_list.append(rpath)
		else:
			rt_list.append(dirpath)
	return rt_list

def md5_str(value):
	_md5 = hashlib.md5()
	_md5.update(value)
	return _md5.hexdigest()

if __name__ == '__main__':
	# argvs = sys.argv
	# print sys.argv
	# if len(argvs) > 1:
	# 	print getfile(argvs[1]) 
	# else:
	# 	print 'argvs  error'
	# 	sys.exit(-1)
	# _parser = argparse.ArgumentParser()
	# _parser.add_argument('-d', '--filename', help="directory name", type=str, default='Desktop')
	# _parser.add_argument('-C', '--cmds', help="excute cmd", nargs='+', default=[])
	# args = _parser.parse_args()
	# print args
	# if args.filename is None:
	# 	print _parser.print_help()
	# 	sys.exit(-1)
	# print getfile(args.filename)

	# if len(args.cmds) == 0:
	# 	print _parser.print_help()
	# 	sys.exit(-1)
	# print args
	#print md5_str('pip123')
	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(pathname)s %(levelname)s %(module)s %(lineno)d %(relativeCreated)d",
		filename='log.txt')
	logger.debug('i am debug')
	logger.info('i am info')
	logger.error('i am error')
