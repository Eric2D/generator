# ult_rep replaces selected text in files

import io
import os
import glob
import sys


content = "../ZZ_data_ZZ/content.txt"
results = "../ZZ_data_ZZ/results.txt"

reading = open(content)

# pulls text from file and stores in a variable
text = reading.read()
reading.close()
print text

######################################################

def the_gen(text):

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




the_gen(text)













