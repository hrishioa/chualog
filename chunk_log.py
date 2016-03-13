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

    chunk_no = 1

    while(True):
        chunk_max = 10000
        chunk = []
        start_time = calendar.timegm(time.gmtime())
        speed = 0
        print "\tLoading data to chunk:"
        for i in xrange(0, chunk_max):
            val = ADC.read(in_channel)*1.8
            if(calendar.timegm(time.gmtime()) != start_time):
                speed = i/(calendar.timegm(time.gmtime())-start_time)
            sys.stdout.write("\tPosition %d/%d in chunk %d. Current Voltage: %f V. Speed : %f.\t\r" % (i, chunk_max, chunk_no, val, speed))
            sys.stdout.flush()
            chunk.append(val)
        print "\tCollection complete.\t\t\t\t\t"
        avg = sum(chunk)/len(chunk)
        print "\tWriting chunk to disk:"
        with open(bitfile, 'a') as bf:
            for i in xrange(0, chunk_max):
                if chunk[i] > avg:
                    bf.write("1")
                elif chunk[i] < avg:
                    bf.write("0")
            bf.close()
        print "Chunk %d written to disk." % chunk_no
        chunk_no+=1

    # while(True):
    #     counter+=1
    #     val = ADC.read(in_channel)*1.8
    #     with open(filename, "a") as file:
    #         file.write("%f\n" % val)
    #         file.close()
    #     if calendar.timegm(time.gmtime()) != start_time:
    #         sys.stdout.write("\tSpeed : %f, Counter: %d. Current Voltage: %f\t\r" % (counter/(calendar.timegm(time.gmtime())-start_time), counter, val))
    #     sys.stdout.flush()

main()
