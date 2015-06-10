# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) 
# and big bars (5 kilos each). Return the number of small bars to use, assuming we always 
# use big bars before small bars. Return -1 if it can't be done. 

def make_chocolate(small, big, goal):
	if (goal > (big * 5) + small):
		return -1

	goal -= min(goal / 5, big) * 5
	if (goal > small):
		return -1

	return min(goal, small)


assert make_chocolate(4, 1, 9) == 4
assert make_chocolate(4, 1, 10) == -1
assert make_chocolate(4, 1, 7) == 2
assert make_chocolate(6, 1, 10) == 5