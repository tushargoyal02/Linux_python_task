#!/usr/local/bin/python3
#Definning the location of Python3 above
#PYTHON PROGRAM FOR FACTORIAL OF A NUMBER
#Defining the factorial_out variable as 1.
factorial_out=1


#Taking the value from a user in the variable fnumber
fnumber=int(raw_input('Enter the number you want to get the factorial:'))
while(fnumber>0 and fnumber>1):
	factorial_out*=fnumber
	#Decremention value of "Fnumber" by -1 in the next step:	
	fnumber-=1
print('The factorial of the given number is:')
print(factorial_out)
