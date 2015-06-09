# Given a string, return a version without the first and last char, so "Hello" yields "ell". 
# The string length will be at least 2. 

def without_end(str):
	return str[ 1 : -1]

assert without_end('Hello') == 'ell'
assert without_end('java') == 'av'
assert without_end('coding') == 'odin'