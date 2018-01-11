# ult_search

# ult_rep
import io
import os
import glob
import sys

def file_check(file_name):
	try:
		file_name = "please_find.txt"
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

	results = open(os.path.join("Results.txt"), 'w')

	try:
		times = input('How many items would you like '
			'to search?\n\n')

	
######################################################

		for x in range(times):
			x = x + 1
			search = raw_input('What are you searching? '
				+ str(x) + '\n\n')
			finding = text.find(search)

			if finding == -1:
				results.write("\n\nCouldn't find ---- " + search)
			else:
				results.write("\n\nFound ---- " + search)

			
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

	

	results.close

	results = open(os.path.join("Results.txt"), 'r')
	new_text = results.read()
	results.close()
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