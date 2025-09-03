# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# marks=100

# subject1=int(input('enter your marks of english: '))
# subject2=int(input('enter your marks of maths: '))
# subject3=int(input('enter your marks of reasoning: '))

# if(subject1>=40% marks and subject2>=40% marks and subject3>=40% marks):
#     print('you are pass')
# else:
#     print('you are fail')   

# this was my approach there are few mistakes




subject1=int(input('enter your marks of english: '))
subject2=int(input('enter your marks of maths: '))
subject3=int(input('enter your marks of reasoning: '))

# check for total percentage

total_percentage= (100*(subject1+subject2+subject3)/300) 

# if(subject1<33 or subject2<33 or subject3<33):
#     print('you are fail')


if(total_percentage>=40 and subject1>=33 and subject2>=33 and subject3>=33): 
    print('you are pass',total_percentage)  
else:
    print('you failed',total_percentage)    