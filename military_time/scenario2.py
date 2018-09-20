# scenario 2

import io
import os
import glob
import sys

def scen2(search, results):

	num_set1 = ['1','2','3','4','5','6','7','8','9','10','11','12']

	am_time = ['1:00','2:00','3:00','4:00','5:00','6:00','7:00',
		'8:00','9:00','10:00','11:00','00:00']

	pm_time = ['13:00','14:00','15:00','16:00','17:00','18:00','19:00',
		'20:00','21:00','22:00','23:00','12:00']

	# strips white space for time variable and makes all letters lower case
	# creating number string variable
	num_search = search.lower()
	count_space = num_search.count(' ')
	num_search = num_search.replace(' ', '', count_space)

	# establish am and pm on right and left side + first center marker
	center_marker = num_search.find('-')
	left_am = search.find('am', 0, center_marker)
	right_am = search.find('am', center_marker)

	# strip am and pm away for simple conversion
	num_search = num_search.replace('pm','', 2)
	num_search = num_search.replace('am', '', 2)

	# set search markers
	center_marker = num_search.find('-')

	# right and left side
	left_hour = num_search[ : center_marker ]
	right_hour = num_search[ center_marker + 1 : ]

	try:
		# for left side of time
		# AM
		if left_am != -1:
			for x in range(12):

				if left_hour == num_set1[x]:
					first = am_time[x]

		# PM
		if left_am == -1:
			for x in range(12):

				if left_hour == num_set1[x]:
					first = pm_time[x]



		# for right side of time
		# AM
		if right_am != -1:
			for x in range(12):

				if right_hour == num_set1[x]:
					second = am_time[x]

		# PM
		if right_am == -1:
			for x in range(12):

				if right_hour == num_set1[x]:
					second = pm_time[x]


		results.write('\n' + first + '-' + second)

	except UnboundLocalError:
		return






