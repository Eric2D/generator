# stripper

import io
import os
import sys


files = os.listdir("the_data/.")

fro = raw_input('Start search after?\n\n')
to = raw_input('And the word just after the section?\n\n')

# open file for writing
pen = open("the_results/results.txt", 'w')

# loops for each file in the_data folder
for x in files:

	# gathers text from file
	opening = open('the_data/' + x, 'r')
	text = opening.read()
	opening.close

	a_start = text.find(fro)
	a_start = a_start + len(fro)
	a_finish = text.find(to, a_start)
	a_finish = a_finish

	# declares the selected word and gets rid of the starting white space
	n_text = text[ a_start : a_finish]
	

	# writes in search 
	pen.write('\n' + n_text.strip())


pen.close()