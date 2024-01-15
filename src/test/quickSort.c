#include <stdio.h>
int array[1001];


int partition(int left, int right) {
    int pivot = array[right];
    int i = (left - 1);
    int j;

    for (j = left; j < right; j = j+1) {
        if (array[j] <= pivot) {
            i = i + 1;
            int temp2 = array[i];
            array[i] = array[j];
            array[j] = temp2;
        }
    }
    int temp1 = array[i + 1];
    array[i + 1] = array[right];
    array[right] = temp1;
    return (i + 1);
}

void quickSort(int left, int right) {
    if (left < right) {
        int pi = partition(left, right);

        quickSort(left, pi - 1);
        quickSort(pi + 1, right);
    }
    return;
}

void printArray(int InputArray) {
    int i = 0;
    for (i = 0; i < InputArray; i = i + 1) {
        printf("%d ", array[i]);
    }
    return;
}

int main(){
    printf("Input the length of the string:");
    int InputArray;
	scanf("%d",&InputArray);
	printf("Please input the array to be sorted:");
	int i,j,t;
	for(i = 0; i < InputArray; i = i + 1)
	{
		scanf("%d",&array[i]);
	}
	int temp = InputArray - 1;
	quickSort(0,temp);

	printArray(InputArray);
	return 0;
}
