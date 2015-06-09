# Return True if the string "cat" and "dog" appear the same number of times in the given string. 

def cat_dog(str):
	return str.count("dog") == str.count("cat")

assert cat_dog('catdog') == True
assert cat_dog('catcat') == False
assert cat_dog('1cat1cadodog') == True