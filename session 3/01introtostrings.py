name="jay"
# this is a basic string!
print(len(name))

nameshort =name[0:2]
#start from index 0 all the way till 2 (excluding 2)
charater1 = name[2]
print(charater1)
print(nameshort)

# slicing with skip value

word = "amazing"

wordshort=word[1: 6: 2]
# mzn
print(wordshort)

number=[0,1,2,3,4,5,6,7,8,9,10]

numberskip=number[0:7:2]
# [0:7:2] means first you select how many indexes you want like in this case 0:7 means output will be 0 to 6 0,1,2,3,4,5,6 now we are adding:2 that means the output we got will skip 2 indexes  0 , 2, 4, 6

print(numberskip)