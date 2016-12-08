#!/usr/bin/env python

from time import sleep

if __name__ == '__main__':
	
	print "PM 2.5: 100" 
	sleep(0.5)

	for i in range(200, 5000, 100):
		print '\033[7C\033[1A',i
		sleep(0.05)

'''
	print '\033[7C\033[1A',
	sleep(0.5)
	print '\033[7C\033[1A',400
	sleep(0.5)
'''
