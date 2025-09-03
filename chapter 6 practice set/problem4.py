# Write a program to find whether a given username contains less than 10
# characters or not.

username=input("enter your username: ",)

if(len(username)>=10):
    print('username is correct')
else:
    print('username should atleast have 10 characters')