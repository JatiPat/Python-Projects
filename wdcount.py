# Jatin Patel 2719019 #

import sys

infile = open(sys.argv[1], "r") # taking in commandline file #
diffcount = 0
totalcount = 0 #setting up word counts #

wdcount = {} #setting up dictionary #

for w in infile.read().split():  #taking in each word by splitting them using spaces #
    w = w.lower()
    totalcount += 1
    if w not in wdcount: # if w is not in the dictionary, add to dictionary and increase count. Else just increase old word #
        wdcount[w] = 1
        diffcount += 1
    else:
        wdcount[w] += 1  
	      

print("Words that are bigger than 4 letters and end with 'in' are...")

for w in sorted(wdcount, key=wdcount.get, reverse= True): #printing out the words that end with 'in' and bigger than 4 letters#
    if len(w) > 4 and w.endswith('in'):
        print(w,wdcount[w])

print(f"Different word count: {diffcount}") # printing up word counts #
print(f"Total word count: {totalcount}")