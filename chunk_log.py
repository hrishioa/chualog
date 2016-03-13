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

    chunk_no = 0

    chunk_max = 10000
    chunk = []
	start_time = calendar.timegm(time.gmtime())
    print "Loading data to chunk:"
    for i in xrange(0, chunk_max):
		val = ADC.read(in_channel)*1.8
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
