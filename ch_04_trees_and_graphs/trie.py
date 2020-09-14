"""
A trie is a variant of an n-ary tree in which characters are stored at each node. Each path down the tree may represent a word. 
"""

"""
Notes:
* Tries reminded me of this: https://github.com/idilsulo/METU-CENG/blob/master/CENG242/THE2/HW2.hs
"""

# class ListNode:
# 	def __init__(self, x):
# 		self.char = x
# 		self.next = None

# Alphabet size containing the end of string character
ALPHABET_SIZE = 27
BASE=65
SPECIAL_CHAR='['

class TrieNode:
	def __init__(self, c=SPECIAL_CHAR):
		self.children = [None] * ALPHABET_SIZE # nodes[1] = 1 -> 'A'
		self.count = 0

	def pretty_print(self):
		node = self.children

		while(node.count):
			for child in children:
				print(child.data, end=' ')
			node = node


def insert(root, s):

	node = root 
	for c in s:
		i = ord(c) + BASE
		if not node.nodes[i]:
			node.nodes[i] = TrieNode(c)
			node.count += 1
		node = node.nodes[i]




if __name__ == '__main__':

	trie = TrieNode()
