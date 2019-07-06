#!/usr/bin/python3


# calling function

def recursion_func(number):

	# if number is 1 return that number
	if number <=1:
		return number

	# if number is greater than 1 call functin with the value as down
	else:
		return(recursion_func(number-1) + recursion_func(number-2))


# input number by user
no=int(input("Enter number for fibonacci sequence:"))

# check condition if number is negative print message
if no <= 0:
	print("Enter number greater than 1")


# if above condition is false provide value to the function in loop
else:
	for i in range(no):
		print(recursion_func(i))


