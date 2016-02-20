import sys 

A = []
B = []
execute = {}

A.append('a1')
A.append('a2')
B.append('B1')
B.append('B2')
B.append('B3')

for i in A:
	z = []
	for j in B:
		z.append(j)
	execute[i] = z

print execute

