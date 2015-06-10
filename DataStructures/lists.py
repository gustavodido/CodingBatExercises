# Creation
my_list = [1, 2, 3, 4, 5]
print my_list

# New item

my_list.append(6)
print "New item", my_list

my_list[len(my_list):] = [7]
print "New item", my_list

# Extend and add a range
my_list.extend([8, 9])
print "Extend", my_list

# Index
print "Index of 5 - ", my_list.index(5)
#print "Index of 100 - ", my_list.index(100) - Exception if the item is not in the list

#Insert
my_list.insert(5, "DUMMY")
print "Insert dummy", my_list

#Remove
my_list.remove("DUMMY")
print "Remove dummy", my_list

#Count
print "Count", my_list.count(2)

#Reverse
my_list.reverse()
print "Reverse", my_list

