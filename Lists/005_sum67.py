# Return the sum of the numbers in the array, except ignore sections of numbers starting with 
# a 6 and extending to the next 7 (every 6 will be followed by at least one 7). 
# Return 0 for no numbers. 

def sum67(nums):
	s = 0
	six_found = False
	for i in nums:
		if i == 6:
			six_found = True
		elif six_found and i == 7:
			six_found = False
		elif not six_found:
			s += i

	return s

assert sum67([1, 2, 2]) == 5
assert sum67([1, 2, 2, 6, 99, 99, 7]) == 5
assert sum67([1, 1, 6, 7, 2]) == 4