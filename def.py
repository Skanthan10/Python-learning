# Write your code here :-)
def sayHello() :
    print ("Hello World!")  # block belonging of function
    #end of function
sayHello() #call the function

def prmax (a,b):
    if a > b:
        #print (a,"is maximum")
        return a
    else :
        #print (b,"is maximum")
        return b
prmax (3,4)
big_number = prmax (3,4)
print ("\n","Max # :",big_number,"\n")

#!/usr/bin/python
#file :using_sys.py
import time  # time is a module, calling using import
print ('The sleep started')
time.sleep(3)  # screen will sleep for 3 sec
print('The sleep finished')

import os
print(os.listdir('.'))  # it will show the Phython program
print(dir(os))    # displays all the function of operation and files.

import time
print (dir(time))

all_files =os.listdir (".")

counts = len(all_files)
print (counts)

for item in all_files:
    #print (item)
    if item.endswith ("py"):    # it will print files end with py
        print (item)


