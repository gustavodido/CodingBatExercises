stack = []

# Push item to the top
for i in range(10):
	stack.append(i)

print stack	

# Pop item
i1 = stack.pop()
i2 = stack.pop()

print stack, "-", i1, i2