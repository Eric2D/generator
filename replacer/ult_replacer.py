
import io
import os
import glob
import sys

# ult_rep replaces selected text in files
def replace_type_1():

	content = "../ZZ_data_ZZ/content.txt"
	results = "../ZZ_data_ZZ/results.txt"
	# pulls text from file and stores in a variable
	reading = open(content)
	text = reading.read()
	reading.close()

	editing = open(os.path.join(results), 'w')

	search = raw_input('What would you like to replace?\n\n')

	try:
		times = input('How many times would you like '
			'to make this change?\n\n')
		num = input('How many times per round?\n\n')

		
		# loop for replacement cycles
		for x in range(times):
			x = x + 1
			new_item = raw_input('What would you like to replace '
			'the item with? ' + str(x) + '\n\n')

			text = text.replace(search, new_item, num)

			
	except ValueError:
		print('\n\n\n\nPlease enter a number.\n\n\n\n')
		the_gen(text)
	except SyntaxError:
		print('\n\n\n\nPlease enter a number.\n\n\n\n')
		the_gen(text)
	except TypeError:
		print('\n\n\n\nPlease enter a whole number.\n\n\n\n')
		the_gen(text)
	except NameError:
		print('\n\n\n\nPlease enter a whole number.\n\n\n\n')
		the_gen(text)

	text = editing.write(text)

	editing.close()

	# displays new text with replaced content
	editing = open(os.path.join(results), 'r')
	new_text = editing.read()
	editing.close()
	print 'Open results.txt file to see your results'
	return

def replace_type_2():
	nextc = 1

	opening = open("../ZZ_data_ZZ/content.txt", 'r')
	text_lines = opening.readlines()
	opening.close

	# both old opening and closing tags
	tag = '<' + raw_input("The tag to replace?\n\n")
	tag_specific = tag[tag.find('<') + 1: tag.find(' ')]
	tag_close = "</" + tag_specific + ">"

	# both new opening and closing tags
	new_tag = "<" + raw_input("The new tag?\n\n") + ">"
	new_tag_specific = new_tag[new_tag.find('<') + 1: new_tag.find(' ')]
	new_tag_close = "</" + new_tag_specific + ">"

	# open file for writing results
	pen = open("../ZZ_data_ZZ/results.txt", 'w')
	
	for text in text_lines:

		count = text.count(tag)

		# to check input for an actual number
		while count < 0:
			count = counter(count)

		# Search points and count for tags
		tag_count = text.count(tag)


		for z in range (tag_count):

			# simple loading stat
			print str(nextc) + ' / ' + str(count)
			nextc += 1

			# sections off and searches next tag
			next_tag = text.find(tag)
			next_tag_close = text.find(">", next_tag)
			full_tag = text[ next_tag : next_tag_close + 1 ]

			# deletes spaces to improve search results
			text = text.replace(full_tag, new_tag, 1)
			# replaces tag ending using the curnent tag as a count marker
			text = text.replace(tag_close, new_tag_close, 1)


			# writes in search and gets rid of the starting white space
		pen.write(text)



	pen.close()

	print "\nOpen the results.txt file and search 'Found' or 'Couldn't find' or 'Check text' to quickly check results\n"




answer = None

while answer != "exit":

	answer = raw_input("Which search type would you like to use?\n\n"
		"	TYPE 1 - Replace text in files\n"
		"	TYPE 2 - replace all of an html tag instance with a new one\n"
		"            (Program searches one line at a time)\n"
		"	Exit\n\n")
	answer = answer.lower()

	if answer == "type 1":
		replace_type_1()
	if answer == "type 2":
		replace_type_2()

sys.exit()














