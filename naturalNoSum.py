#! /usr/bin/python3

# finding the sum of natural number here

number=int(input("enter natural number:"))

sum1=0

# checking conditions whether a number is positive or negative
if number<=0:
	print("Please enter a postive number greater than zero [0]!")
else:
	while number>=0:
	
		# calculating the sum of numbers
		sum1+=number

		#print(sum1)
		# reducing the number by 1
		number -= 1


print("Sum of natural numbers are:",sum1)
