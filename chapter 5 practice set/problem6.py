# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

# fvtlanguages={
    
# }


# freind1=input("enter your name: ")
# fvtlanguages.update({'freind1'})
# freind2=input("enter your name: ")
# fvtlanguages.update({'freind2'})
# freind3=input("enter your name: ")
# fvtlanguages.update({'freind3'})
# freind4=input("enter your name: ")
# fvtlanguages.update({'freind4'})

# not a correct approach

fvtlanguages={}    

friend1=input('enter your name: ')
language1=input('enter your favorite language: ')

fvtlanguages[friend1]=language1

friend2=input('enter your name: ')
language2=input('enter your favorite language: ')

fvtlanguages[friend2]=language2

friend3=input('enter your name: ')
language3=input('enter your favorite language: ')

fvtlanguages[friend3]=language3

friend4=input('enter your name: ')
language4=input('enter your favorite language: ')

fvtlanguages[friend4]=language4

print(fvtlanguages)


# alternate solution to this is which i was also thinking but syntax was not clear in my mind

fvtlanguages.update({friend1:language1})


