"""
Learn dictionaries
Dictionaries maps keys to values

In some languages are knows as associateive arrays, or hashes, maps

Creat them using{} continuing a key-value pair

Creat them {} continuing a key-value pair
Restrieve them by [key_value}
"""

d = {'alice':'801-123-45-898',
     'pedro':'956-445-78-8986',
     'john': '651-123-66-4477'}
print(d, type(d))

#Acces one element
print(d['pedro'])

#Add members to the dictionary, of names_> grades
roster = {}   # Empty dictionary
total = 0
while total < 3:
    #get key value
    name = input("Enter your name")
    #get value associated to key
    score = input("Enter score")

    #add element to dictionary
    #note: If key value exist, it will update the value
    #  otherwise it will be add it to the dict.
    total +=1
#Print dictionary
print(roster)
