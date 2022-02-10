#---------------------------------------------------------------------------------------------------------------------------------------

mark="-----------------------------------------------------------------------------------------------------------------------"

print(mark)

details="""
OPERATING SYSTEM MARKET SHARE
"""

defaultpath=('/home/savio/Project/os.csv')


path=input(f"Do you want to use the default csv path? {defaultpath} [y/N] ")   

if path == "y":
    path=defaultpath
elif path == "Y":
    path=defaultpath
else:
    path=input("Enter your path  ")

print(mark)

print(details)

print(mark)

#---------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
#---------------------------------------------------------------------------------------------------------------------------------------


#1.To display the entire csv file
def os():
    df=pd.read_csv(path)
    print(df)
    print()

    print(mark)


# 🔒 Source code hidden 🔒

#---------------------------------------------------------------------------------------------------------------------------------------

#14 Command selector

def selector():
    print()
    print("1  = Display the entire csv file")
    print("2  = Display csv with Date as index")
    print("3  = Display first n or last n Dates")
    print("4  = Display a particular column")
    print("5  = Display a particular row")
    print("6  = Linegraph")
    print("7  = ")
    print("8  = ")
    print("9  = ")
    print("10 = ")
    print("11 = ")
    print("12 = ")
    print("13 = ")
    print("14 = Exit")

    print()
    option=int(input("Enter your choice "))
    print()
    
    if option!=7:
        print(mark)

    print()
    if option==1:
#        os()                #Commented out as source code is hidden 🔒
        return
    elif option==2:
#        index()             #Commented out as source code is hidden 🔒
        return
    elif option==3:
#        head()              #Commented out as source code is hidden 🔒
        return
    elif option==4:
#        column()            #Commented out as source code is hidden 🔒
        return
    elif option==5:
#        rows()              #Commented out as source code is hidden 🔒
        return
    elif option==6:
#        linegraph()         #Commented out as source code is hidden 🔒
        return


    elif option==14:
        print("Goodbye!")
        print()
        exit()
    elif option>14:
        print("INVALID INPUT!")
    elif option<1:
        print("INVALID INPUT!")
    else:
        print("INVALID INPUT!")

#---------------------------------------------------------------------------------------------------------------------------------------


print()
os()


while True:
    selector()

