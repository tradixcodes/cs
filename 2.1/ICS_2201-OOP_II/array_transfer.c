#include <stdio.h>
void transfer_array(int arr1[], int arr2[], int n){
    //int n being the number of elements in the array 1
    int i;
    for (i = 0; i < n; i++)
    {
        arr2[i] = arr1[i];
        printf("The number %d of array 2 is: %d\n", i, arr2[i]);
    }
}
void array_max(int arr[], int n) {
    int i, j, temp;

    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap arr[j] and arr[j + 1]
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    // Print the sorted array
   /* for (i = 0; i < k; i++) {
        printf("%d, ", arr[i]);
    }*/
    printf("%d\n", arr[n - 1]);
}

/*void array_sort(int arr[], int k){
    //We'll be using bubble sort
    int i, j, temp;

    for (i = 1; i < k; i++){
        for(j = 0; j < k - 1; j++){
            if(arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                printf("%d, ", arr[j]);
            }
        }
    }
}*/
int main(void)
{
    int myArray1[] = {30, 70, 20, 60, 60, 15};
    int myArray2[7];
    int n = 6;
    // sizeofArray1
    int k = 7;
    // sizeofArray2

    transfer_array(myArray1, myArray2, n);
    myArray2[6] = 120;

    printf("The number 6 of the array 2 is: %d\n", myArray2[6]);
    array_max(myArray2, k);
    return (0);
}