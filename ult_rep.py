# ult_rep
import io
import os
import glob
import sys

def file_check(file_name):
	try:
		file_name = raw_input("File name to search?\n"
			"Please inclue file type\n\n")
		reading = open(file_name)
		reading.close()
		return(file_name)

	except IOError:
		print('Please enter an existing file.\n\n')
		sys.exit()


file_name = ''
file_name = file_check(file_name)
reading = open(file_name)
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

	
######################################################

		for x in range(times):
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

	editing.close

	editing = open(os.path.join(file_name), 'r')
	new_text = editing.read()
	editing.close()
	print new_text
	sys.exit()

#######################################################

#	answer = raw_input('Would you like to replace in the same '
#		'file?\n yes\n no\n\n')

#	if answer == 'yes':
#		the_gen(text)
#	if answer == 'no':
#		return(text)
#		sys.exit()
#	else:
#		print ('Please pick one of the options.\n\n')

#	return(text)



the_gen(text)













