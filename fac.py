#!/usr/bin/env python
import sys

# this is to yield factorial of each number from 1 to max_fac_num



def factorial( max_fac_num ):
	n = 1
	for i in xrange(1, max_fac_num + 1):
		n *= i
		yield n

if __name__ == '__main__':
	max_num = int(sys.argv[1])
	for num, fac in zip(xrange(1, max_num + 1), factorial(max_num)):
		print 'factorial of %d is %d'%(num, fac)
