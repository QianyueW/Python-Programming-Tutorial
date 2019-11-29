import re
handle  = open('regex_sum_327075.txt')
numlist = list()

for line in handle:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) < 1: continue
    for num in stuff:
        num = int(num)
        numlist.append(num)

print(sum(numlist))
