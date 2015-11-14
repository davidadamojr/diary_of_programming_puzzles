"""
Write an implementation of the Rabin-Karp algorithm, a string searching algorithm 
that uses hashing to find any one of a set of pattern strings in a text.

For text of length n and p patterns of combined length m
Best case running time - O(n+m)
Worst case running time is - O(nm)
Space complexity - O(p)

- Originally contributed by Nishant - https://github.com/Optimus-Nishant
"""

def rabin_karp_search(text, pattern):
	"""
	Rabin karp search is best with a rolling hash algorithm
	The key to the algorithm's performance is the efficient computation of 
	hash values of the successive substrings of text.
	"""
	
	text_length = len(text)
	pattern_length = len(pattern)
	pattern_hash = hash(pattern)
	substr_hash = hash(text[0:pattern_length-1])
	
	for i in range(0, text_length-pattern_length):
		if pattern_hash == substr_hash:
			if pattern == text[i:pattern_length]: # in case of collisions
				return i
	return None
	
def hash(substr_index, substr, full_text):
	if substr == full_text[0:len(substring)]:
		# calculate new hash value
	else:
		# calculate successive hash
		
