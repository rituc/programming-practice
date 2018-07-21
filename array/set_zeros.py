# https://www.interviewbit.com/problems/set-matrix-zeros/

def set_matrix_zero(A):

	row_flag = False
	col_flag = False

	for i in range(len(A)):
		for j in range(len(A[0])):
			if(i==0 and A[i][j]==0):
				row_flag = True
			if(j==0 and A[i][j] == 0):
				col_flag = True

			if(A[i][j] == 0):
				A[0][j] = 0
				A[i][0] = 0

	for i in range(1, len(A)):
		for j in range(1, len(A[0])):
			if A[0][j] == 0 or A[i][0]==0:
				A[i][j] = 0

	if row_flag:
		for j in range(len(A[0])):
			A[0][j] = 0

	if col_flag:
		for i in range(len(A)):
			A[i][0] = 0

	return A

A = [[1, 0], [1, 0]]

print set_matrix_zero(A)
A = [
	[1,1,1],
	[1,0,1],
	[1,1,1]
]


# output [
# 	[1,0,1],
# 	[0,0,0],
# 	[1,0,1]
# ]
print set_matrix_zero(A)

A = [
	[0,1,2,0],
	[3,4,5,2],
	[1,3,1,5]
]
# Output:
# [
# 	[0,0,0,0],
# 	[0,4,5,0],
# 	[0,3,1,0]
# ]
print set_matrix_zero(A)

