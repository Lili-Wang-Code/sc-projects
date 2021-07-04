"""
File: anagram.py
Name: Lili Wang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
dictionary = {}


def main():
    """
    First, the user input a word, and this function will find
    all the anagram(s) for the word inputted and terminate when the
    input string matches the EXIT constant defined at line 23.
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        start = time.time()
        read_dictionary()
        if word == EXIT:
            break
        else:
            print('Searching...')
            lst = find_anagrams(word)
            print(str(len(lst)) + ' anagrams: ' + str(lst))
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def find_anagrams(s):
    """
    :param s: str, a word inputted by user
    :return: list, all the anagram(s) for the word
    """
    d = {}  # to count the number of a alphabet in the word and store in the dictionary
    s_d(s, d)
    lst = find_anagrams_helper(s, '', [], d)
    return lst


def find_anagrams_helper(s, current_s, anagrams_list, d):
    """
    :param s: str, a word inputted by user
    :param current_s: str, an empty string to find the anagram
    :param anagrams_list: list, an empty list to store all the anagram(s) for the word
    :param d: dictionary for s, key(alphabet): value(number of the alphabet in a word)
              e.g when user input 'stop': {['s':1], ['t':1], ['o':1],['p':1] }

    :return anagrams_list: all the anagram(s) for the word
    """
    if len(s) == len(current_s) and current_s in dictionary[current_s[0]] and current_s not in anagrams_list:
        print('Found: ' + current_s)
        print('Searching...')
        anagrams_list.append(current_s)
    else:
        for i in range(len(s)):
            ch = s[i]
            if d[ch] > 0:  # discuss with Ilona
                current_s += ch
                d[ch] -= 1
                if len(current_s) == 1 or has_prefix(current_s): # discuss with Ilona(2 conditions written in same line)
                    find_anagrams_helper(s, current_s, anagrams_list, d)
                    current_s = current_s[:len(current_s) - 1]
                    d[ch] += 1
                else:
                    current_s = current_s[:len(current_s)-1]
                    d[ch] += 1
    return anagrams_list


def s_d(str, d):
    """
    :param str: str, the inputted word by user
    :param d: dict, to store the number of a alphabet in the word
    :return: dict, already calculate the number of a alphabet in the word,
            e.g when user input 'stop': {['s':1], ['t':1], ['o':1],['p':1] }
    """
    for i in range(len(str)):
        word = str[i]
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1


def read_dictionary():
    """
    This function reads the dictionary.txt, and will store in a dict.
    the format of the dict: {'a':['a','aa','aah'...],... }
        key: the alphabet from a-z
        value: only stores the word starts with 'key' alphabet

    :return: dict
    """
    if len(dictionary) == 0:
        with open(FILE, 'r') as f:
            for line in f:
                word = line.strip()
                if word[0] not in dictionary:  # discuss with Ilona
                    dictionary[word[0]] = [word]
                else:
                    dictionary[word[0]].append(word)


def has_prefix(sub_s):
    """
    :param sub_s: str, current substring
    :return: bool, whether the word start with sub_s is in the dictionary
    """
    for word in dictionary[sub_s[0]]:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
