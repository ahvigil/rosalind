import sys

input = sys.argv
a_count=0
g_count=0
t_count=0
c_count=0

print sys.argv
f = open(sys.argv[1],'r')
input=f.read()
print input, type(input)

for base in input:
	if base=='A': a_count+=1
	if base=='G': g_count+=1
	if base=='T': t_count+=1
	if base=='C':c_count+=1

print a_count, c_count, g_count, t_count 