# Searches queries in a batch of content and displays line of content's first occurance

import io
import os
import sys

def counter(count):
	try:
		count = input('How many phrases would you like to search?\n\n')
		return count
	except SyntaxError:
		print 'Please use a number.\n\n'
		return
	except NameError:
		print 'Please use a number.\n\n'
		return

def the_gen():

	count = None

	# to check input for an actual number
	while count < 0:
		count = counter(count)
	
	# Opens file content you would like to search and creates a list out of the file lines
	reading = open("../ZZ_data_ZZ/content.txt")
	lines = reading.readlines()
	reading.close()

	# open file for writing
	pen = open("../ZZ_data_ZZ/results.txt", 'w')

	term_list = []

	# Adds terms to list
	for x in range(count):
		term_list += [raw_input('What would you like to search for? '
				+ str(x + 1) + '\n\n')]

	content_lines_found = []
	to_remains = []

	num = 0

	# searchs terms by each content's line
	for x in term_list:

		num = num + 1

		# makes term lowercase
		term = x.lower()

		# search for term in content lines
		for y in lines:

			line = y.lower()
			finding = line.find(term)
			counting = line.count(term)

			# conditions for finding term
			if finding != -1:
				no_luck = False
				found_here = y
				break

			if finding == -1:
				no_luck = True
				found_here = "****\n"

		# lines with unfound items will be written
		if no_luck == True:
			pen.write("\n\nCouldn't find //// " + x)
			to_remains = [found_here]

		# Found items will be saved to be written to remains
		if no_luck == False:
			pen.write("\n\nFound //// " + str(x) + " ---- " + str(counting))
			to_remains = [found_here]
		
		content_lines_found += to_remains

	pen.close()


	# Writing found location to remains.txt.
	# good lord please check your content!
	remains = open("../ZZ_data_ZZ/remains.txt", 'w')
	num = 0


	for x in content_lines_found:
		num = num + 1
		remains.write(x)
		print "Writing remains - " + str(num) + " / " + str(len(content_lines_found))

	remains.close()
	sys.exit()

the_gen()

print "\nOpen the results.txt file and search 'Found' or 'Couldn't find' to quickly check "
"results\n\nAnd open remains.txt to see the line of the first instance the content was found\n"













