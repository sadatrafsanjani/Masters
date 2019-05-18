"""
Roll: MIT1926
Name: Mohammad Sadat Hussain Rafsanjani
E-Mal: sadatrafsanjani [at] gmail [dot] com
Website: www.sadatrafsanjani.com


Note: This program targets that the guessed word is at most 10-characters long. 
If the word is larger than that, it won't work.
"""

import  random

# Word List
corpus = ['hack', 'love', 'hate']

# Random index generator
i = random.randint(0, 2)

# Randomly picking a word from list
length = len(corpus[i])
puzzle = corpus[i]

# Player will have at most 10 tries
counter = 10

# Generating the question view
guess = [' * '] * length


while counter > 0:
    
    
    #out = str(guess)[1:-1]
    out = ''.join(str(e) for e in guess)
    
    print("\n", out, "\n")
    
    w = input("Guess a character: ")
    
    if(w in puzzle):
        
        print("You guessed Correct!\n")
        guess[puzzle.find(w)] = w
        
        if not (' * ' in guess):
            print("You have won!")
            break
        
    else:
        print('Oops! Wrong Guess \n')
        
    counter = counter - 1
    
    if(counter > 0 ):
        print("Tries Left: ", counter, '\n')
    else:
        print('You have been Hangged! Bis Bald\n')