# Jatin Patel 2719019 #

import sys

def lexan():
	global mitr
	try: 
	    return (next(mitr))
	except stopIteration: 
	    return('')

def match(ch):
	global lookahead
	if ch == lookahead:
		lookahead = lexan()
	else:
		print("Syntax Errror in Match")
		exit()

def S():
    global lookahead
    if lookahead == 'a'or lookahead == 'd':
        A()
    elif lookahead == 'b' or lookahead == 'c':
        B()
    else:
        print("Syntax error in S")
        exit

def A():
    global lookahead
    match('a')
    if lookahead == 'a':
        A()
    elif lookahead == 'd':
        A2()
        
def A2():
    global lookahead
    match('d')
    if lookahead == 'd':
        A2()
   ## elif lookahead == 'b': # stopIteration errors if not commented out! I don't know how to fix it :( #
       ## B()

        
 
def B():
    global lookahead
    match('b')
    if lookahead == 'b':
        B()
    elif lookahead == 'c':
        B2()
        
def B2():
    global lookahead
    match('c')
    if lookahead == 'c':
        B2()
   ## elif lookahead == 'a': # stopIteration errors if not commented out! I don't know how to fix it :( #
      ##  A()



infile = open(sys.argv[1], "r") # taking in commandline file #
wlist = infile.read().split()
mitr = iter(wlist)
lookahead = lexan()
S()
if lookahead == '':
	print("pass!")
else:
	print("Syntax Error! No end detected!")