# Define function to apply
def square(x):
    return x * x

# Custom map implementation
def map_function(func, input_list):
    result = [] # Intitialize an empty list to store results
    for item in input_list:
        result.append(func(item)) # Apply func to each item and add to result
    return result

# Test the custom map function
num = [1, 2, 3, 4, 5]

#Apply the square function to each element of nums using the custom map
squared_numbers_custom = map_function(square, num)

# Print the results of the custom map function
print("Results using custom map functions: ", squared_numbers_custom)

# Using Python's inbuilt map() function
squared_numbers_builtin = list(map(square, num))

# Print the result from the built-in map function
print("Result using built-in map function: ", squared_numbers_builtin)