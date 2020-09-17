"""
A trie is a variant of an n-ary tree in which characters are stored at each node. Each path down the tree may represent a word. 
"""

"""
Notes:
* Tries reminded me of an old project of mine, a WordTree project written in Haskell
	https://github.com/idilsulo/METU-CENG/blob/master/CENG242/THE2/HW2.hs
* Haskell is a very powerful language especially for making use of recursive data types:
	https://stackoverflow.com/questions/63694831/recursive-data-types-in-python

"""

ALPHABET_SIZE = 27  # Alphabet size containing the end of string character
BASE = 65 			# Base used for ordinal and character conversion
SPECIAL_CHAR = '['  # Special character for the root

"""
Time Complexity and Comparison to Hash Table:

* A trie can check if a string is a valid prefix in 0(K) time, 
	where K is the length of the string. 
* This is actually the same runtime as a hash table will take. 
* Although we often refer to hash table lookups as being 0(1) time, 
	this isn't entirely true. A hash table must read through all the characters in the input, 
	which takes O(K) time in the case of a word lookup. 
"""
class TrieNode:
	def __init__(self, x):
		self.val = x
		self.children = [None] * ALPHABET_SIZE # nodes[1] = 1 -> 'A'
		self.count = 0


def pretty_print(node, seq=''):
	if not node:
		return
	elif node.count == 0:
		print(seq + str(node.val))
	else:
		if node.val != SPECIAL_CHAR: 
			seq += str(node.val)
			if node.count > 1: 
				print(seq + ':')
				seq = '\t' + seq
		
		for i, child in enumerate(node.children):
			if child: pretty_print(child, seq)
		

def insert(node, s):
	for c in s:
		i = ord(c) - BASE
		if not node.children[i]: 
			node.children[i] = TrieNode(c)
			node.count += 1
		node = node.children[i]

def fix_invalid(node, seq):
	for c in seq:
		node.count += 1
		node = node.children[ord(c) - BASE]
		


def delete(root, s):
	parent = None
	node = root 
	flag = True
	for i,c in enumerate(s):
		j = ord(c) - BASE
		if not node.children[j]:
			print("%s does not exist. Thus, cannot be deleted." % (s))
			fix_invalid(root, s[:i])
			return
		else:
			if node.count == 1:
				# Check if the whole string exists in dictionary
				# Ex: LIVE exists but LIVEE is trying to be deleted
				flag = True
				node.count -= 1
			else:
				parent = node
				node = node.children[j]

	if flag:
		parent.count -= 1
		parent.children[ord(node.val)-BASE] = None

if __name__ == '__main__':

	trie = TrieNode(SPECIAL_CHAR)
	insert(trie, 'A')
	insert(trie, 'MANY')
	insert(trie, 'MY')
	insert(trie, 'LIE')
	insert(trie, 'LOVE')
	insert(trie, 'LOSE')
	
	print("Printing trie...")
	pretty_print(trie)

	delete(trie, 'LIFE')
	delete(trie, 'LOVE')
	
	print("Printing trie...")
	pretty_print(trie)

	insert(trie, 'LOST')
	insert(trie,'LOOKING')
	insert(trie, 'LIFE')
	insert(trie, 'LIVABLE')
	insert(trie, 'LOOSE')

	print("Printing trie...")
	pretty_print(trie)

	# delete(trie, 'LIFE')
	delete(trie, 'LIVABLEE')

	insert(trie, 'MORE')
	insert(trie, 'MOVE')
	insert(trie, 'MOST')
	insert(trie, 'MOREOVER')
	insert(trie, 'MOVIE')
	insert(trie, 'TRIE')
	insert(trie, 'TREE')

	print("Printing trie...")
	pretty_print(trie)