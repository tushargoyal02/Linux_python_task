#! /usr/bin/python3

# armstrong number are the number whose sum of cube of number forms the same number
# example 153 = 1**3 + 5**3 + 3**3

number=int(input("enter a number:"))
sum1=0
duplicate=number

while duplicate > 0:

	# finding the reminder value of the number
	reminder=duplicate%10
	# collecting all value cube and adding it to check armstrong number
	sum1+=reminder**3

	# taking only the interger value and assigning it
	duplicate//=10

def reverse(a): 
  str = "" 
  for i in a: 
    str = i + str
return str


if number==sum1:
	print("this is a armstrong number:",number)

else:
	print("This is not a armstrong number:",number)
