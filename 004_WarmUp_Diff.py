# Given an int n, return the absolute difference between n and 21, 
# except return double the absolute difference if n is over 21. 

# diff21(19) = 2
# diff21(10) = 11
# diff21(21) = 0

def diff21(x):
	diff = abs(x - 21)
	return diff if x <= 21 else diff * 2;

assert diff21(19) is 2
assert diff21(10) is 11
assert diff21(21) is 0
