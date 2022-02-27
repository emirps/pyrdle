import random
import enchant
import os
import sys
with open("words.txt") as file:
    lines=file.readlines()
    lines = [line.rstrip() for line in lines]
acceptables = ['']
d=enchant.Dict("en_US")
def wordeval(word, guess):
    global result
    result=''
    i=0
    if len(guess) != 5:
        g()
    if guess == word:
        print('You won in '+str(t)+' guesses!')
        exit()
    for x in range(len(guess)):
        if guess[x] == word[x]:
            result+=" ! "
        elif guess[x] not in list(word):
            result+=" / "
        else:
            result+=" ? "


    print(result)
alphabet='abcdefghijklmnopqrstuvwxyz'
alphabet=alphabet.upper()
alphabet=list(alphabet)
for line in lines:
    if len(line) == 5:
        if line.isalpha() == True:
            acceptables.append(line)
        else:
            continue
    else:
        continue
wordle=random.choice(acceptables)
wordle=wordle.upper()
global t
t=0
def g():
    global t
    elmnts=''
    guess=''
    guess=input('Guess: ')
    if guess == "GIVEMETHEWORD!":
        print(wordle)
    if d.check(guess) == False:
        print('This word is not recognized.')
        guess=''
        g()
    guess=guess.upper()
    for char in list(guess):
        if char not in alphabet:
            print('Character '+char+' is invalid.')
            g()
    if len(guess) == 5 and d.check(guess) == True:
        wordeval(wordle, guess)
        for char in list(guess):
            elmnts+=' '+char+' '
        print('')
        print(elmnts)
        print('')
        t+=1
while t<6:
    g()
if t==6:
    print("You've reached 6 guesses.")
    print('The word was '+wordle)
    exit()
