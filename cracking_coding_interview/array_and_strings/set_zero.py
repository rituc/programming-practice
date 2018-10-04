def set_zero(a):
	row_flag = False
	col_flag = False
	for i in range(len(a)):
		for j in range(len(a[0])):
			if(i == 0 and a[i][j] == 0):
				row_flag = True
			if (j == 0 and a[i][j] == 0):
				col_flag = True

			if a[i][j] == 0:
				a[0][i] = 0
				a[i][0] = 0

	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[0][j] == 0 or a[i][0] == 0:
				a[i][j] = 0

	if row_flag:
		for i in range(len(a[0])):
			a[0][j] = 0

	if col_flag:
		for i in range(len(a)):
			a[i][0] = 0
	return a


A = [[1, 1], [1, 0]]

print set_zero(A)