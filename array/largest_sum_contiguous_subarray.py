# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
def sum_contiguous(nums):
	max_so_far = 0
	max_ending_here = 0
	max_num = nums[0]
	for i in range(len(nums)):
		max_ending_here = max_ending_here + nums[i]
		if max_ending_here < 0:
			max_ending_here = 0
		if(max_ending_here > max_so_far):
			max_so_far = max_ending_here
		if  nums[i] > max_num:
			max_num = nums[i]

	if max_num < 0:
		max_so_far = max_num
	return max_so_far


print sum_contiguous([-2, -3, 4, -1, -2, 1, 5, -3])
print sum_contiguous([-1, -2, -3, -4])
