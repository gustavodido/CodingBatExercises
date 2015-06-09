# Return the number of times that the string "code" appears anywhere in the given string, except 
# we'll accept any letter for the 'd', so "cope" and "cooe" count. 

import re

def count_code(str):
	return len(re.findall("co(.)e", str))

assert count_code('aaacodebbb') == 1
assert count_code('codexxcode') == 2
assert count_code('cozexxcope') == 2