# Write a program to accept marks of 6 students and display them in a sorted manner.


students=[]

s1=int(input("student1 marks: "))
students.append(s1)
s2=int(input("student2 marks: "))
students.append(s2)
s3=int(input("student3 marks: "))
students.append(s3)
s4=int(input("student4 marks: "))
students.append(s4)
s5=int(input("student5 marks: "))
students.append(s5)
s6=int(input("student6 marks: "))
students.append(s6)

students.sort()
print(students)