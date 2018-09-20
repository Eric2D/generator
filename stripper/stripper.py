# stripper searches through all files in the_data folder and returns a list of results

import io
import os
import sys

def type_1():
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
			pen.write("\n---- Couldn't find ---- " + x)

		if marker != -1 and a_finish != -1:
			# declares the selected phrase
			n_text = text[ a_start : a_finish]
			

			# writes in search and gets rid of the starting white space
			pen.write('\n' + n_text.strip())


	pen.close()

	print "\nOpen the results.txt file and search 'Found' or 'Couldn't find' to quickly check results\n"



def type_2():
	nextc = 1

	opening = open("../ZZ_data_ZZ/content.txt", 'r')
	text = opening.read()
	opening.close

	count = text.count("<a")

	# to check input for an actual number
	while count < 0:
		count = counter(count)

	# open file for writing results
	pen = open("../ZZ_data_ZZ/results.txt", 'w')




	for x in range(count):

		# simple loading stat
		print str(nextc) + ' / ' + str(count)
		nextc += 1

		# Search points and count for a tags
		a_tag = "<a"
		tag_close = ">"
		a_tag_count = text.count(a_tag)

		marker = 0

		for z in range (a_tag_count):

			# search points for href in a tags
			findings = ''
			href_open = 'href="'
			href_close = '"'

			here = None

			# sections off and searches next a tag
			next_tag = text.find(a_tag, marker)
			next_tag_close = text.find(tag_close, next_tag)
			full_a_tag = text[ next_tag : next_tag_close + 1 ]

			# deletes spaces to improve search results
			full_a_tag = full_a_tag.replace(' ', '')

			################### for search of href" ###################
			here = full_a_tag.find(href_open)

			# if no href=" or href=' then skip
			if here == -1:

				################### for search of href' ###################

				# search second case
				href_open = "href='"
				here = full_a_tag.find(href_open)

				# if no proper href is found notify
				if here == -1:
					pen.write('\n' + "---- No href ---- ")
					#sets up for next atag marker
					marker = next_tag + 1
					continue

			# uses coordinates to extract text from a tag
			href_start = text.find(href_open, next_tag)
			text_start = len(href_open) + href_start
			href_end = text.find(href_close , text_start)

			# the text
			findings = text[ text_start : href_end ]

			# case for empty hrefs
			if findings == '':
				pen.write('\n' + "---- Empty a tag ---- ")
				#sets up for next atag marker
				marker = next_tag + 1
				continue

			#sets up for next atag marker
			marker = next_tag + 1

			# writes in search and gets rid of the starting white space
			pen.write('\n' + "Found" + " ---- " + findings.strip())



	pen.close()

	print "\nOpen the results.txt file and search 'Found' or 'Couldn't find' or 'Check text' to quickly check results\n"

def type_3():
	nextc = 1
	marker = 0
	results = []

	# lists and sorts the files
	file_list = os.listdir("../ZZ_files_ZZ/Done/.")
	file_list.sort()


	for x in file_list:

		try:
			x = "../ZZ_files_ZZ/Done/" + x
			results += ["\n\n#----# " + x + " #----#\n\n"]
			opening = open(x, 'r')
			text = opening.read()
			opening.close
		except IOError:
			results += ["\n\n#----#" + x + "#----#\n\n "
			"//// Directory not a file ////\n"]


		# simple loading stat
		print str(nextc) + ' / ' + str(len(file_list))
		nextc += 1

		for y in range(2):
			# Search points and count for a tags
			item = "id='"
			item_close = "'"
			item_count = text.count(item)

			if item_count == 0:
				item = 'id="'
				item_close = '"'
				item_count = text.count(item)

			for z in range(item_count):

				# sections off and searches next a tag
				next_tag = text.find(item, marker)
				after_next = next_tag + len(item)
				next_tag_close = text.find(item_close, after_next)
				stripped = text[ after_next : next_tag_close ]
				text = text.replace(item, '', 1)
				results += [stripped]


	# open file for writing results
	pen = open("../ZZ_data_ZZ/results.txt", 'w')
	for x in results:
		if "#----#" in x:
			pen.write(x + '\n')
			continue

		x = x.replace(' ', '\n')
		pen.write(x + '\n')
	pen.close()

	print "\nOpen the results.txt file and search 'Found' or 'Couldn't find' or 'Check text' to quickly check results\n"

answer = None

while answer != "exit":

	answer = raw_input("Which search type would you like to use?\n\n"
		"	TYPE 1 - Scrape content from all files in a directory\n"
		"	TYPE 2 - Scrape all a tages from content in content.txt file\n"
		"	TYPE 3 - Scrape all classes tages from files in a directory\n"
		"	Exit\n\n")
	answer = answer.lower()

	if answer == "type 1":
		type_1()
	if answer == "type 2":
		type_2()
	if answer == "type 3":
		type_3()

sys.exit()


