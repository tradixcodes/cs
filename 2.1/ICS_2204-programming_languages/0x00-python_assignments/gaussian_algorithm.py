import numpy as np

def gauss_jordan_elimination(A, B):
    # Augment the matrix A with the column vector B
    augmented_matrix = np.column_stack((A, B))
    
    # Perform Gauss-Jordan elimination
    rows, cols = augmented_matrix.shape
    for i in range(min(rows, cols - 1)):
        # Find the pivot row
        pivot_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        
        # Swap rows
        augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]
        
        # Make the pivot element 1
        augmented_matrix[i] /= augmented_matrix[i, i]
        
        # Eliminate other elements in the current column
        for j in range(rows):
            if i != j:
                augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i]
    
    # Extract the solution from the last column of the augmented matrix
    solution = augmented_matrix[:, -1]
    
    return solution

# Example usage for your system of equations
A = np.array([[1, 2, 1], [2, 7, 8], [0, -2, 2]], dtype=float)
B = np.array([-2, -16, 2], dtype=float)

solution = gauss_jordan_elimination(A, B)
print("Solution:", solution)
