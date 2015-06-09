# Given two strings, return True if either of the strings appears at the very end of the 
# other string, ignoring upper/lower case differences (in other words, the computation 
# should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string. 

def end_other(a, b):
	la = a.lower()
	lb = b.lower()
	return la[len(a) - len(b) : ] == lb or lb[len(b) - len(a) : ] == la

assert end_other('Hiabc', 'abc') is True
assert end_other('AbC', 'HiaBc') is True
assert end_other('abc', 'abXabc') is True