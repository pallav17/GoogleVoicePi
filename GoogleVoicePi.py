#!/usr/bin/python

from multiprocessing import Pool

# Config
# Number of processes
N_PROCESSES = 10

records = {}

def find(n):
	res = digits.find(n)
	if res > -1:
		records[n] = res
		print("%s found at index %d." % (n, res))

with open('pi') as f:
	digits = f.readline().strip()

numbers = [line.strip() for line in open('numbers')]

p = Pool(N_PROCESSES)
p.map(find, numbers)

print("Done.")
results = sorted(records, key=records.get)
print results
