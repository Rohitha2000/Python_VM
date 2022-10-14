num:int = 33
print(num)
print(type(num))

num= "rohi"
print(num)
print(type(num))

# global variables
global text
text= "global"
def fun():
    text = "local"
    print(text)

print("outside {0}, calling function {1}".format(text, fun()))
print()
