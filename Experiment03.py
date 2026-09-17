#Develop a python program to generate Fibonacci series up to n terms using looping statements.

n = int(input("Enter the number of terms : "))
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c