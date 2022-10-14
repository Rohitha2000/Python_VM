def fibonacci(number):
  n1, n2 = 0, 1
  print("Fibonacci Series:", n1, n2, end=" ")
  for i in range(2, number):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
    #if n3== number:
     #   break


number = int(input("enter number "))
fibonacci(number)