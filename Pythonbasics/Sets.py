example_set = {1, 2, 3}


example_set.add(3)
example_set.add(4)


example_set.update([5, 6, 7])


example_set.update([5, 6, 7], {6, 7, 8})

# Remove a value
example_set.remove(8)


# Discard will not throw an error if the argument is not in the set
# Remove will

example_set.discard(8)


example_set.pop()


example_set.clear()