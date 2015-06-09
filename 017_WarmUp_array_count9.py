# Given an array of ints, return the number of 9's in the array. 

def array_count9(arr):
	c = 0
	for i in arr:
		if i == 9:
			c += 1

	return c

assert array_count9([1, 2, 9]) == 1
assert array_count9([1, 9, 9]) == 2
assert array_count9([1, 9, 9, 3, 9]) == 3