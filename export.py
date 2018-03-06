import csv
import glob

csvfiles = glob.glob('parsedfiles/*.csv')
wf = csv.writer(open('parsedfiles/output.csv', 'wb'), delimiter=',')
wf.writerow(['Website','Phone Number'])


for file in csvfiles:
	rd = csv.reader(open(file, 'r'), delimiter=',')
	rd.next()
	
	for row in rd:
		wf.writerow(list(row))