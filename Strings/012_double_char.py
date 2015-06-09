# Given a string, return a string where for every char in the original, there are two chars. 

def double_char(str):
	result = ""
	for i in str:
		result += i * 2

	return result;

assert double_char('The') == 'TThhee'
assert double_char('AAbb') == 'AAAAbbbb'
assert double_char('Hi-There') == 'HHii--TThheerree'