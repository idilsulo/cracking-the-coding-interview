"""
PROBLEM

URLify: 
* Write a method to replace all spaces in a string with '%20'. 
* You may assume that the string has sufficient space at the end to hold the additional characters,
	and that you are given the "true" length of the string. 
* If implementing in Java, please use a character array so that you can perform this operation in place.

Input: "Mr John Smith    ", 13 
Output: "Mr%20John%20Smith"

"""

"""
Notes: 
* Strings are immutable in Python. Therefore, we use another string in order to copy the relevant characters

* Time Complexity: O(N), N is the length of actual string
* Space Complexity: O(N), allocated string grows with the size of input array
"""
def urlify(s : str, length : int) -> str:

	url = ''
	#start = 0
	#end = 0
	for c in s[:length]:
		if c != ' ':
			url += c
		else:
			url += '%20'

	return url


		
if __name__ ==  '__main__':

	print("TEST CASE #1 : %r" % (urlify('abc De  ', 7)))
	print("TEST CASE #2 : %r" % (urlify("Mr John Smith    ", 13)))
