"""
PROBLEM

Zero Matrix: 
* Write an algorithm such that if an element in an MxN matrix is 0, 
	its entire row and column are set to 0.
"""

import numpy as np

def zero_matrix(m : list) -> list:
	
	m = np.array(m)
	M, N = m.shape

	found = []

	for i in range(M):
		for j in range(N):
			if m[i][j] == 0:
				found.append([i,j])

	for i, j in found:
		m[i] = np.zeros(N)
		m[:,j] = np.zeros(M)

	return m.tolist()


if __name__ == '__main__':
	print("TEST CASE #1 : \n %r" % (np.array(zero_matrix([[1,0,3],[4,5,6],[7,8,9]]))))
	print("TEST CASE #2 : \n %r" % (np.array(zero_matrix([[0]]))))
	print("TEST CASE #3 : \n %r" % (np.array(zero_matrix([[1]]))))