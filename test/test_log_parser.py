from netaddr import *
import pytest
import re

def is_found(line, addr, isCIDR):
	# get ip string at each line if available
	ip_str = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line).group(0)
	if ip_str != "":
		print(ip_str)
		ip = IPAddress(ip_str)
		if isCIDR:
			return ip in addr
		return ip == addr
	return False
	pass


def test_is_found_true():
	line = '180.76.15.17 - - [02/Jun/2015:17:20:23 -0700] "GET /logs/access_141026.log HTTP/1.1" 200 45768 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"'
	addr = IPAddress('180.76.15.17')
	assert is_found(line, addr, False) == True

def test_is_found_true_cidr():
	line = '180.76.15.17 - - [02/Jun/2015:17:20:23 -0700] "GET /logs/access_141026.log HTTP/1.1" 200 45768 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"'
	addr = IPNetwork('180.76.15.0/24')
	assert is_found(line, addr, True) == True

def test_is_found_false():
	line = '180.76.15.17 - - [02/Jun/2015:17:20:23 -0700] "GET /logs/access_141026.log HTTP/1.1" 200 45768 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"'
	addr = IPAddress('180.76.15.18')
	assert is_found(line, addr, False) == False

def test_is_found_false_cidr():
	line = '180.76.15.17 - - [02/Jun/2015:17:20:23 -0700] "GET /logs/access_141026.log HTTP/1.1" 200 45768 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"'
	addr = IPNetwork('180.76.16.0/24')
	assert is_found(line, addr, True) == False