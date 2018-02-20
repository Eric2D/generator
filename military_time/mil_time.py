# mil_time converts regular time to military time

import io
import os
import glob
import sys
import scenario2

def the_gen():
	# Opens the file where the results will be stored
	results = open(os.path.join("../ZZ_data_ZZ/results.txt"), 'w')

	try:
		times = input('THE FORMAT MUST BE (1:00am-3:00pm) or (12pm-12am)\n'
			'THIS CODE DOES NOT ASSUME AM AND PM\n'
			'Words that are entered will only be printed, they cannot be converted'
			'\n\nHow many items would you like to convert?\n\n')

	
######################################################

		# time possibilities
		num_set1 = ['1','2','3','4','5','6','7','8','9','10','11','12']

		pm_time = ['13','14','15','16','17','18','19',
			'20','21','22','23','12']


		for x in range(times):
			x = x + 1

			# allows input for the time you would like to convert
			search = raw_input('What are you converting? '
				+ str(x) + '\n\n')
			

			# strips white space for time variable and makes all letters lower case
			# creating number string variable
			num_search = search.lower()
			count_space = num_search.count(' ')
			num_search = num_search.replace(' ', '', count_space)

			# establish am and pm on right and left side + first center marker
			center_marker = num_search.find('-')
			left_am = search.find('am', 0, center_marker)
			right_am = search.find('am', center_marker)
			left_pm = search.find('pm', 0, center_marker)
			right_pm = search.find('pm', center_marker)

			# strip am and pm away for simple conversion
			num_search = num_search.replace('pm','', 2)
			num_search = num_search.replace('am', '', 2)

			# set search markers
			center_marker = num_search.find('-')
			left_marker = num_search.find(':')
			right_marker = num_search.find(':', left_marker + 1)

			# seperating time variable
			left_hour = num_search[ : left_marker]
			left_min = num_search[ left_marker : center_marker ]

			right_hour = num_search[ center_marker + 1 : right_marker ]
			right_min = num_search[ right_marker : ]

			# for scenario if the times are properly formated 1:00am-3:00pm
			if left_marker != -1 and right_marker != -1:

				# for left side of time
				if left_pm != -1:
					for x in range(12):

						if left_hour == num_set1[x]:
							left_hour = pm_time[x]
				# for special case 12am
				if left_am != -1:

					if left_hour == '12':
						left_hour = '00'


				# for Right side of time
				if right_pm != -1:
					for x in range(12):

						if right_hour == num_set1[x]:
							right_hour = pm_time[x]
				# for special case 12am
				if right_am != -1:

					if right_hour == '12':
						right_hour = '00'

				first = left_hour + left_min
				second = right_hour + right_min

				results.write('\n' + first + '-' + second)
				continue

			# for scenario if the times are properly formated 12pm-12am
			if left_marker == -1 and right_marker == -1:
				if left_am != -1 or left_pm != -1:
					if right_am != -1 or right_pm != -1:
						scenario2.scen2(search, results)
						continue

			# for scenario if time is not in correct format
			if left_marker == -1 or right_marker == -1:
				results.write('\n' + search)
				continue
			if left_am == -1 or left_pm == -1:
				results.write('\n' + search)
				continue
			if right_am == -1 or right_pm == -1:
				results.write('\n' + search)
				continue

			
	except ValueError:
		print('\n\n\n\nPlease enter a number.\n\n\n\n')
		the_gen()
	except SyntaxError:
		print('\n\n\n\nPlease enter a number.\n\n\n\n')
		the_gen()
	except TypeError:
		print('\n\n\n\nPlease enter a whole number.\n\n\n\n')
		the_gen()
	except NameError:
		print('\n\n\n\nPlease enter a whole number.\n\n\n\n')
		the_gen()

	

	results.close()
	
	# For displaying the search results after the code has finished
	r_results = open(os.path.join("../ZZ_data_ZZ/results.txt"), 'r')
	new_text = r_results.read()
	r_results.close()
	print new_text

	sys.exit()


the_gen()