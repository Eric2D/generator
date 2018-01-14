# ult_rep
import io
import os
import glob
import sys

# Checks if the file exists in the folder
def file_check(file_name):
	try:
		file_name = raw_input("File name to search?\n"
			"Please inclue file type\n\n")
		reading = open(file_name)
		reading.close()
		return file_name

	except IOError:
		print('Please enter an existing file.\n\n')
		file_name = ''
		return file_name


file_name = ''

# loop allowing for resubmit of file name
while file_name == '':
	file_name = file_check(file_name)


reading = open(file_name)

# pulls text from file and stores in a variable
text = reading.read()
reading.close()
print text

######################################################

def the_gen(text):

	editing = open(os.path.join(file_name), 'w')

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
	editing = open(os.path.join(file_name), 'r')
	new_text = editing.read()
	editing.close()
	print new_text
	sys.exit()




the_gen(text)













