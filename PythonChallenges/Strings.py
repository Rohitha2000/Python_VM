Hello_string = "I am AN_Python, and while I can talk, I also Smile!"

# Capitalise the first letter of the string
Hello_string.capitalize()


print(Hello_string.find("Smile"))


print(Hello_string.isalpha())

print(Hello_string.isalnum())


print(Hello_string.isdigit())


len(Hello_string)

# Replace

print(Hello_string.replace("AN_Python", "a Python"))


print(Hello_string.replace("a Python", "AN_Python"))

# Strip away all trailing whitespaces
print(Hello_string.strip())


Hello_string = "I am AN_Python, and while I can talk, I also Smile!" # Let's reset



print(Hello_string.split(","))


space_string = "hello    \nthis is    great"
print(space_string.split())

print("|".join(["1", "2", "3", "4", "5"]))



print("a".zfill(5))