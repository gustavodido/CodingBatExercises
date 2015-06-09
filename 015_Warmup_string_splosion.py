# Given a non-empty string like "Code" return a string like "CCoCodCode". 

def string_splosion(str):
	result = ''
	for i in range(len(str)):
		result += str[:i]

	return result + str

assert string_splosion('Code') == 'CCoCodCode'
assert string_splosion('abc') == 'aababc'
assert string_splosion('ab') == 'aab'
