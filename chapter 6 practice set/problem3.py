# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams

comment= input('enter your comment: ')

if('make a lot of money'or'buy now'or'subscribe this'or'click this' in comment):
    print('spam comment against user policies')
else:
    print('thanks for your comment')

# the in operator checks that the given string is the substring of other or not
