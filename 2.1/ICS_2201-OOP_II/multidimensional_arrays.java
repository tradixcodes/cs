public class multidimensional_arrays {
    public static void main(String[] args) {
        // Create a 2D array
        int[][] matrix = new int[3][3];

        // Populate the matrix with elements
        int value = 1;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                matrix[i][j] = value;
                value++;
            }
        }

        // Display the original matrix
        System.out.println("Original Matrix:");
        printMatrix(matrix);

        // Add elements to a specific row (e.g., row 1)
        int[] elementsToAdd = {10, 11, 12};
        matrix[1] = elementsToAdd;

        // Display the updated matrix
        System.out.println("\nMatrix after adding elements to row 1:");
        printMatrix(matrix);
    }

    // Helper method to print a 2D matrix
    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}
