# program that wraps the php tag around desired content between html tags

import io
import os
import glob
import sys


def it_does_the_thing(the_actual, tag_count, tags, bad_tags, tag_item, tags_close, tags_end, category, close_tag_c_count):
	# makes copy of the string, transfering bits of the string will be a way to keep from replacing a certain string multiple times
	the_copy = the_actual
	the_actual = ''

	# checks and injects for h tag taking the content in the tag and wrapping it in the desired php phrase
	for x in range(tag_count):
		# finding existing tags types to ignore
		#php_start
		#php_end
		
		


		start = the_copy.find(tags[tag_item])
		swrap = the_copy.find(tags_end, start) + 1
		finished = the_copy.find(tags_close[tag_item], swrap)

		# for skip situations
		tag_atribute_check = the_copy[start:swrap]
		tag_a_check = the_copy[start:swrap + close_tag_c_count]
		tag_a_closing = the_copy[start:finished + close_tag_c_count]

		# for searching for instance without spaces
		whole_part = the_copy[start:finished]
		nospace_whole_part = whole_part.replace(' ', '')
		nospace_whole_part = whole_part.replace('\n', '')

		# the content within the tags
		tag_innards = the_copy[swrap:finished]

		warning = "****ATTENTION REQUIRED****" + tag_innards
		all_ok = True

		# check to skip if tag is <hr/>
		if tag_atribute_check.find('<hr') != -1:
			all_ok = False

		# check to skip if <a> tag is the only thing inside a tag
		if nospace_whole_part.find(tag_atribute_check + '<a ') != -1:
			if tag_a_closing.find('</a>' + tags_close[tag_item]) != -1:
				all_ok = False
			if tag_a_closing.find('</a> ' + tags_close[tag_item]) != -1:
				all_ok = False

		# makes sure there are no unecessary tags housing tags that cause conflicts
		for x in bad_tags:
			if tag_innards.find(x) != -1:
				all_ok = False


		if all_ok == True:
			# fixes Quote issues and wraps php tag
			replacement = '<?php _e("' + tag_innards.replace('"', '\\"') + '","' + category + '"); ?>'

			the_copy = the_copy.replace(tag_innards, replacement, 1)

		else:
			the_copy = the_copy.replace(tag_innards, warning, 1)

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
		"		<?php _e(\"String to be translated.\",\"category\"); ?>\n\n"
		"What would you like the category to be?\n\n")

	tags = ['<h', '<p', '<li']
	bad_tags = ['<?php', '<ul', '<ol', '<button', '<!--']
	tags_close = ['</h', '</p>', '</li>', '?>']
	tags_end = '>'

	h_count = the_actual.count(tags[0])
	p_count = the_actual.count(tags[1])
	list_count = the_actual.count(tags[2])

	# goes through the function wrapping the php tag around desired content between html tags
	# h tag
	the_actual = it_does_the_thing(the_actual, h_count, tags, bad_tags, 0, tags_close, tags_end, category, 5)
	# p tag
	the_actual = it_does_the_thing(the_actual, p_count, tags, bad_tags, 1, tags_close, tags_end, category, 4)
	# list tag
	the_actual = it_does_the_thing(the_actual, list_count, tags, bad_tags, 2, tags_close, tags_end, category, 5)



	# opens a new file with the same name as the old and writes in the new version
	with io.FileIO("../ZZ_files_ZZ/Results/" + the_file, "w") as creation:
		creation.write(the_actual)
		creation.close()


	print "\n\nTask Completed\n"
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




