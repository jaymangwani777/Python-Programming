# Write a program to find out whether a given post is talking about “Harry” or not.


post=input('enter your post: ')

post = post.lower()

if('harry' in post):
    print('the post is talking about harry')
else:
    print('the post is not talking about harry')        

    # the in operator checks if the string is substring of other this means if you want to check a perticular name or letter inside the variable you can use in operator