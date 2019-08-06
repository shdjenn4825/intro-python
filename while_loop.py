"""
Learn conditional Repetition
Two Loops: for loops and while_loops
"""

counter = 5
while counter != 0:
    print(counter)
    # Augmented Operator
    counter -= 1

counter = 5
while counter:
    print(counter)
    # Augmented Operator
    counter -= 1

#Run for ever

while True:
    print("Enter a number")
    responsew = input()     #take user input
    if int("response") % 7 == 0: #number divisible by 7
        break                   #exit loop
print("Outside while loop")