# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

numbers=set()

n1=int(input('enter number 1: '))
numbers.add(n1)
n2=int(input('enter number 2: '))
numbers.add(n2)
n3=int(input('enter number 3: '))
numbers.add(n3)
n4=int(input('enter number 4: '))
numbers.add(n4)
n5=int(input('enter number 5: '))
numbers.add(n5)
n6=int(input('enter number 6: '))
numbers.add(n6)
n7=int(input('enter number 7: '))
numbers.add(n7)
n8=int(input('enter number 8: '))
numbers.add(n8)

print(numbers)