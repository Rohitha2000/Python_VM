import numpy as np

array = np.array([431, 462, 93, 4])

filtering = array > 100

new_array = array[filtering]

print(filtering)
print(new_array)