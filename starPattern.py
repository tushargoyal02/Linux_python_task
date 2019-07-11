#!/usr/bin/python3

#Here we will print the * (star) pattern with single for loop

number=int(input("Enter the no of lines for star to be printted:"))

def star(num):

#initializing a variable as 0
	line_star=1

	if num<=0:
		print("Please enter positive number or greater than 0")
	else:
		for i in range(line_star,num+1):
			print("*" * i)
		'''	if i==0:
				print("*")
			else:
				print("*" * i)
		'''
star(number)		
