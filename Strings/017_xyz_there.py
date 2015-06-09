# Return True if the given string contains an appearance of "xyz" where the xyz is not directly 
# preceeded by a period (.). So "xxyz" counts but "x.xyz" does not. 

def xyz_there(str):
		return str.count(".xyz") == 0 and str.count("xyz") > 0 
assert xyz_there('abcxyz') == True
assert xyz_there('abc.xyz') == False
assert xyz_there('xyz.abc') == True
