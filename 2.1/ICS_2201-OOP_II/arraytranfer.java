public class arraytranfer {
    public static void transferArray(int[] arr1, int[] arr2, int n) {
        for (int i = 0; i < n; i++) {
            arr2[i] = arr1[i];
            System.out.printf("The number %d of array 2 is: %d\n", i, arr2[i]);
        }
    }

    public static void arrayMax(int[] arr, int n) {
        int temp;

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j + 1]
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        // Print the last element of the sorted array
        System.out.println(arr[n - 1]);
    }

    public static void main(String[] args) {
        int[] myArray1 = {30, 70, 20, 60, 60, 15};
        int[] myArray2 = new int[7];
        int n = 6;
        int k = 7;

        transferArray(myArray1, myArray2, n);
        myArray2[6] = 120;

        System.out.printf("The number 6 of array 2 is: %d\n", myArray2[6]);
        arrayMax(myArray2, k);
    }
}
