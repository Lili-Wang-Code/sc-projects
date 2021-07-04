"""
File: hangman.py
Name: Lili Wang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    Users sees a dashed word, trying to correctly figure the un-dashed word out
    by inputting one character each round.
    If the user input is correct, show the updated word on console.
    Any number or punctuation mark is illegal format of the input.
    Players have N_TURNS chances to try and win this game.
    """
    w = random_word()  # get a random word
    n = first(w)  # let the word to become the dashes
    print('The word looks like: ' + n)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    t = N_TURNS  # the number of the guesses
    while True:
        ans = ''
        g = input('Your guess: ')
        g = g.upper()
        if len(g) != 1:  # the guess alphabet is not 1 alphabet
            print('illegal format.')
        elif g.isalpha() is False:  # the guess alphabet is not alphabet
            print('illegal format.')
        elif g in w:  # the guess alphabet is in the random word
            for i in range(len(w)):  # where is the position of the guess alphabet
                ch1 = w[i]  # random word
                ch2 = n[i]  # word with dashes
                if g in ch1:  # replace dash with the guess alphabet
                    ans += g
                else:  # keep the same word from the word with dashes
                    ans += ch2
            n = ans  # a word with dashes and the guess alphabets
            print('You are correct!')
            if '-' not in n:  # whether all of the dashes are replaced by the guess word
                print('You win!!\nThe word was: ' + w)
                break
            print('The word looks like: ' + n)
            print('You have ' + str(t) + ' guesses left.')
        else:  # the input is not in the random word
            print('There is no ' + g + '\'s in the word.')
            t -= 1  # decrease the guess times
            if t == 0:   # whether the turn of guess is 0
                print('You are completely hung :(')
                print('The word was: ' + w)
                break
            print('The word looks like: ' + n)
            print('You have ' + str(t) + ' guesses left.')


def first(w):
    """
    to count how many alphabets are there from a random word,
    and let form of the word to become dashes.
    :return: dashes(----)
    """
    ans = ''
    for i in range(len(w)):
        ans += '-'
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
