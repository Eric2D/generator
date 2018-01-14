# ult_search

# ult_rep
import io
import os
import glob
import sys

# Opens file with the content you would like to search through
reading = open("please_find.txt")
text = reading.read()
reading.close()

# displays content you will be searching
print text

######################################################


def the_gen(text):
	# Opens the file where the results will be stored
	results = open(os.path.join("Results.txt"), 'w')

	try:
		times = input('How many items would you like '
			'to search?\n\n')

	
######################################################

		for x in range(times):
			x = x + 1

			# allows input for the word or phrase you would like to search
			search = raw_input('What are you searching? '
				+ str(x) + '\n\n')
			finding = text.find(search)

			# for reporting on findinds in the results file
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

	# For displaying the search results after the code has finished
	results = open(os.path.join("Results.txt"), 'r')
	new_text = results.read()
	results.close()
	print new_text

	sys.exit()


the_gen(text)