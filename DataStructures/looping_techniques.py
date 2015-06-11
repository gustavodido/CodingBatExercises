ml = [1, 2, 3]

#Simple
for i in ml:
	print i

#With index
for i, j in enumerate(ml):
	print i, ":", j

#Dics
di = {0: 100, 1: 200, 2: 300}
for k, v in di.iteritems():
	print k, ":", v

#Loop over a copy, changing the underlining list
for i in ml[:]:
	ml.append(i)
	
print ml