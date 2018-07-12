# web stripper searches through content provided from links  to pull desired content

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
		count = input('How many links would you like to strip from?\n\n')
		return count
	except SyntaxError:
		print 'Please use a number.\n\n'
		return
	except NameError:
		print 'Please use a number.\n\n'
		return




count = None
nextc = 1


# to check input for an actual number
while count < 0:
	count = counter(count)


link_list = []


# open file for writing results
pen = open("../ZZ_data_ZZ/results.txt", 'w')

# write links into a list
for x in range (count):

	link_list += [raw_input("What link would you like to strip from?\n\n")]


for x in link_list:

	link = x

	# simple loading stat
	print str(nextc) + ' / ' + str(count)
	print link
	nextc += 1

	# link check
	try:
		# gathers text from link
		site_text = urllib2.urlopen(link)
		text = site_text.read()
		site_text.close()

	except urllib2.HTTPError as e:
		pen.write("\nCheck link ---- " + str(responses[e.code]))
		continue
	except urllib2.URLError:
		pen.write("\n---- Check link ---- ")
		continue
	except ValueError:
		pen.write("\n---- Check link ---- ")
		continue



	# Search points and count for a tags
	a_tag = "<a"
	tag_close = ">"
	a_tag_count = text.count(a_tag)

	marker = 0

	# seperates link results in results file
	pen.write("\n\n\n\n" + str(a_tag_count) + " #----# " + link + " #----#\n")

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

		# uses coordinates to extract link from a tag
		href_start = text.find(href_open, next_tag)
		link_start = len(href_open) + href_start
		href_end = text.find(href_close , link_start)

		# the link
		findings = text[ link_start : href_end ]

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

print "\nOpen the results.txt file and search 'Found' or 'Couldn't find' or 'Check link' to quickly check results\n"