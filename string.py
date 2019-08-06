"""
String and Collections

A string is a immutable sequences of Unicode code-points
"""

print('This is a string')
print('This is a string too')

# Concatention and Adjacent Strings
s1 = "First"
s2 = "Second"
print(s1 + s2)

# multi-line Strings and newlines
s3 = """This is 
a multi-line
string"""
print(s3)
s4 = "This is \na multi-line\nstring"
print(s4)

#Support for backslash
s5 = "A\\in a string"
print(s5)

s6 = 'This is "wow"'
print(s6)

#Raw strings
raw_strings =r'C:\User|Documents\Books'
print("raw_string")

#String as sequence
s = "parrot"

#index notation:0,1,2, etc
print("s[4]", s[4], type(s))

#Capitalize the string
print(s,s.capitalize())


