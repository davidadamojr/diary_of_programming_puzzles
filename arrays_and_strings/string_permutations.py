#This Program Prints the various Permutaions of a given string in lexographical Order.

from itertools import permutations
stri=input()
all = [''.join(ch) for ch in permutations(stri)]
all = set(all)
all=list(all)
all.sort()
for item in all:
	print (item)


