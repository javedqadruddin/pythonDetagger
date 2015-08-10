import sys
import re


r = open(sys.argv[1], 'r')
w = open(sys.argv[1] + '_detagged.txt', 'w')

regex = re.compile(r'<.*?>')


for line in r:
    w.write(regex.sub(' ', line))

w.close()
r.close()