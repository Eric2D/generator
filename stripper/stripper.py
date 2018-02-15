# stripper searches through all files in the_data folder and returns a list of results

import io
import os
import sys

# lists and sorts the files
files = os.listdir("the_data/.")
files.sort()

# inputs for search requirements
fro = raw_input('Start search for phrase after?\n\n')
to = raw_input('And the word just after the desired phrase?\n\n')

# open file for writing
pen = open("the_results/results.txt", 'w')

# loops for each file in the_data folder
for x in files:

	# prints current file for stripping
	print x

	# gathers text content from file
	opening = open('the_data/' + x, 'r')
	text = opening.read()
	opening.close

	# finds starting point and end point for desired content
	a_start = text.find(fro)
	a_start = a_start + len(fro)
	a_finish = text.find(to, a_start)
	a_finish = a_finish

	# declares the selected phrase
	n_text = text[ a_start : a_finish]
	

	# writes in search and gets rid of the starting white space
	pen.write('\n' + n_text.strip())


pen.close()