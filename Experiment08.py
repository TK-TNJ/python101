# Write a program which accepts a sequence of comma-separated numbers from console 
# and generate a list and a tuple which contains every number. Suppose the following 
# input is supplied to the program: 34, 67, 55, 33, 12, 98. Then, the output should be: 
# ['34', '67', '55', '33', '12', '98'] ('34',67', '55', '33', '12', '98'). Write a Python program that 
# accepts a sequence of comma-separated numbers from the console and generates a list 
# and a tuple containing every number. Display the generated list and tuple, the total 
# number of elements, the first and last elements, and the list in reverse order. 

numbers = input("Enter numbers : ")
my_list = numbers.split(",")
my_tuple = tuple(my_list)
print("List : ", my_list)
print("Tuple : ", my_tuple)
print("Total number of elements : ", len(my_list))
print("First element : ", my_list[0])
print("Last element : ", my_list[-1])
print("List in reverse order : ", my_list[::-1])