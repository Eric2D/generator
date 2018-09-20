# Searches queries in a batch of content and displays line of content's first occurance

#####
#####
#####
#####	ADD FEATURE TO DELETE DUPLICATE SEARCH TERMS AND KEEP ONE
#####
#####
#####

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

def search_type_1():

	count = None

	# to check input for an actual number
	while count < 0:
		count = counter(count)
	
	# Opens file content you would like to search and creates a list out of the file lines
	reading = open("../ZZ_data_ZZ/content.txt")
	lines = reading.readlines()
	reading.close()

	# Opens file content you would like to search and copies text to a string.
	# helps for count of search term
	reading2 = open("../ZZ_data_ZZ/content.txt")
	full_text = reading2.read()
	full_text = full_text.lower()
	reading2.close()

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
			word_count = full_text.count(term)

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
			pen.write("\n\nFound //// " + str(x) + " ---- " + str(word_count))
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

# Search one line for one item in mass
def search_type_2():
	count = None

	# to check input for an actual number
	while count < 0:
		count = counter(count)

	# open file for writing
	pen = open("../ZZ_data_ZZ/results.txt", 'w')

	word_list = []
	line_list = []

	# loops for count
	for x in range (count):
		# inputs for search requirements
		word = raw_input('What is the word or phrase? ' + str(x+1) + '\n\n')
		word_list = word_list + [word]

	for x in range (count):
		line = raw_input("What line would you like to search from? " + str(x+1) + '\n\n')
		line_list = line_list + [line]

	for x in range (count):

		# Redefine word and line
		# And change case of word to expand search results
		word = word_list[x]
		word = word.lower()

		line = line_list[x]
		line = line.lower()


		# finds and counts desired content
		a_start = line.find(word)
		word_count = line.count(word)
		word_count = str(word_count)

		if a_start == -1:

			# writes in search
			pen.write('\n' + "Couldn't find ---- " + word_list[x] + " ---- " + line_list[x] + " ---- .")

		if a_start != -1:

			# writes in search
			pen.write('\n' + "Found ---- " + word_list[x] + " ---- " + line_list[x] + " ---- " + word_count)
		
		print "Writing ---- " + str(x)


	pen.close()

	print "\nOpen the results.txt file and search 'Found', 'Couldn't find' or 'Check line' to quickly check results\n"



answer = None

while answer != "exit":

	answer = raw_input("Which search type would you like to use?\n\n"
		"	TYPE 1 - Search content for multiple phrases\n"
		"	TYPE 2 - Search one line for one phrase in mass\n"
		"	Exit\n\n")
	answer = answer.lower()

	if answer == "type 1":
		search_type_1()
	if answer == "type 2":
		search_type_2()

sys.exit()












