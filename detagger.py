import sys
import re


r = open(sys.argv[1], 'r')
w = open(sys.argv[1] + '_detagged.txt', 'w')

regex = re.compile(r'<.*?>')
regex_tag_to_end_of_line = re.compile(r'<.*?\n')
regex_start_of_line_to_tag = re.compile(r'^.*?>')


for line in r:
    line = regex.sub(' ', line)
    line = regex_tag_to_end_of_line.sub('', line)
    line = regex_start_of_line_to_tag.sub('',line)
    w.write(line)

w.close()
r.close()