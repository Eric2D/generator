# multiple ways to search through the web for content

import io
import os
import sys
import urllib2

# responses for server issues
# siting from source ---- https://docs.python.org/2/howto/urllib2.html
responses = {
		100: ('Continue', 'Request received, please continue'),
		101: ('Switching Protocols',
			 'Switching to new protocol; obey Upgrade header'),

		200: ('OK', 'Request fulfilled, document follows'),
		201: ('Created', 'Document created, URL follows'),
		202: ('Accepted',
					'Request accepted, processing continues off-line'),
		203: ('Non-Authoritative Information', 'Request fulfilled from cache'),
		204: ('No Content', 'Request fulfilled, nothing follows'),
		205: ('Reset Content', 'Clear input form for further input.'),
		206: ('Partial Content', 'Partial content follows.'),

		300: ('Multiple Choices',
					'Object has several resources -- see URI list'),
		301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
		302: ('Found', 'Object moved temporarily -- see URI list'),
		303: ('See Other', 'Object moved -- see Method and URL list'),
		304: ('Not Modified',
					'Document has not changed since given time'),
		305: ('Use Proxy',
					'You must use proxy specified in Location to access this '
					'resource.'),
		307: ('Temporary Redirect',
					'Object moved temporarily -- see URI list'),

		400: ('Bad Request',
					'Bad request syntax or unsupported method'),
		401: ('Unauthorized',
					'No permission -- see authorization schemes'),
		402: ('Payment Required',
					'No payment -- see charging schemes'),
		403: ('Forbidden',
					'Request forbidden -- authorization will not help'),
		404: ('Not Found', 'Nothing matches the given URI'),
		405: ('Method Not Allowed',
					'Specified method is invalid for this server.'),
		406: ('Not Acceptable', 'URI not available in preferred format.'),
		407: ('Proxy Authentication Required', 'You must authenticate with '
					'this proxy before proceeding.'),
		408: ('Request Timeout', 'Request timed out; try again later.'),
		409: ('Conflict', 'Request conflict.'),
		410: ('Gone',
					'URI no longer exists and has been permanently removed.'),
		411: ('Length Required', 'Client must specify Content-Length.'),
		412: ('Precondition Failed', 'Precondition in headers is false.'),
		413: ('Request Entity Too Large', 'Entity is too large.'),
		414: ('Request-URI Too Long', 'URI is too long.'),
		415: ('Unsupported Media Type', 'Entity body in unsupported format.'),
		416: ('Requested Range Not Satisfiable',
					'Cannot satisfy request range.'),
		417: ('Expectation Failed',
					'Expect condition could not be satisfied.'),

		500: ('Internal Server Error', 'Server got itself in trouble'),
		501: ('Not Implemented',
					'Server does not support this operation'),
		502: ('Bad Gateway', 'Invalid responses from another server/proxy.'),
		503: ('Service Unavailable',
					'The server cannot process the request due to a high load'),
		504: ('Gateway Timeout',
					'The gateway server did not receive a timely response'),
		505: ('HTTP Version Not Supported', 'Cannot fulfill request.'),
		}



def counter(count):
	try:
		count = input('How many links would you like to search from?\n\n')
		return count
	except SyntaxError:
		print 'Please use a number.\n\n'
		return
	except NameError:
		print 'Please use a number.\n\n'
		return

# Search multiple links for one phrase
def search_type_1():
	count = None
	load = 0
	link_list = []

	# to check input for an actual number
	while count < 0:
		count = counter(count)

	# inputs for search requirements and makes phrase lowercase
	word = raw_input('What is the word or phrase?\n\n')
	word = word.lower()

	# open file for writing
	pen = open("../ZZ_data_ZZ/results.txt", 'w')

	# loops for each link input
	for x in range (count):

		link_list += [raw_input("What link would you like to search from?\n\n")]

	for x in link_list:
		load += 1
		link = x

		print str(load) + " / " + str(len(link_list))

		try:
			# gathers text from link and makes text lowercase
			site_text = urllib2.urlopen(link)
			text = site_text.read()
			text = text.lower()

			# finds and counts desired content
			a_start = text.find(word)
			counting = text.count(word)
			counting = str(counting)

			if a_start == -1:

				# writes in search and gets rid of the starting white space
				pen.write('\n' + "Couldn't find ---- " + word + " ---- " + link)

			if a_start != -1:

				# writes in search and gets rid of the starting white space
				pen.write('\n' + "Found ---- " + word + " ---- " + link + " ---- " + counting)

		except urllib2.HTTPError as e:
			pen.write("\nCheck link ---- " + link + ' ---- ' + str(responses[e.code]))
		except urllib2.URLError:
			pen.write("\nCheck link ---- " + link)
		except ValueError:
			pen.write("\nCheck link ---- " + link)

	pen.close()

	print "\nOpen the results.txt file and search 'Found', 'Couldn't find' or 'Check link' to quickly check results\n"



