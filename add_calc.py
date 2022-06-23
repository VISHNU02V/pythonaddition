import calclib as fn
d=1
while d!=5:
 print("Menu\n1.ADD\n2.Exit\n")
 d=int(input("Enter the Option : "))
 if d>2:
  x=int(input("Enter the Num1 : "))
  y=int(input("Enter the Num2 : "))
 if d==1:
     fn.add(x,y)
 if d==5:
    print("Abortin...")
