import os, sys, calendar, time

while(True):
	print "Adding..."
	os.system("git add .")
	print "Committing..."
	os.system("git commit -m 'Timely commit %d'" % (calendar.timegm(time.gmtime())))
	print "Pushing..."
	os.system("git push --all")
	print "Sleeping..."

	time.sleep(600)
