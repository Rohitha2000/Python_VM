
txt= "rohi'tha'"
print(txt)

# checking if word is present in a sentence

sentence= "Python is a popular programming language"
word1= "language"
if word1 in sentence:
    print("language present in sentence")
else:
    print("not present")

if 'game' in sentence:
    print("language present in sentence")
else:
    print("not present")

print(len(word1))

# slicing words
print(sentence[2:6])
print(sentence[:5])

b = "Hello, World!"
print(b[-5:-2])

# ignoring capital letters or case sensitive
w1= "HEllo"
w2= "hello"
if(w1.casefold() == w2.casefold()):
    print("case not sensitive")
else:
    print("case sensitive")

str= "rohitha"

print("Replaced string ", str.replace("tha", "rohi"))

# splitting sentence into words
print(sentence.split(" "))

# escape chars
txt = "We are the so-called \"Vikings\" from the north."
print(txt)