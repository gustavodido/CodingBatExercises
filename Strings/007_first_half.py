# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo". 

def first_half(str):
	return str[: len(str) / 2]

assert first_half('WooHoo') == 'Woo'
assert first_half('HelloThere') == 'Hello'
assert first_half('abcdef') == 'abc'
