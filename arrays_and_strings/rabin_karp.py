"""
Write an implementation of the Rabin-Karp algorithm, a string searching algorithm 
that uses hashing to find any one of a set of pattern strings in a text.

For text of length n and p patterns of combined length m
Best case running time - O(n+m)
Worst case running time is - O(nm)
Space complexity - O(p)

- Originally contributed by Nishant - https://github.com/Optimus-Nishant
"""

def robin(T,P,d,q):
	n=len(T)
	m=len(P)
	p=0
	t=0
	h=pow(d,m-1)%q
	result=[]
	for i in range(m):
		p = (d*p+ ord(P[i]))%q
		t = (d*t+ ord(T[i]))%q 
	for s in range(n-m+1):
		if p==t:
			chk=True
			print chk
			for i in range(m):
				if P[i]!=T[i+s]:
					chk=False
					break
			if chk:
				result=result+[s]
		if s < n-m:
			t=(t-h*ord(T[s]))%q
			t=(t*d+ord(T[s+m]))%q
			t=(t+q)%q


	return result

print robin("3141592653589793", "26", 257, 11)

#text=raw_input("Enter The text: ")
#pattern=raw_input("Enter The Pattern To Be Matched: ")
#print robin(text,pattern,256,10000007)

