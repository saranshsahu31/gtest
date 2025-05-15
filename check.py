import numpy as np

def sum_numbers(numbers):
    # Convert input to numpy array and calculate sum
    arr = np.array(numbers)
    return np.sum(arr)

def mul_numbers(numbers):
    # Convert input to numpy array and calculate product
    arr = np.array(numbers)
    return np.prod(arr)

if __name__ == "__main__":
    # Example usage
    test_numbers = [1, 2, 3, 4, 5]
    result = sum_numbers(test_numbers)
    print(f"Sum of numbers {test_numbers} is: {result}")
    
    # Example with floating point numbers
    float_numbers = [1.5, 2.7, 3.2, 4.1]
    float_result = sum_numbers(float_numbers)
    print(f"Sum of numbers {float_numbers} is: {float_result}")
