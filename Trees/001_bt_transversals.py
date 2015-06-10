class TreeNode:
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

def in_order(node, arr):
	if node:
		in_order(node.right, arr) 
		arr.append(node.value) 
		in_order(node.left, arr)

def pre_order(node, arr):
	if node:
		arr.append(node.value) 
		pre_order(node.right, arr)
		pre_order(node.left, arr)

def pos_order(node, arr):
	if node:
		pos_order(node.right, arr)
		pos_order(node.left, arr)
		arr.append(node.value) 

def build_tree():
	root = TreeNode(1)
	root.right = TreeNode(2)
	root.left = TreeNode(3)
	root.right.right = TreeNode(4)
	root.right.left = TreeNode(5)
	return root

t = build_tree()

arr = []
pre_order(t, arr)
print arr

arr = []
in_order(t, arr)
print arr

arr = []
pos_order(t, arr)
print arr

