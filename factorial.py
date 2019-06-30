#!/usr/bin/python3

number=int(input("enter number for factorial:"))
factorial=1

#checking if value is less than zero
if number<0:
	print("no factorial found")


# if number is 1 or 0
elif number==1 or number==0:
	print("factorial of number:", 1)


# if number is greater than zero
else:
	for i in range(1,number+1):
		#print(i)
		factorial=factorial*i

	print("factorial of number:",factorial)


