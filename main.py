import csv
from orderedset import OrderedSet
# if phone or websites dont appear on spreadsheet change the row indexs
#enter file here
fil = ''
with open(fil) as csvfile:
	readCSV = csv.reader(csvfile, delimiter= ",")
	websites = OrderedSet()
	phonenumbers = OrderedSet()
	# find whatever is this array
	data = []
	# remove urls that have these strings,  only works with the first string but not second one.
	# remove anything within remo variable
	remo = []
	for row in readCSV:
		website = row[0]
		phonenumber = row[1]
		if website not in websites:
			if phonenumber not in phonenumbers:
				for x in data:
					if x in website:
						for r in remo:
							if all(r not in website for r in remo):
								if phonenumber not in phonenumbers:
									websites.add(website)
									phonenumbers.add(phonenumber)

									mylist = zip(websites, phonenumbers)



									with open('parsedfiles/' + str(fil), 'w+b') as csvfile:
										writer = csv.writer(csvfile, delimiter=",")
										writer.writerow(['Website','Phone Number'])
										for i in mylist:
											writer.writerow(list(i))
									

	



