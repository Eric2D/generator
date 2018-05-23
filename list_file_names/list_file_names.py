# list files in a directory and writes them to 
import io
import os
import sys


########## ADD ERROR CASE FOR ---- "OSError: [Errno 2] No such file or directory: '~/vagrant/generator/ZZ_files_ZZ'" ----



# lists and sorts the files
files = os.listdir(raw_input('\n\nWhat is the file directory?\n\n'))
files.sort()

# open file for writing
pen = open("../ZZ_data_ZZ/results.txt", 'w')

# loops for each file in the_data folder
for x in files:

	# Writes the file name in results folder
	pen.write('\n' + x)

print "\nOpen the results.txt file to find the results"