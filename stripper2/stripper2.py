# stripper2 mass searches through the content file and reuturns desired search results

import io
import os
import sys

# gathers text content from file
opening = open("../ZZ_data_ZZ/content.txt", 'r')
text = opening.read()
opening.close

def the_gen(text):

	try:

		print text + '\n\n'
		# inputs for search requirements
		fro = raw_input('The beginning of desired content?\n\n')
		to = raw_input('And the word just after the desired phrase?\n\n')
		count = input('How many times would you like to strip from this file?\n\n')

		# open file for writing
		pen = open("../ZZ_data_ZZ/results.txt", 'w')

		# loops for each count
		for x in range (count):

			# finds starting point and end point for desired content
			a_start = text.find(fro)
			a_finish = text.find(to, a_start)

			if a_start == -1 or a_finish == -1:
				pen.write("\nCouldn't find ---- " + search)

			if a_start != -1 and a_finish != -1:

				# declares the selected phrase
				n_text = text[ a_start : a_finish]
				
				# deletes recently searched phrase from workspace so it is not searched again
				text = text.replace(n_text, '', 1)

				# writes in search and gets rid of the starting white space
				pen.write('\n' + n_text.strip())


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

the_gen(text)

print "\nOpen the results.txt file and search 'Found', 'Couldn't find' or 'Check link' to quickly check results\n"