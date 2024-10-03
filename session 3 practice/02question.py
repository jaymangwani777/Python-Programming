# Write a program to fill in a letter template given below with name and date.

# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date'''

# print(letter.replace("<|Name|>","Jay").replace("<|Date","27 september 2024"))

Name = input("Enter the name of the candidate: ")
date = input("Enter the date of selection: ")

print(f"Dear {Name},\n\nYou are selected!\n\nDate: {date}")
