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
from random import randint
from types import *
from collections import OrderedDict
import time
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
raw_ID = None #for raw input
total=0 #For calculating total balance
today=(time.strftime("%y.%m.%d"))#To get today's date in year.month.day
ACCT_LIST = []*5 #for exporting
account_array_rewrite = [] #for saving changes
"""
Deposit or Withdraw
-------------------

any changes are saving into ACCT_LIST and sample.log file
I am not sure, if you wanted to change text.txt 
"""
def depOrWith(getAccNum,getAccNam):
    print("This is ",getAccNum," for ", getAccNam)
    global ACCT_LIST,account_data_info, today
    print("\n","Deposit or Withdraw: \n")
    print("d for deposit")
    print("w for withdraw")
    print("q for exit")
    print("m for main")
    print("--------------")
    tranInput = raw_input("Enter choice: ")
   
    try:
        if tranInput == "q":
            sys.exit()
        elif tranInput =="d":
            
            deposit = float(input("Enter amount: "))

            
            ACCT_LIST.append("%s:%s:%s:%s:%s" %(getAccNum, getAccNam, today,"D", deposit))
            
            print("Deposit Successful")
            print("To see changes, go to main menu and use -d option")
            transaction()
        elif tranInput =="w":
            ACCT_LIST=[]
            withdraw = float(input("Enter amount: "))
            ACCT_LIST.append("%s:%s:%s:%s:%s" %(getAccNum, getAccNam, today,"W", withdraw))
            
            print("Withdrew Successful")
            print("To see changes, go to main menu and use -d option")
            transaction()
                
        elif tranInput =="m":
            main()
        else:
            print("Try again.")
            transaction()
            
                 
                
    except IndexError:
        
        transaction()
                
"""
Creating account
----------------
saves new account to ACCT_LIST
"""
def createAcc():
    print("\nCreating account ")
    print("-----------------")
    global ACCT_LIST,account_data_info, today

    name = raw_input("What is your full name? ")
    money = float(raw_input("you have to deposit X amount of money: $"))
    accID = randint(1000,9999)

    if accID not in account_data_info:
        ACCT_LIST.append("%s:%s:%s:%s:%s\n" %(accID, name, today, "D",money))
        print("Following is added",ACCT_LIST)
        main()
    
def transaction():
    global sorted_ID, raw_ID
    getAccNum=0
    getAccNam=""
    print('\n')
    print('transaction')
    print('-----------')
    for i in range(0, len(account_data_info)):
        print(i+1,account_data_info[i])
    print("n for new account")
    print("q for exit")
    print("m for main menu")
    task = raw_input("Enter choice: ")
    try:
        if task == "q":
            sys.exit()
        elif task == "n":
            createAcc()
        elif task == "m":
            main()
        elif task != 'q':
            for s in sorted_ID:
                s = s.strip()
                accInfo = s.split(':')
                accID = int(accInfo[0])
                match = account_data_info[int(task)-1][1]
                namMatch = account_data_info[int(task)-1][0]
                getAccNum = match
                getAccNam = namMatch
            depOrWith(getAccNum,getAccNam)
        else:
            print("Wrong Input. Try again.")
            transaction()
            

            
    except IndexError:
        print("Wrong input. Try again.")
        transaction()

def openfile():
        
    """
    opening text.txt file

    and assign values to globals
    """
    global sorted_ID, raw_ID, account_array_rewrite
    log = open("text.txt", "r+")
    logData = log.readlines()
        
        
    for i in range(0,len(logData)):
        acc = [(logData[i])]
        account_array_sorted.extend(acc)
    sorted_ID = (sorted(set(account_array_sorted)))
    raw_ID = account_array_sorted
        
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
        account_array_rewrite = [accID, accName, accDate, accTran, accBal]
        account_array_info = [accName,accID]
        account_array = [accName, accID, accDate, accTran, accBal]
        
        global account_data, account_data_info, account_data_bal
        

        if account_array not in account_data:
            account_data.append(account_array)
       
        if account_array_info not in account_data_info:
            account_data_info.append(account_array_info)

"""
Calculating total balance of an account
"""
def calc(task):
    print("\n")
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
    print("\n")
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
            
            calc(task)

            
    except IndexError:
        print("Wrong input. Try again")
        information()
        

    
        
"""
check history of account(s)

"""
def history():
    print("\n")
    print("History")
    print("-------")
    global account_data_info, raw_ID
    for i in range(0, len(account_data_info)):
        print(i+1,account_data_info[i])
    print("q for exit")
    task = raw_input("Enter choice: ")
    print("\n")
    try:
        if task == "q":
            sys.exit()
        elif task != "q":
            selected = int(task)-1
            
            accN=[]
            
            for s in raw_ID:
                s=s.strip()
                accInfo = s.split(':')
                accID = int(accInfo[0])
                match = account_data_info[int(task)-1][1]
                if match==accID:
                    accN.append(s)
                    
            for i in accN:
                
                accInfo2 = i.split(':')
                if accInfo2[3] == "D":
                    
                    print(accInfo2[2]," Deposit ", accInfo2[4])
                    
                else:
                    print(accInfo2[2]," Withdraw ", accInfo2[4])
                            
            
            history()
            

    except IndexError:
        print("Wrong input. Try again.")
        history()


"""
main function calls out options for tasks

"""
def main():
    global ACCT_LIST
    openfile()
    print("Use -i for input")
    print("Use -h for history")
    print("Use -t for transaction")
    print("Use -? for usage message")
    print("Use -q to quit")
    print("Use -d for save changes in ACCT_LIST and generate sample.log")
    
    task = raw_input("What do you want to do? ")
    print("You inputed ",task)
        
    if task == "-i":
        print("You have selected information")
        information()
    elif task== "-h":
        print("You have selected history")
        history()
    elif task == "-t":
        transaction()
    elif task == "-q":
        sys.exit()
    elif task =="-?":
        print("Just running a program will prompt you options")
        print("after program started, type -i for information")
        print("-h for history, -t for transaction")
        print("-q for quit")
        sys.exit()
    elif task == "-d":
        
        for i in range(0, len(ACCT_LIST)):
            print(ACCT_LIST[i])
            with open("sample.log", "w") as output:
                
                for i in range(0,len(ACCT_LIST)):
                    output.write(str(ACCT_LIST[i]))
                    output.write('\n')
            
    elif task != "-i" or "-t" or "-h" or "-q" or "-d":
        print("Wrong input try again.")
        main()
    
            
main()
    


