Python_list = ["Hello", "Rar", "Hell"]

# Appending
Python_list.append("Rar")
Python_list.append("Pop_Me")

# Extending
number_list = [1, 2, 3]
extend_list = [4, 5]
number_list.append(extend_list)
number_list.extend(extend_list)

Python_list.pop()


# Inserting into an index
Python_list.insert(1, "Rrr")


# Removing
Python_list.remove("Rrr")


# Delete an item
del Python_list[3]


Python_list.count("Rar")


Python_list.sort() # Sort!
Python_list.reverse() # Reverses order of list



# Return length of list
len(Python_list)

# Return maximum (alphanumerically)
max(Python_list)

# Return minimum (alphanumerically)
min(Python_list)

# Sum all values in the list
#sum(Python_list)


set([1,1,1,1,1,2])

# Find index of a list element
Python_list.index("Hello")
print(Python_list)
