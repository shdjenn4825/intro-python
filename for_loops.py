"""
Practice for loops
keyword: for
"""

cities = ["London", "New York", "Madrid", "Paries", "Ogden"]
#Interate over the collection
for city in cities:
    print(city)

d = {'alice': '801-123-45-898',
     'pedro': '956-445-78-8986',
     'john': '651-123-66-4477'}

# for Iterate over a dictionary
for item in d:
    print(item, "=>", d[item])