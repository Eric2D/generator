# list files in a directory and writes them to 
import io
import os
import sys


########## ADD ERROR CASE FOR ---- "OSError: [Errno 2] No such file or directory: '~/vagrant/generator/ZZ_files_ZZ'" ----

########################################################
##############							  ##############
##############		program tools		  ##############
##############							  ##############
########################################################


def path_fix(directory):

	# some auto correction for directory path	

	# makes sure there is a backslash at the beginning and end of directory path
	if directory[-1] != '/':
		directory += '/'
	if directory[0] != '/':
		directory = '/' + directory

	try:

		# lists the files
		files = os.listdir(directory)

		# returns a proper directory
		return directory

	except:
		return False



########################################################
##############							  ##############
##############		  main programs	  	  ##############
##############							  ##############
########################################################


def the_gen(start_directory):

	print("working in directory - " + start_directory)

	global scraped_list

	start_directory = path_fix(start_directory)

	if start_directory == False:

		return 1

	else:

		# lists and sorts files in the directory
		directory_list = os.listdir(start_directory)
		directory_list.sort()
		

		scraped_list += [start_directory]

		for x in directory_list:
			

			dir_retrieved = the_gen(start_directory + x)

			if dir_retrieved == 1:
				continue


	# ends the program loop
	return -1



########################################################
##############							  ##############
##############	   program beginning	  ##############
##############							  ##############
########################################################


warning = 0

scraped_list = []

while warning >= 0:

	start_directory = raw_input("Please enter directory to scrape\n\n\n")

	warning = the_gen(start_directory)

	if warning == 1:
		print("Please enter a proper starting directory\n\n\n")


# open file for writing
pen = open("../ZZ_data_ZZ/results.txt", 'w')

# loops for each file in the_data folder
for x in scraped_list:

	# Writes the file name in results folder
	pen.write('\n' + x)



print "\n\nOpen the results.txt file to find the results\n\n"






