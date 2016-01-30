import csv
import sys
import os

def write():
	name = '700d_transrec_combined.txt'
	try:
		file = open(name, 'w')
		file.close()
	except:
		sys.exit(0)

# result = write()

list1 = []

os.system("merge_srp.py input/700d tempcsv")

with open('tempcsv', 'r') as output:
	repeatreader = csv.reader(output, delimiter = ' ', quotechar = ">")
	for items in repeatreader:
		if list1.count(item) == 0:
			list1.append(item)
		else:
			pass

with open('700d_transrec_combined.txt', 'a') as result:
	n = len(list1)
	for x in range(0, n):
		result.write(list1[x])


