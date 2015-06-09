# Given two int values, return their sum. Unless the two values are the same, then return double their sum. 

# sum_double(1, 2) = 3
# sum_double(3, 2) = 5
# sum_double(2, 2) = 8

def sum_double(a, b):
	sum = a + b
	return sum if a != b else sum * 2

assert sum_double(1, 2) is 3
assert sum_double(3, 2) is 5
assert sum_double(2, 2) is 8