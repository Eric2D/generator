import io
import os
import glob
import sys

def the_gen():
	# Opens the file where the results will be stored
	results = open(os.path.join("Results.txt"), 'w')

	try:
		times = input('THE FORMAT MUST BE "1:00-3:00 "\n 	AM on the left, PM on the right'
			'\n\nHow many items would you like to convert?\n\n')

	
######################################################

		# time possibilities
		num_set1 = ['1','2','3','4','5','6','7','8','9','10','11','12']

		time_set1 = ['1:00','2:00','3:00','4:00','5:00','6:00','7:00',
			'8:00','9:00','10:00','11:00','12:00']
		time_set11 = ['1: 00','2: 00','3: 00','4: 00','5: 00','6: 00','7: 00',
			'8: 00','9: 00','10: 00','11: 00','12: 00']
		time_set111 = ['1 :00','2 :00','3 :00','4 :00','5 :00','6 :00','7 :00',
			'8 :00','9 :00','10 :00','11 :00','12 :00']
		new_time1 = ['13:00','14:00','15:00','16:00','17:00','18:00','19:00',
			'20:00','21:00','22:00','23:00','00:00']

		time_set2 = ['1:30','2:30','3:30','4:30','5:30','6:30','7:30',
			'8:30','9:30','10:30','11:30','12:30']
		time_set22 = ['1: 30','2: 30','3: 30','4: 30','5: 30','6: 30','7: 30',
			'8: 30','9: 30','10: 30','11: 30','12: 30']
		time_set222 = ['1 :30','2 :30','3 :30','4 :30','5 :30','6 :30','7 :30',
			'8 :30','9 :30','10 :30','11 :30','12 :30']
		new_time2 = ['13:30','14:30','15:30','16:30','17:30','18:30','19:30',
			'20:30','21:30','22:30','23:30','00:30']

		for x in range(times):
			x = x + 1

			# allows input for the time you would like to convert
			search = raw_input('What are you converting? '
				+ str(x) + '\n\n')
			start = search.find('-') + 1

			am = search[:start - 1]

			pm = search[start:]


			# for reporting on conversion in the results file
			if start == 0:
				results.write('\n' + search)
			else:
				for x in range(12):

					# AM possibilities check
					if am == time_set111[x] or am == time_set11[x]:
						am = time_set1[x]
					
					if am == num_set1[x]:
						am = time_set1[x]

					if am == time_set222[x] or am == time_set22[x]:
						am = time_set2[x]

				for x in range(12):

					# PM possibilities check
					if pm == time_set1[x] or pm == time_set11[x]:
						pm = new_time1[x]
					if pm == time_set111[x]:
						pm = new_time1[x]

					if pm == num_set1[x]:
						pm = new_time1[x]

					if pm == time_set2[x] or pm == time_set22[x]:
						pm = new_time2[x]
					if pm == time_set222[x]:
						pm = new_time2[x]

				results.write('\n' + am + '-' + pm)

			
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
	r_results = open(os.path.join("Results.txt"), 'r')
	new_text = r_results.read()
	r_results.close()
	print new_text

	sys.exit()


the_gen()