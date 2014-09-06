import sys

input = sys.argv

f = open(sys.argv[1],'r')
input=f.read()
output=''

for base in input:
	if base=='T': output+='U'
	else: output+=base

print output