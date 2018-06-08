#!/usr/bin/python
#taking value by user in variable x in string format;
print('Press 1 > To show date and time:')
print('Press 2 > To open up a file:')
print('Press 3 > To make a directory:')
print('Press 4 > To search on google:')
print('Press 5 > To Logout from your sysytem:')
print('Press 6 > To shutdown your os:')
print('Press 7 > To check internet connection on the internet:')
print('Press 8 > To search on google')
print('Press 9 > To show all IP.ADDRESS connented to pc:')
import os
choice=int(raw_input('Enter the work of your choice b/w 1 to7:'))

#Here conditions are checked that what data is been inserted by the user.
if(choice==1):
	import os
	os.system('date')

#Above used import os is used to import date from the OS as it is.
elif(choice==2):
		
	file_name=raw_input('Enter name:')
	os.system('touch '+file_name+' ')
	msg=('Your File has been created by the name, you have provided. Thank for Your Response')
	os.system('echo '+msg+'  | festival --tts') 
	
elif(choice==3):
	z=raw_input('Enter the Name you want to create a folder:')
	os.system('mkdir '+z+' ') 
	print("""Thanks for Working with Us
		YOUR Folder has been created""")
elif(choice==6):
	print('Your system is shutting Down in 10 sec')
	os.system('shutdown -f 10.00')
elif(choice==7):	
	os.system('ifconfig')
elif(choice==9):
	os.system('nmap')
else:
	print('Wrong choice is been made!  Try it again')

