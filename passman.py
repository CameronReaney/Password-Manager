
#--------- Librarys --------- #
from asyncio.base_subprocess import WriteSubprocessPipeProto
from base64 import decode
from doctest import OutputChecker
import re
import operator
import time
import random
#--------- Variables --------- #
strmasterp = "Cameron1"
userpasswordsFile = "userpasswords.txt"
#-----------Functions------------#
def sleeping():
    for i in range(5,0,-1):
        time.sleep(1)
        print(i)
    print("Goodnight!!!")
    quit()
    
#--------------Main--------------#
    
mpass = "Cameron1"
masterPass = input("Enter a Master Password: ")
mode = input("View Or Add a Password?: ")
if mode == "View":
    while masterPass != mpass:
        cmasterP = input("Confirm The Master Password: ")
    else:
        f = open(userpasswordsFile,'r')
        URL = input("Enter the URL of the website: ")
        f = open(userpasswordsFile,'r')
        searchlines = f.readlines()
        for i, line in enumerate(searchlines):
            if URL in line:
                print("Account Found!")
                linerep = line.replace(URL, '')
                print("The Password For", URL , "is" + linerep)
            else:
                print("Sorry no account was found! Sleeping in:")
                sleeping()
if mode == "Add":
    while mpass != masterPass:
        cmasterP = input("Confirm The Master Password: ")
    else:
        
        webName = input("Enter the Name of the website: ")
        webpassword = input("Enter the password for the website: ")
        f = open(userpasswordsFile,"a")
        f.write(webName + " "+ webpassword + "\n")
        
            
            


        


