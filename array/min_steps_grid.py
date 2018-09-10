def find_min_steps_in_infinite_grid(A, B):
	total = 0
	curr_x = A[0]
	curr_y = B[0]
	for i in range(1, len(A)):
		j = abs(A[i] - curr_x)
		k = abs(B[i] - curr_y)
		curr_x = A[i]
		curr_y = B[i]
		total = total + max(j, k)
	return total


print find_min_steps_in_infinite_grid([0, 1, 1], [0, 1, 2])



