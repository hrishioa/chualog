import Adafruit_BBIO.ADC as ADC
from sys import argv
import sys
import calendar, time

in_channel = "AIN1"

def main():
	script, bitfile = argv
	ADC.setup()
	file_counter=0
	counter=0
	start_time = calendar.timegm(time.gmtime())
	# First collect enough data to get a reasonable estimate of the average
	history = []

	average_count = 10000
	average = 0.0

	print "Pulling data for average: "

	for i in xrange(0, average_count):
		val = (ADC.read(in_channel)*1.8)
		average+=val
		sys.stdout.write("Collected %d/%d samples.\r" % (i, average_count))
		history.append(val)
		sys.stdout.flush()
	average /= average_count
	speed = 0.0

	print "Starting collection:\n"

	disparity_count = 0

	while(True):
		counter+=1
		val = ADC.read(in_channel)*1.8
		# history[(counter-1) % (len(history))] = val
		average = ((average*average_count)+val)/(average_count+1)
		# average = sum(history)/len(history)
		# average = (max(history)+min(history))/2
		average_count+=1
		with open(bitfile, "a") as file:
			if val > average:
				file.write("1")
				disparity_count+=1
			elif val < average:
				file.write("0")
				disparity_count-=1
			file.close()
		if(calendar.timegm(time.gmtime()) != start_time):
			speed = average_count/(calendar.timegm(time.gmtime())-start_time)
		sys.stdout.write("\t Counter: %d. Disparity: %d. Current Average: %f. Current Bit: %d. Current Voltage: %f. Speed : %f.\t\r" % (counter, disparity_count, average, 1 if val > average else (0 if val < average else -1), val, speed))
		sys.stdout.flush()

	# while(True):
	# 	counter+=1
	# 	val = ADC.read(in_channel)*1.8
	# 	with open(filename, "a") as file:
	# 		file.write("%f\n" % val)
	# 		file.close()
	# 	if calendar.timegm(time.gmtime()) != start_time:
	# 		sys.stdout.write("\tSpeed : %f, Counter: %d. Current Voltage: %f\t\r" % (counter/(calendar.timegm(time.gmtime())-start_time), counter, val))
	# 	sys.stdout.flush()

main()
