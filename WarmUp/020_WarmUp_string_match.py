# Given 2 strings, a and b, return the number of the positions where they contain the same 
# length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings 
# appear in the same place in both strings. 

import numpy

def string_match(a, b):
	c = 0
	for i in range(len(a)):
		if (a[i : i + 2] == b[i : i + 2]):
			c += 1

	return c

a = numpy.arange(9).reshape(3,3)
print a