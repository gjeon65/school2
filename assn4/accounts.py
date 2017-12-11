#!/usr/bin/python

"""
Geun Jeon
CS265-002
Assignment 4
2017-12-12
"""

import os
import sys
import math
import random
from types import *
from collections import OrderedDict
"""
globals
"""
account_array=[] #for all of log data
account_array_sorted=[] #for sorting account data
account_array_info = [] #for information account data
account_array_hist = [] #for history account data
account_data = [] #sorted all log data
account_data_info = [] #to show only a unique account ID and name
account_data_bal = [] # to show balance in information()
sorted_ID = None #for sorting id
total=0 #For calculating total balance
        

def openfile():
        
    """
    opening text.txt file

    and assign values to globals
    """
    global sorted_ID
    log = open("text.txt", "r+")
    logData = log.readlines()
        
        
    for i in range(0,len(logData)):
        acc = [(logData[i])]
        account_array_sorted.extend(acc)
    sorted_ID = (sorted(set(account_array_sorted)))
        
    for line in sorted_ID:
        line = line.strip()
        logData_sorted = line.split(":")
                
        """
        account_data[0].append(accID)  
        account_data[1].append(accName)    
        account_data[2].append(accDate)
        account_data[3].append(accTran)    
        account_data[4].append(accBal)
        """
        accID = int(logData_sorted[0])
        accName = logData_sorted[1]
        accDate = logData_sorted[2]
        accTran = logData_sorted[3]
        accBal = logData_sorted[4]

        account_array_info = [accName,accID]
        account_array = [accName, accID, accDate, accTran, accBal]
        
        global account_data, account_data_info, account_data_bal
        

        if account_array not in account_data:
            account_data.append(account_array)
       
        if account_array_info not in account_data_info:
            account_data_info.append(account_array_info)


def calc(task):
    
    accN=[]
    global total, account_data_info
    for s in sorted_ID:
        s = s.strip()
        accInfo = s.split(':')
        accID = int(accInfo[0])
        match = account_data_info[int(task)-1][1]
    
        if match == accID:
            accN.append(s)
            
            for i in accN:
                accInfo2 = i.split(':')
                if accInfo2[3] == "D":
                    total += float(accInfo[4])
                else:
                    total -= float(accInfo[4])

    print(" account#: ", account_data_info[int(task)-1][1])
    print("     name: ", account_data_info[int(task)-1][0])
    print("  balance: $",total)
    information()
        
        
        
"""
Display information of account(s)

"""

def information():
    i=0
    
    print("information")
    print("-----------")
    for i in range(0, len(account_data_info)):
        print(i+1,account_data_info[i])
    print("q for exit")
    task = raw_input("Enter choice: ")        
    try:
        if task == "q":
            sys.exit()
        elif task != "q":
            selected = int(task)-1
            #print(account_data_info[selected])
            calc(task)
            
                

            
            
    except IndexError:
        print("Wrong input. Try again")
        information()
        

def history():
    print("History")
    print("-------")
         
def main():
    
    openfile()
    print("Use -i for input")
    print("Use -h for history")
    print("Use -t for transaction")
    print("Use -q to quit")
    task = raw_input("What do you want to do? ")
    print("You inputed ",task)
        
    if task == "-i":
        print("You have selected information")
        information()
    elif task== "-h":
        print("You have selected history")
        history()
    elif task == "-q":
        sys.exit()
    elif task != "-i" or "-t" or "-h" or "-q":
        print("Wrong input try again.")
        main()
    #print("in main: ",account_data_info)

        
main()
    


