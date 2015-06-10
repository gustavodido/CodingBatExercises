# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere. 

def has22(nums):
	if len(nums) <= 1:
		return False;

	for i in range(len(nums) - 1):
		if nums[i] == nums[i + 1] == 2:
			return True

	return False

assert has22([1, 2, 2]) == True
assert has22([1, 2, 1, 2]) == False
assert has22([2, 1, 2]) == False