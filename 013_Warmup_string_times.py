# Given a string and a non-negative int n, return a larger string that is n copies of the original string. 

def string_times(str, n):
	return str * n;

assert string_times('Hi', 2) == 'HiHi'
assert string_times('Hi', 3) == 'HiHiHi'
assert string_times('Hi', 1) == 'Hi'