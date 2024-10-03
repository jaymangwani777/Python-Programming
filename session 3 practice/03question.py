# Write a program to detect double space in a string.

# str="jay is a hot dude"

# print(str.find(" "))

def has_double_space(test_string):
    # Check for double spaces in the string
    return '  ' in test_string

# Test string without double spaces
test_string = "this string do not contains any double space at all"

# Check for double spaces
if has_double_space(test_string): 
    print("this string contains double spaces")
else:
    print("the string does not contain double spaces")
