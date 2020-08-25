"""
PROBLEM

Palindrome Permutation: 
* Given a string, write a function to check if it is a permutation of a palin­drome. 
* A palindrome is a word or phrase that is the same forwards and backwards. 
* A permutation is a rearrangement of letters. 
* The palindrome does not need to be limited to just dictionary words.

"""

"""
Notes:
* Bit manipulation trick for finding corresponding characters

* Time Complexity: O(N), 3 passes over the string in the worst case -> O(3*N) = O(N)
* Space Complexity: O(1)
"""
def palindrome_permutation(s : str) -> bool:

	xor = 0

	s = s.lower()

	for c in s:
		if c != ' ':
			xor ^= ord(c)

	if xor == 0:
		return True
	elif chr(xor) in s:
		return True
	else:
		return False


if __name__ == '__main__':
	print("TEST CASE #1 : %r" % (palindrome_permutation('Tact Coa')))
	print("TEST CASE #2 : %r" % (palindrome_permutation('Tact CoaB')))
	print("TEST CASE #3 : %r" % (palindrome_permutation('Tact Coa ')))
	print("TEST CASE #4 : %r" % (palindrome_permutation('')))
	print("TEST CASE #5 : %r" % (palindrome_permutation('T')))