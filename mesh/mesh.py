# mesh one word or phrase to a bunch of other phrases

import io
import os
import sys

def the_gen():
	
	try:
		
		# inputs for search requirements
		phrase = raw_input('The phrase to mesh?\n\n')
		count = input('How many times would you like to mesh?\n\n')

		# open file for writing
		pen = open("../ZZ_data_ZZ/results.txt", 'w')

		num = 0
		# loops for each count
		for x in range (count):

			num = num + 1

			input_phrase = raw_input("The phrase to mesh? " + str(num) + "\n\n")

			mesh = pen.write("\n" + phrase + input_phrase)

		pen.close()

	except ValueError:
		print('\n\n\n\nPlease enter a number.\n\n\n\n')
		the_gen()
	except SyntaxError:
		print('\n\n\n\nPlease enter a number.\n\n\n\n')
		the_gen()
	except TypeError:
		print('\n\n\n\nPlease enter a whole number.\n\n\n\n')
		the_gen()
	except NameError:
		print('\n\n\n\nPlease enter a whole number.\n\n\n\n')
		the_gen()


the_gen()

print "\nOpen the results.txt file and search 'Found' or 'Couldn't find' to quickly check results\n"