# Lists without duplication

set_a = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print set_a

set_b = set([1, 2, 6, 7, 8])
print set_b

# In a but not b - Difference
print set_a - set_b

# In a or b - Union
print set_a | set_b

# In a and b - Intersection
print set_a & set_b

# In a or b, but not both - Complement
print set_a ^ set_b



