##MAKING SURE ALL INPUT FILES HAVE THE EXACT same HEADINGS and there are no alignment issues before merging 
import sys
import os

inpath, outpath = sys.argv[1], sys.argv[2]

header = None
with open(outpath,'w') as outfile:
	for filename in os.listdir(inpath):
		with open(os.path.join(inpath, filename)) as infile:
			print infile
			line = next(infile)
			if header is None:
				outfile.write(line)
				header = line
			for line in infile:
				outfile.write(line)