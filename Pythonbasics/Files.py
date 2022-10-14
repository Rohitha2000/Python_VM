import os
f = open("demo.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demo.txt", "r")
print(f.read())
f.close()


if os.path.exists("demo.txt"):
  os.remove("demo.txt")
  print("File has been removed")
else:
  print("The file does not exist")