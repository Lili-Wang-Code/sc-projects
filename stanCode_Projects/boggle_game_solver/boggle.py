"""
File: boggle.py
Name: Lili Wang
----------------------------------------
This file is a word search game called Boggle.
It will ask the users to input 4 letters for 4 times,
and the goal is to find all the words in these 16 letters.
To search the word, it can find the next letter from its
neighbor(in all directions), and a letter can be only used once in a word.
After searching the word, it will print the word and the total numbers
of the found words.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
dictionary = {}


def main():
	"""
	First, this function will ask the users to input 4 letters
	for 4 times, and search the word from these 16 letters.
	After searching all of the word, it will print the word and
	the total numbers of the found words.
	"""
	input_list = input_row_letters([])
	if len(input_list) == 0:  # wrong format will get an empty list
		print('Illegal input')
	else:
		start = time.time()
		read_dictionary()
		boggle_list = find_boggle(input_list)
		print(f'There are {len(boggle_list)} words in total.')
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_boggle(input_list):
	"""
	:param input_list: (list) stores 4 lists of the inputted words
	:return: (list) all the searched words from input_list
	"""
	boggle_list = []
	for x in range(4):  # vertical  # discuss with Ilona
		for y in range(4):  # horizontal
			boggle_list = find_boggle_helper(x, y, input_list, '', boggle_list, [])
	return boggle_list


def find_boggle_helper(x, y, input_list, current_s, boggle_list, path_list):
	"""
	:param x: (int) the position of the input_list[x]
	:param y: (int) the position of the input_list[x][y]
		the x,y is to find the word so it can search its neighbors

	:param input_list: (list) stores 4 lists of the inputted words
	:param current_s: (str) current search word
	:param boggle_list: (list) the searched words from input_list
	:param path_list: (list) store the number from every word, to make sure a letter only used once

	:return: (list) all the searched words from input_list

	This function is to search the word and to check the word exists in dictionary.
	It can find the next letter from its neighbor(in all directions),
	and a letter can be only used once in a word.
	"""
	if len(current_s) > 3 and current_s in dictionary[current_s[0]] and current_s not in boggle_list:
		print(f'Found \"{current_s}\"')
		boggle_list.append(current_s)
		find_boggle_helper(x, y, input_list, current_s, boggle_list, path_list)
		# keep searching the word in dictionary has longer word
	else:
		num_word = x + y/10  # define the word in input_list a number
		if len(current_s) == 0:  # current_s is an empty string -> new start
			current_s += input_list[x][y]  # first word
			path_list.append(num_word)  # record the path of searching words
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				a = x+i  # vertical
				b = y+j  # horizontal
				num_word = a + b / 10
				if num_word not in path_list:  # whether the word has been searched and in current_s
					if 0 <= a < len(input_list) and 0 <= b < len(input_list):  # whether the word exists
						current_s += input_list[a][b]
						path_list.append(num_word)
						if has_prefix(current_s):
							find_boggle_helper(a, b, input_list, current_s, boggle_list, path_list)
							current_s = current_s[:len(current_s)-1]
							path_list.pop()
						else:
							current_s = current_s[:len(current_s) - 1]
							path_list.pop()
	return boggle_list


def input_row_letters(input_list):
	"""
	:param input_list: (list) an empty list
	:return: (list) stores 4 lists of the inputted word or an empty list

	This function will stores 4 lists of the inputted word, but when
	the inputted words are in illegal format, the input_list will be an
	empty list.
	"""
	illegal_input = False
	for i in range(4):
		letter = input(f'{i+1} row of letters: ')
		letter = letter.lower()
		lst = letter.split()  # makes the input string to become a list
		input_list.append(lst)
		if len(letter) < 7 or len(lst) != 4:
			illegal_input = True
		else:
			for j in range(4):
				word = lst[j]
				if len(word) != 1:
					illegal_input = True
					break
		if illegal_input is True:
			input_list = []
			break
	return input_list


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words that have more than 4 alphabets into a Python dict.
	"""
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if len(word) >= 4:
				if word[0] not in dictionary:  # discuss with Ilona
					dictionary[word[0]] = [word]
				else:
					dictionary[word[0]].append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
