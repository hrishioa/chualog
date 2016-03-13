import Adafruit_BBIO.ADC as ADC
from sys import argv
import sys
import calendar, time
import numpy as np

in_channel = "AIN1"

def main():
    script, bitfile = argv
    ADC.setup()
    file_counter=0
    counter=0

    chunk_no = 1

    global_disparity = 0

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
            sys.stdout.write("\tPosition %d/%d in chunk %d. Global Disparity: %d. Current Voltage: %f V. Speed : %f.\t\r" % (i, chunk_max, chunk_no, global_disparity, val, speed))
            sys.stdout.flush()
            chunk.append(val)
        print "\tCollection complete.\t\t\t\t\t"
        med = np.median(np.array(chunk))
        print "\tWriting chunk to disk:"
        disparity = 0
        with open(bitfile, 'a') as bf:
            for i in xrange(0, chunk_max):
                if chunk[i] > med:
                    bf.write("1")
                    disparity+=1
                elif chunk[i] < med:
                    disparity-=1
                    bf.write("0")
            bf.close()
        print "Chunk %d written to disk. Disparity: %d" % (chunk_no, disparity)
        global_disparity += disparity
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
