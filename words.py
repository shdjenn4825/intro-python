"""
get a file from the web:
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

task 1: count number of words in document
"""

from urllib.request import urlopen
# from functions import even_or_odd

file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"


def fetch_words():  #can be fetch_words(filename):
    """
    fetch the words from a file on the web
    :return:
    """
count = 0
data = {}    #empty dictionary
with urlopen(file) as story:
    for line in story:
        words = line.decode('utf-8').split()   #split with space as
        #print(words)
        for word in words:
            #check if key already in dict
            if word in data:
                data[word] += 1
            else:
                data[word] = 1
            count += 1

print("Total number of words", count)
#Sort by key values
for key in sorted(data.keys()):
    print(key, data[key])


def main():
    fetch_words()


if __name__ == '__main__':
    main()
    exit(0)
print("Total data", data)