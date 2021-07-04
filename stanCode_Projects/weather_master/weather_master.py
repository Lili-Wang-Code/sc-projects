"""
File: weather_master.py
Name: Lili Wang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = 5


def main():
	"""
	As the users enter the temperature,
	this program will compute the average, highest,
	lowest, cold days (< 16 degrees ) among the inputs.
	When the exit number is entered, this program will show the results,
	and the exit number is not included to compute.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	data = int(input('Next Temperature : (or '+str(EXIT)+' to quit) ? '))
	if data == EXIT:  # the first temperature is the exit number
		print('No temperatures were entered.')
	else:
		maximum = data
		minimum = data
		cold = 0  # count the number of cold days (< 16 degrees)
		count = 1  # to compute the average temperature
		# count the number of users entering the temperature
		total = data  # to compute the average temperature
		# add all temperature of users entered
		average = data  # to compute the average temperature
		while True:
			if data != EXIT:  # whether the temperature is exit number
				if data < 16:
					cold += 1  # count the number of cold days (< 16 degrees)
			data = int(input('Next Temperature : (or ' + str(EXIT) + ' to quit) ? '))
			if data == EXIT:
				print('Highest temperature = '+str(maximum))
				print('Lowest temperature = ' + str(minimum))
				print('Average = '+str(average))
				print(str(cold)+' cold day(s)')
				break
			if data > maximum:
				# compare the entered temperature and the current maximum temperature
				maximum = data
			if data < minimum:
				# compare the entered temperature and the current minimum temperature
				minimum = data
			count += 1  # add one more time of entering the temperature
			total = total + data  # add all the temperature users entered
			average = total / count  # compute the average temperature


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
