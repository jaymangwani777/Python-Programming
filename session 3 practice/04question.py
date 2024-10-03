# . Replace the double space from problem 3 with single spaces


def has_single_space(test_string):
    # Check for single space in the string
    return ' ' in test_string

# Test string without single space
test_string = "thisstringdonotcontainsanydoublespaceatall"

# Check for single space
if has_single_space(test_string): 
    print("this string contains single spaces")
else:
    print("the string does not contain single spaces")