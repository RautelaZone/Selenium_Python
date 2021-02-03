import numpy as np

arr = np.array([1, 2, 8, 4, 5])
value = 9

absolute_val_array = np.abs(arr - value)
print(absolute_val_array)
smallest_difference_index = absolute_val_array.argmin()
print(smallest_difference_index)
closest_element = arr[smallest_difference_index]

print("Closest element to" ,value, "is", closest_element)