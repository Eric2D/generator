# stripper searches through all files in the_data folder and returns a list of results

import io
import os
import sys

# lists and sorts the files
files = os.listdir("../ZZ_files_ZZ/.")
files.sort()

# inputs for search requirements
fro = raw_input('Start search for phrase after?\n\n')
to = raw_input('And the word just after the desired phrase?\n\n')

# open file for writing
pen = open("../ZZ_data_ZZ/results.txt", 'w')

# loops for each file in the_data folder
for x in files:

	# prints current file for stripping
	print x

	# gathers text content from file
	opening = open('../ZZ_files_ZZ/' + x, 'r')
	text = opening.read()
	opening.close

	# finds starting point and end point for desired content
	marker = text.find(fro)
	a_start = marker + len(fro)
	a_finish = text.find(to, a_start)


	if marker == -1 or a_finish == -1:
		pen.write("\n---- Couldn't find ---- ")

	if marker != -1 and a_finish != -1:
		# declares the selected phrase
		n_text = text[ a_start : a_finish]
		

		# writes in search and gets rid of the starting white space
		pen.write('\n' + n_text.strip())


pen.close()

print "\nOpen the results.txt file and search 'Found', 'Couldn't find' or 'Check link' to quickly check results\n"