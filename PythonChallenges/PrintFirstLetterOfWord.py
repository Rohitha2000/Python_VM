sentence= "Global warming is a very serious issue which people have been ignoring for a long time"

# Printing first letter of every word int the above sentence.

#splitting words

list= sentence.split(" ")
print(list)
for x in list:
    print(x[0], end= " ")