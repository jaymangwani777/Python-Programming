# . Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter=( '''
 Dear <|Name|>,
 You are selected!
 <|Date|>
 ''')

print(letter.replace ('<|Name|>', 'Jay').replace('<|Date|>', '27/09/2001') )