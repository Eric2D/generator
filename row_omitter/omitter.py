# Searches unique content and deletes the row containing it

import io
import os
import sys

def counter(count):
	try:
		count = input('How many phrases would you like to omit?\n\n')
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
	
	# Opens file content you would like to search and creates a list
	reading = open("../ZZ_data_ZZ/content.txt")
	lines = reading.readlines()
	reading.close()

	# open file for writing
	pen = open("../ZZ_data_ZZ/results.txt", 'w')

	num = 0

	term_list = []
	checks_balances = []

	# loops for each count making a list of search terms in lowercase
	for x in range (count):

		num = num + 1
		new_term = raw_input("What is the new term? " + str(num) + "\n\n")
		term = [new_term.lower()]
		term_list = term_list + term

	num = 0
	remain_check = 0

	# calls on lines which is a list of each row in the content.txt file
	for x in lines:

		num = num + 1

		# make line lowercase
		content = x.lower()

		# search for term
		for y in term_list:

			finding = content.find(y)

			# conditions for finding term to be deleted
			if finding != -1:
				no_luck = False
				break

			if finding == -1:
				no_luck = True

		# lines with unfound items will be written
		if no_luck == True:
			pen.write(x)

		# Found items will be saved to be written to remains
		if no_luck == False:
			to_remains = [x]
			checks_balances = checks_balances + to_remains
		print "Working - " + str(num) + " / " + str(len(lines))

	pen.close()

	# Writing to remains for the sake of double checking content.
	# good lord please check your content!
	remains = open("../ZZ_data_ZZ/remains.txt", 'w')
	num = 0

	for x in checks_balances:
		num = num + 1
		remains.write(x)
		print "Writing remains - " + str(num) + " / " + str(len(checks_balances))

	remains.close()
	sys.exit()

the_gen()

print "\nOpen the results.txt file and search 'Found' or 'Couldn't find' to quickly check "
"results\nAnd open remains.txt to see the left over content.\n"