# Search multiple links for one phrase
def search_type_2():
	count = None

	# to check input for an actual number
	while count < 0:
		count = counter(count)

	# inputs for search requirements and makes phrase lowercase
	word = raw_input('What is the word or phrase?\n\n')
	word = word.lower()

	# Search markers
	print "What two phrases would you like to search between?\n"
	left_outer = raw_input('What is the left_outer word or phrase?\n\n')
	right_outer = raw_input('What is the right_outer word or phrase?\n\n')

	# open file for writing
	pen = open("../ZZ_data_ZZ/results.txt", 'w')

	# loops for each link input
	for x in range (count):

		link = raw_input("What link would you like to search from?\n\n")

		print link

		try:
			# gathers text from link and makes text lowercase
			site_text = urllib2.urlopen(link)
			text = site_text.read()
			text = text.lower()

			# Finds Markers
			Left_mark = text.find(left_outer)
			right_mark = text.find(right_outer)

			# finds and counts desired content
			a_start = text.find(word, Left_mark, right_mark)
			counting = text.count(word)
			counting = str(counting)

			if a_start == -1:

				# writes in search and gets rid of the starting white space
				pen.write('\n' + "Couldn't find ---- " + word + " ---- " + link)

			if a_start != -1:

				# writes in search and gets rid of the starting white space
				pen.write('\n' + "Found ---- " + word + " ---- " + link + " ---- " + counting)

		except urllib2.HTTPError as e:
			pen.write("\nCheck link ---- " + link + ' ---- ' + str(responses[e.code]))
		except urllib2.URLError:
			pen.write("\nCheck link ---- " + link)
		except ValueError:
			pen.write("\nCheck link ---- " + link)

	pen.close()

	print "\nOpen the results.txt file and search 'Found', 'Couldn't find' or 'Check link' to quickly check results\n"



# Search one link for one item in mass
def search_type_3():
	count = None
	# to check input for an actual number
	while count < 0:
		count = counter(count)

	# open file for writing
	pen = open("../ZZ_data_ZZ/results.txt", 'w')

	word_list = []
	link_list = []

	# loops for each link input
	for x in range (count):
		# inputs for search requirements and makes phrase lowercase
		word = raw_input('What is the word or phrase?\n\n')
		word = word.lower()
		word_list = word_list + [word]

	for x in range (count):
		link = raw_input("What link would you like to search from?\n\n")
		link_list = link_list + [link]

	for x in range (count):
		try:
			# gathers text from link and makes text lowercase
			site_text = urllib2.urlopen(link_list[x])
			text = site_text.read()
			text = text.lower()

			# finds and counts desired content
			a_start = text.find(word_list[x])
			counting = text.count(word_list[x])
			counting = str(counting)

			if a_start == -1:

				# writes in search
				pen.write('\n' + "Couldn't find ---- " + word_list[x] + " ---- " + link_list[x])

			if a_start != -1:

				# writes in search
				pen.write('\n' + "Found ---- " + word_list[x] + " ---- " + link_list[x] + " ---- " + counting)
			
			print "Writing ---- " + str(x + 1) + '/' + str(count)

		except urllib2.HTTPError as e:
			pen.write("\nCheck link ---- " + link_list[x] + ' ---- ' + str(responses[e.code]))
		except urllib2.URLError:
			pen.write("\nCheck link ---- " + link_list[x])
		except ValueError:
			pen.write("\nCheck link ---- " + link_list[x])

	pen.close()

	print "\nOpen the results.txt file and search 'Found', 'Couldn't find' or 'Check link' to quickly check results\n"

answer = None

while answer != "exit":

	answer = raw_input("Which search type would you like to use?\n\n"
		"	TYPE 1 - Search multiple links for one phrase\n"
		"	TYPE 2 - Search multiple links for one phrase between tags\n"
		"	TYPE 3 - Search one link for one item in mass\n"
		"	Exit\n\n")
	answer = answer.lower()

	if answer == "type 1":
		search_type_1()
	if answer == "type 2":
		search_type_2()
	if answer == "type 3":
		search_type_3()

sys.exit()