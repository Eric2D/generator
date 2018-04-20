# mesh one word or phrase to a bunch of other phrases in a list or sandwich phrases in a list

import io
import os
import sys

def counter(count):
	try:
		
		count = input('How many times would you like to combine?\n\n')
		return count

	except ValueError:
		print('\n\n\n\nPlease enter a number.\n\n\n\n')
	except SyntaxError:
		print('\n\n\n\nPlease enter a number.\n\n\n\n')
	except TypeError:
		print('\n\n\n\nPlease enter a number.\n\n\n\n')
	except NameError:
		print('\n\n\n\nPlease enter a number.\n\n\n\n')

def the_gen():

	# inputs for search requirements
	phrase = raw_input('The phrase to mesh?\n\n')
	sandwich = raw_input('And to close the sandwich?\n\n')

	# open file for writing
	pen = open("../ZZ_data_ZZ/results.txt", 'w')

	count = 0

	while count <= 0:
		count = counter(count)


	num = 0
	# loops for each count
	for x in range (count):

		num = num + 1

		input_phrase = raw_input("The phrase to mesh? " + str(num) + "\n\n")

		mesh = pen.write("\n" + phrase + input_phrase + sandwich)

	pen.close()

the_gen()

print "\nOpen the results.txt file and search 'Found' or 'Couldn't find' to quickly check results\n"