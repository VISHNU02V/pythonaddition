# Addition using functions

def add1(a,b):              # function to add
    s=a+b
    print("The sum of the 2 numbers,",a,"and",b,",is:",s)
ch="y"
while (ch=="y"):
    print("/////   TO ADD 2 NUMBERS   //////")
    a=int(input("Please enter the 1st number::"))
    b=int(input("Please enter the 2nd number::"))
    print("~~~~~~~ SUM OF 2 NUMBER ~~~~~~")
    add1(a,b)
    ch=input("Do you want to continue::")
print("///////THANK YOU///////")