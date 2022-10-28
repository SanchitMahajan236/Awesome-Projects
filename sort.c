// The idea is to divide the array into two subsets – sorted subset and unsorted subset. Initially, a sorted subset consists of only one first element at index 0. Then for each iteration, insertion sort removes the next element from the unsorted subset, finds the location it belongs within the sorted subset and inserts it there. It repeats until no input elements remain. 

#include <stdio.h>
 

void insertionSort(int arr[], int n)
{

    for (int i = 1; i < n; i++)
    {
        int value = arr[i];
        int j = i;
 

        while (j > 0 && arr[j - 1] > value)
        {
            arr[j] = arr[j - 1];
            j--;
        }
 

 
        arr[j] = value;
    }
}
 

void printArray(int arr[], int n)
{
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
}
 
int main(void)
{
    int arr[] = { 3, 8, 5, 4, 1, 9, -2 };
    int n = sizeof(arr) / sizeof(arr[0]);
 
    insertionSort(arr, n);
 
    // print the sorted array
    printArray(arr, n);
 
    return 0;
}
