#!/usr/bin/env python

from time import sleep

def loading( duration ):
	load_char_arr = r'--\||/--/||\--'
	char_arr_len = len(load_char_arr)
	print "\033[1;30;42m"
	txt = "Module Initializing...                             "

	print ' ' * len(txt)
	print txt
	print ' ' * len(txt)
	# displaying frame
	print "\033[2A\033[?25l"
	# ?25l make cursor disappeared during the loop

	for i in range(0, duration):	
		print "\033[1A\033[43C",load_char_arr[i % char_arr_len]+' '+str(i)+'%'
	# mod caculation of the array index make the loop possible 
		sleep(0.03)
	print "\033[1A\033[43C",' '
	# omitting the dynamic loading symbol after end of loading loop
	print "\033[0m\033[?25h"
	# rolling back to Console ANSI defaults setting

if __name__ == "__main__":
	loading(101)
