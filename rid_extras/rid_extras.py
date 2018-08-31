# ult_rep replaces selected text in files

import io
import os
import glob
import sys


content = "../ZZ_data_ZZ/content.txt"
results = "../ZZ_data_ZZ/results.txt"

# pulls text from file and stores as lines in a variable
reading = open(content)
text_lines = reading.readlines()
reading.close()
count = 0
filtered = []

print "Filtering - " + content + "\n\n\n"

# filtering process
for x in text_lines:

	count += 1
	print str(count) + ' / ' + str(len(text_lines))

	if x.find('#----#') >= 0:
		filtered += [x]
		continue
		
	if x in filtered:
		continue
	else:
		filtered += [x]

pen = open(results, 'w')
for x in filtered:
	pen.write(x)
pen.close()


print '\n\n\nOpen results.txt file to see your results'


