#!/usr/bin/env python
import random
import re


def ext_data_init( input_filename, n_ways, way_size, *temp_filename ):
	input_fd = open(input_filename)
	data_list = []
	for ways in range(n_ways):
		for lines in range(way_size):
			line = input_fd.readline()
			string_rex = re.match('[0-9]+', line)
			data_list.append(int( string_rex.group() ))
			
		write_mem2file(data_list, temp_filename[ways])
		data_list = []

	input_fd.close()
	

def read_file2mem( file_name, size ):
	fr_hand = open(file_name)
	list_temp = []
	for i in xrange(size):
		line = fr_hand.readline()
		string_rex = re.match('[0-9]+', line)
		list_temp.append( int(string_rex.group() ))
	fr_hand.close()
	return list_temp


def write_mem2file( list_in_mem, output_file ):
	fw_hand = open(output_file, 'w')
	list_w = [str(num)+'\n' for num in list_in_mem]
	fw_hand.writelines(list_w)
	fw_hand.close()

def write_mem2output( list_in_mem, output_file ):
	fw_hand = open(output_file, 'a')
	list_w = [str(num)+'\n' for num in list_in_mem]
	fw_hand.writelines(list_w)
	fw_hand.close()

def input_file_read2mem( input_file, way_size, file_pos ):
	fd = open(input_file)
	pos = file_pos
	fd.seek(pos, 0)
	ret_list = []
	line_count = 1
	line = fd.readline()

	while( line != "" and line_count <= way_size ):
		ret_list.append(int(line.rstrip('\n')))
		line_count += 1
		line = fd.readline()

	pos = fd.tell() - len(line)
	fd.close()

	return (ret_list, pos)


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
	
	n_ways = 4;
	way_size = 100000;
	buf_size = 20000;
	src_data_size = 400000
	data_upper = 1000000

	# initialize data, in case when  src_data is ready, this step could be ignored
	list_data = [random.randint(1, data_upper) for i in xrange(src_data_size)]
	write_mem2file(list_data, 'input.txt')
	
	# space allocated for seg data sorting, but 1x more mem space is needed.
	list_space = [0 for i in xrange(way_size)]


	ext_data_init('input.txt', n_ways, way_size, 'file0', 'file1', 'file2', 'file3')
	
	for i in xrange(n_ways):
		file_name = 'file' + str(i)
		lst_2sort = read_file2mem( file_name, way_size )
		merge_sort(lst_2sort, list_space)
		write_mem2file(lst_2sort, file_name)
		list_space = [0 for i in xrange(way_size)]
	
	# initialize seg_input_lists
		
	(list0, posi0) = input_file_read2mem('file0', buf_size, 0) 
	(list1, posi1) = input_file_read2mem('file1', buf_size, 0) 
	(list2, posi2) = input_file_read2mem('file2', buf_size, 0) 
	(list3, posi3) = input_file_read2mem('file3', buf_size, 0) 
	
	lst_input_list = [(list0, posi0), (list1, posi1), (list2, posi2), (list3, posi3)]

	for k in range( src_data_size / buf_size ):
		
		buf_list = []

		for m in xrange(buf_size):
			way_list = [data_upper for k in range(n_ways)]
			for n in xrange(n_ways):
				if len(lst_input_list[n][0]) == 0:
						#continue
					lst_input_list[n][0].append(data_upper)
				else:
					#print n
					way_list[n] = lst_input_list[n][0][0] 

			min_value = min(way_list)
			buf_list.append(min_value)

			for k in xrange(n_ways):
				if min_value == way_list[k]:
					break;
			if min_value in lst_input_list[k][0]:

				lst_input_list[k][0].remove(min_value)
			else:  #when candidate list is empty, the empty list pops 0 value, and it is not in the empyt list 
				pass

			for j in range(n_ways):
				if lst_input_list[j][0] == []:
					lst_input_list[j] = input_file_read2mem('file' + str(j), buf_size, lst_input_list[j][1])		

		write_mem2output(buf_list, 'output.txt')	

	
