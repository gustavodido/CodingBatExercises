# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble. 

# monkey_trouble(True, True) -> True
# monkey_trouble(False, False) -> True
# monkey_trouble(True, False) -> False

def is_monkey_in_trouble(a_smile, b_smile):
	return (not a_smile != b_smile)

print is_monkey_in_trouble(True, True)
print is_monkey_in_trouble(False, False)
print is_monkey_in_trouble(False, True)
print is_monkey_in_trouble(True, False)


