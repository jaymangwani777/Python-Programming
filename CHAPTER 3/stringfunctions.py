str = "harry"
print(len(str)) # Output: 5

str = "harry"
print(str.endswith("rry")) # Output: True

str = "harry"
count = str.count("r")
print(count) # Output: 2
# string.count("c") – counts the total number of occurrences of any character.


str = "harry"
capitalized_string = str.capitalize()
print(capitalized_string) # Output: "Harry"

str = "harry"
index = str.find("rr")
print(index) # Output: 2
# string.find(word) – This function friends a word and returns the index of first
# occurrence of that word in the string

str = "harry"
replaced_string = str.replace("r", "l")
print(replaced_string) # Output: "hally"

# . string.replace (old word, new word ) – This function replace the old word with
# new word in the entire string.
