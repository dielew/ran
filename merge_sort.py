#!/usr/bin/env python
import random


def merge_sort(listA, listB):
	n = len(listA)
	merge_split(listA, listB, n, 0)

	
def merge_split(listA, listB, end, begin):
	if end - begin < 2:
		return
	else:
		mid = (begin + end) / 2
		merge_split(listA, listB, mid, begin)
		merge_split(listA, listB, end, mid)
		merge(listA, listB, begin, mid, end)
		list_copy(listB, listA, begin, end)


def merge(listA, listB, begin, mid, end):
	
	i = begin;
	j = mid;

	for k in range(begin, end):
		if i < mid and (j >= end or listA[i] <= listA[j]):
			listB[k] = listA[i]
			i += 1
		else:
			listB[k] = listA[j]
			j += 1
	


def list_copy(src, dst, begin, end):
	for k in range(begin, end):
		dst[k] = src[k]


if __name__ == '__main__':
	listA = [random.randint(1, 100) for i in xrange(10)]
	listB = [0 for i in xrange(10)]

	print listA
	merge_sort(listA, listB)

	print listA



