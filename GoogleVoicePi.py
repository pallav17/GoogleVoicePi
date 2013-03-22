#!/usr/bin/python

from multiprocessing import Pool

# Config
# Number of processes
N_PROCESSES = 10

records = {}

def find(n):
	res = digits.find(n)
	if res > -1:
		print("%s found at index %d." % (n, res))
		return (n, res)

with open('pi') as f:
	digits = f.readline().strip()

numbers = [line.strip() for line in open('numbers')]

p = Pool(N_PROCESSES)
res = set(p.map(find, numbers))
res.remove(None)

print("Done.")

for n, count in res:
	records[n] = count

results = sorted(records, key=records.get)
for n in results:
	print("%s => %d" % (n, records[n]))