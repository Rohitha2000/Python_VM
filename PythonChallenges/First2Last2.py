def string_both_ends(str):
  if len(str) < 2:
    return "cannot create string"

  return str[0:2] + str[-2:]

print(string_both_ends('rohitha'))
print(string_both_ends('ro'))
print(string_both_ends('r'))