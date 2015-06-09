# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4. 

def array_front9(nums):
	for i in nums[:4]:
		if i == 9:
			return True;

	return False;

assert array_front9([1, 2, 9, 3, 4]) is True
assert array_front9([1, 2, 3, 4, 9]) is False
assert array_front9([1, 2, 3, 4, 5]) is False
assert array_front9([3, 4, 5]) is False
