# Write a program to find the greatest of four numbers entered by the user

n1=int(input("enter number one: "))
n2=int(input("enter number two: "))
n3=int(input("enter number three: "))
n4=int(input("enter number four: "))

if(n1>n2 and n1>n3 and n1>n4):
    print("greatest number is: ",n1)
elif(n2>n1 and n2>n3 and n2>n4):
    print("greatest number is:",n2)
elif(n3>n1 and n3>n2 and n3>n4):
    print("greatest number is: ",n3)
elif(n4>n1 and n4>n2 and n4>n3):
    print('greatest number is: ',n4) 
else:
    print('error')