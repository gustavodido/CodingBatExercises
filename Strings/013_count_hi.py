# Return the number of times that the string "hi" appears anywhere in the given string. 

def count_hi(str):
	return str.count("hi")

assert count_hi('abc hi ho') == 1
assert count_hi('ABChi hi') == 2
assert count_hi('hihi') == 2