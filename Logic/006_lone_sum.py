# Given 3 int values, a b c, return their sum. However, if one of the values is the 
#  same as another of the values, it does not count towards the sum. 

def lone_sum(a, b, c):
	if a == b == c:
		return 0

	if a == b and b != c:
		return c

	if a == c and a != b:
		return b

	if b == c and a != b:
		return a
		
	return a + b + c

assert lone_sum(1, 2, 3) == 6
assert lone_sum(3, 2, 3) == 2
assert lone_sum(3, 3, 3) == 0
assert lone_sum(9, 2, 2) == 9
