# finding out the number is prime or not

#!/usr/bin/python3

number=int(input("enter a number:"))


if number==1:
	print("number is not prime ",number)

elif number==2:
	print("number is prime ",number)

elif number >0:

	for i in range(2,number):
		if(number%i==0):
			
			print("number is not prime number:",number)
			break
	else:
		print("number is prime:", number)

else:
	print("number is not prime")

