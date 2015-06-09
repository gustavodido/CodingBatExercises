# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!". 

def hello_name(str):
	return "Hello " + str + "!"

assert hello_name('Bob') == 'Hello Bob!'
assert hello_name('Alice') == 'Hello Alice!'
assert hello_name('X') == 'Hello X!'