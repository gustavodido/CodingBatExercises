# Given a string, return a new string where the first and last chars have been exchanged. 

def front_back(str):
	if len(str) <= 1:
		return str;

	return str[-1] + str[1 : -1] + str[0]


assert front_back('code') == 'eodc'
assert front_back('a') == 'a'
assert front_back('ab') == 'ba'