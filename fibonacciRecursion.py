#!/usr/bin/python3

def recursion_func(number):
	if number <=1:
		return number
	else:
		return(recursion_func(number-1) + recursion_func(number-2))


no=int(input("Enter number for fibonacci sequence:"))

if no <= 0:
	print("Enter number greater than 1")
else:
	for i in range(no):
		print(recursion_func(i))


