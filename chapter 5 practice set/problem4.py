s = set()
s.add(20)
# (int)
s.add(20.0)
# (float)
s.add('20') # length of s after these operations?
# ('string')

# 20 and 20.0 count as same that's why they both became one element that's why we got 2 as a output

print(s)

print(len(s))