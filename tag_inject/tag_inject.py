# program that wraps the php tag around desired content between html tags

import io
import os
import glob
import sys


def it_does_the_thing(the_actual, tag_count, tags, tag_item, tags_close, tags_end, category, close_tag_c_count):
	# makes copy of the string, transfering bits of the string will be a way to keep from replacing a certain string multiple times
	the_copy = the_actual
	the_actual = ''

	# checks and injects for h tag taking the content in the tag and wrapping it in the desired php phrase
	for x in range(tag_count):
		# finding existing php tags to work inside them
		#php_start
		#php_end
		#<hr/>_start
		#<hr/>_end
		
		


		start = the_copy.find(tags[tag_item])
		swrap = the_copy.find(tags_end, start) + 1
		finished = the_copy.find(tags_close[tag_item], swrap)

		# the content within the tags
		tag_innards = the_copy[swrap:finished]
		
		# fixes Quote issues and wraps php tag
		replacement = '<?php _e("' + tag_innards.replace('"', '\\"') + '","' + category + '"); ?>'

		the_copy = the_copy.replace(tag_innards, replacement, 1)

		# Restablish the start and end of the changes to get next document portion
		start = the_copy.find(tags[tag_item])
		swrap = the_copy.find(tags_end, start)
		finished = the_copy.find(tags_close[tag_item], start)

		# actual obtains next portion of edited document
		the_actual += the_copy[0:finished + close_tag_c_count]
		the_copy = the_copy[finished + close_tag_c_count:]

	the_actual += the_copy

	return the_actual


def the_gen():

	# lists files in the directory
	files = os.listdir("../ZZ_files_ZZ/")
	files.sort()

	go_on = False
	# copies the content of the chosen file
	while go_on == False:

		for x in files:
			print x

		try:
			the_file = raw_input("\n\nEnter a file listed below\n"
				"(Reading from /ZZ_files_ZZ/)\n"
				"(Please include file type)\n\n")
			document = open("../ZZ_files_ZZ/" + the_file, 'r')
			the_actual = document.read()
			document.close()
			go_on = True
		except:
			print "\n\nPlease pick a file.\n\n"


	# sets category for php tag
	category = raw_input("\n\nThis is the php tag example...\n\n"
		"		<?php _e('String to be translated.','category'); ?>\n\n"
		"What would you like the category to be?\n\n")

	tags = ['<h', '<p', '<li', '<?php']
	tags_close = ['</h', '</p>', '</li>', '?>']
	tags_end = '>'

	h_count = the_actual.count(tags[0])
	p_count = the_actual.count(tags[1])
	list_count = the_actual.count(tags[2])

	# goes through the function wrapping the php tag around desired content between html tags
	# h tag
	the_actual = it_does_the_thing(the_actual, h_count, tags, 0, tags_close, tags_end, category, 5)
	# p tag
	the_actual = it_does_the_thing(the_actual, p_count, tags, 1, tags_close, tags_end, category, 4)
	# list tag
	the_actual = it_does_the_thing(the_actual, list_count, tags, 2, tags_close, tags_end, category, 5)



	# opens a new file with the same name as the old and writes in the new version
	with io.FileIO("../ZZ_files_ZZ/Results/" + the_file, "w") as creation:
		creation.write(the_actual)
		creation.close()


	print "Task Completed\n"
	"run ---- php -l filename.php ----\n"
	"in the terminal to see if there are any errors\n"





answer = None

while answer != "exit":

	answer = raw_input("\n\nType start to begin.\n\n"
		"	Start\n"
		"	Exit\n\n")
	answer = answer.lower()

	if answer == "start":
		the_gen()

sys.exit()




