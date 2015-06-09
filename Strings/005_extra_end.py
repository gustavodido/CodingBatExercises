# Given a string, return a new string made of 3 copies of the last 2 chars of the original 
# string. The string length will be at least 2. 

def extra_end(str):
	sub = str[-2:]
	return sub * 3

assert extra_end('Hello') == 'lololo'
assert extra_end('ab') == 'ababab'
assert extra_end('Hi') == 'HiHiHi'