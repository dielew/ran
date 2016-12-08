#!/usr/bin/env python

from time import sleep
from random import randint, uniform


def dis():
	alpha = "ABCDEFGHIGKLMNOPQRSTUVWXYZ!~!@#$%^&*<>?:"
	
	return alpha[randint(0, len(alpha) - 1)]
	
	
def dis_line():
	mode = ['\033[1;32;40m', '\033[4;32;40m', '\033[5;32;40m', '\033[0;32;40m', '\033[8;32;40m']
	mode_len = len(mode)
	for i in xrange(59):
		line_mode = mode[randint(0, mode_len - 1)]
		print line_mode,dis(),
	
	print '\033[0m'	
		

if __name__ == '__main__':
	
	
	for i in xrange(200):
	
		dis_line()
		sleep(0.05)



'''
	mode = ['\033[1;32;40m', '\033[0;32;40m']
	mode_len = len(mode)
	
	for i in xrange(20):
		line_mode = mode[randint(0, mode_len - 1)]
		for j in xrange(randint(1, 5)):
			print line_mode, dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis(), dis()
			sleep(uniform(0.02, 0.05))
		sleep(uniform(0.02, 0.05))
	print '\033[0m'	
'''
