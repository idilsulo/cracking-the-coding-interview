"""
PROBLEM 

One Away: 
* There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
* Given two strings, write a function to check if they are one edit (or zero edits) away.
"""


"""
Notes:
* Ugur came and decided to try his own solution
"""
def one_away(s1: str, s2 : str) -> bool:
	check1 = len(s1) == len(s2)
	check2 = len(s1) == (len(s2) + 1)
	check3 = len(s1) == (len(s2) - 1)


	if check1:
		return sum([i != k for i, k in zip(s1, s2)]) <= 1

	if check2:
		return all( \
				[e1!=e2 for e1, e2 in \
					zip([s1[idx + 1] == s2[idx] for idx in range(len(s2))], \
		 				[s1[idx] == s2[idx] for idx in range(len(s2))]) \
				]
			)
	
	if check3:

		return all( \
			[e1!=e2 for e1, e2 in \
				zip([s1[idx] == s2[idx + 1] for idx in range(len(s1))], \
	 				[s1[idx] == s2[idx] for idx in range(len(s1))]) \
			]
		)

	return False


"""
Notes:
* Time Complexity: O(N), N:length of longest string
* Space Complexity: O(1)
"""
def one_away_alternative(s1: str, s2 : str) -> bool:
	check1 = len(s1) == len(s2)
	check2 = len(s1) == (len(s2) + 1)
	check3 = len(s1) == (len(s2) - 1)

	flag = False
	i = 0
	j = 0

	while(i < len(s1)):
	
		if s1[i] != s2[j]:
			if flag:
				return False
			flag = True
			if check2:
				i += 1
			elif check3:
				j += 1

		i += 1
		j += 1

	return True



if __name__ == '__main__':

	print("TEST CASE #1 : %r" % (one_away('ab', 'abc')))
	print("TEST CASE #2 : %r" % (one_away('abd', 'adb')))



