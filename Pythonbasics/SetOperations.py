a = {1, 2, 3}
b = {"Hello", "Hell", 3}

# Union
print(a | b) # {1, 2, 3, 'Hell', 'Hello'}

# Intersection
print(a & b) # {3}

# Difference (A - B)
print(a - b) # {1, 2}
print(b - a) # {'Hell', 'Hello'}

# Symmetric difference (Opposite of intersection)
print(a ^ b) # {1, 2, 'Hell', 'Hello'}