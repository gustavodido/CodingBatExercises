# Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere. 

def array123(nums):
	for i in range(len(nums)):
		if nums[i : i + 3] == [1, 2, 3]:
			return True
	return False

assert array123([1, 1, 2, 3, 1]) is True
assert array123([1, 1, 2, 4, 1]) is False
assert array123([1, 1, 2, 1, 2, 3]) is True
assert array123([1, 2, 3]) is True