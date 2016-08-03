#include <stdio.h>
#include <stdlib.h>
#include <time.h>





void  rand_generator( size_t size, int ran_max, int* array )
{
	int* array_ptr = array;
	int i;
	for( i = 0; i < size; i++ )
	{
		*(array_ptr + i) = (int)( ((double)rand() / RAND_MAX) * ran_max );
	}
}

void swap( int* a, int* b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

void qu_sort( int* arr, int hi, int lo)
{
	int pivot_pos;
	if( lo < hi	)
	{
		pivot_pos = partition(arr, hi, lo);
		qu_sort(arr, pivot_pos, lo);
		qu_sort(arr, hi, pivot_pos + 1);
	}
	else{
		return;
	}
}

int partition( int* arr, int hi, int lo )
{
	int pivot = arr[lo];
	int i = lo;
	int j = hi;
	
	while(i < j)
	{
		while(i < j && arr[j] >= pivot)
		{
			j--;
		}
		if(i < j){
			swap(&(arr[i]), &(arr[j]));
			i++;
		}
		while(i < j && arr[i] <= pivot)
		{
			i++;
		}
		if(i < j){
			swap(&(arr[i]), &(arr[j]));
			j--;
		}
	}
	return j;
}



int main( void )
{

	size_t size = 10000;
	int arr[size];

	srand((unsigned int)(time(0)));
	rand_generator( size, 100000, arr);
	
	int i;
	int* arr_ptr = arr;
	for( i = 0; i < size; i++ )
	{
		printf("%d\n", *(arr_ptr + i));
	}

	printf("\n\n");

	qu_sort(arr_ptr, size - 1 ,0);

	for( i = 0; i < size; i++ )
	{
		printf("%d\n", *(arr_ptr + i));
	}

	return 0;

}
