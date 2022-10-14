def squares(dict):
    for i in dict:
        dict[i]= i*i

dict={
    2:0,
    3:0,
    5:0,
    8:0,
    12:0
}
squares(dict)
print(dict)