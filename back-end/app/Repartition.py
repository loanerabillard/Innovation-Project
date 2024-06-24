import numpy as np

def generate_matrix(num_matches):
    # Generate indices
    x = np.linspace(0, 1, num_matches)
    
    # First column: Half Gaussian (highest to lowest)
    col1 = np.exp(-x**2 / 0.5)  # Using 0.2 to adjust the spread
    col1 = col1 / col1.sum() * 100  # Scale to sum to 100
    
    # Second column: Gaussian (low, high, low)
    col2 = np.exp(-((x - 0.5) ** 2) / 0.5)  # Centered around 0.5
    col2 = col2 / col2.sum() * 100  # Scale to sum to 100
    
    # Third column: Half Gaussian (lowest to highest)
    col3 = np.exp(-x[::-1]**2 / 0.5)  # Using 0.2 to adjust the spread, reversed x
    col3 = col3 / col3.sum() * 100  # Scale to sum to 100
    
    # Combine columns
    matrix = np.vstack((col1, col2, col3)).T
    
    # Convert to list of lists
    matrix_list = matrix.tolist()
    
    return matrix_list

def calculate_repartition(dict_array):
    num_matches = len(dict_array)
    matrix = generate_matrix(num_matches)
    
    for i in range(num_matches):
        dict_array[i]['repartition'] = [
            round(matrix[i, 0], 2),
            round(matrix[i, 1], 2),
            round(matrix[i, 2], 2)
        ]
    
    return dict_array