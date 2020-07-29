
title = input("Enter file name") # Enter the file to be counted
handle = open(title) 

countsz = dict()
for linez in handle:
    wordz = linez.split()
    for wordd in wordz:
        countsz[wordd] = countsz.get(wordd, 0) + 1

bigCount = None # Initialize to None
bigWord = None # Initialize to None
for wordd,countsz in countsz.items():
    if bigCount is None or countsz > bigCount:
        bigWord = wordd
        bigCount = countsz

print(bigWord, bigCount)