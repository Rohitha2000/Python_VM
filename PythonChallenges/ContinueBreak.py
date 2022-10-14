num_list = [1, 2, 3, 4, 5]

for x in num_list:
    print(x, end=" ")
    if x == 2:
        continue
    print("Check!", end=" ")


for x in num_list:
    print(x, end=" ")
    if x == 2:
        break
    print("Check!", end=" ")