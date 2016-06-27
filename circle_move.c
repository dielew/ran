#include <stdio.h>
#include <stdlib.h>



int len( char* string )
{
	int len = 0;
	char* str_ptr = string;
	for( ; *str_ptr != '\0'; str_ptr++, len++ ){
		;
	}
	return len;
}


char* str_part_reverse( char* string, int start_offset, int end_offset )
{
	char* ret_ptr = string;
	char* sta_ptr = string + start_offset;
	char* end_ptr = string;
	end_ptr += end_offset;
	char temp;
	int i = start_offset;
	int mid = (end_offset + start_offset) >> 1;
	for( ; i <= mid; i++, sta_ptr++, end_ptr-- ){
		temp = *sta_ptr;
		*sta_ptr = *end_ptr;
		*end_ptr = temp;
	}
	return ret_ptr;	
}


char* str_circular_move( char* string, int leng, int pos )
{
	int offset  = leng - 1;
	char* str_ptr = string;
	str_ptr = str_part_reverse(string, 0, pos - 1);
	str_ptr = str_part_reverse(str_ptr, pos, offset);
	str_ptr = str_part_reverse(str_ptr, 0, offset);
	return str_ptr;
}



int main( int argc, char** argv )
{
	if( argc != 2 ){
		perror("Incorrect argument number(hint: 2): ");
		exit(1);
	}
	char ret[100];
	char* ret_val = ret;
	argv++;
	int leng = len(*argv);
	if( leng <= 1 ){
		perror("Invalid String(hint: len >= 2): ");
		exit(1);
	}
	ret_val = *argv;

	printf("length of string(size n): %d\nEnter size size i:", leng);
	int i_pos;
	scanf("%d", &i_pos);
	if( i_pos > leng || i_pos < 0 ){
		perror("Invalid position index: ");
		exit(1);
	}
	
	ret_val = str_circular_move(ret_val, leng, i_pos);
	printf("moved string: %s\n", ret_val);

	return 0;
}
