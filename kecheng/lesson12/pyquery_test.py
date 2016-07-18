#encoding:utf-8

from pyquery import PyQuery as pyq
import requests





def ip_find(ip):
	url = 'http://ip.chinaz.com/?ip={ip}'.format(ip=ip)
	response = requests.get(url)
	jq = pyq(response.text)
	rt = jq('.IcpMain02').find('.bor-b1s')
	
	spans = rt.find('span')[-1]
	print spans.text


if __name__ == '__main__':
	ip_find('1.1.1.1')