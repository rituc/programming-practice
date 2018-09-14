def sort_array(nums):
	count_list = [0,0,0]
	for i in range(len(nums)):
		count_list[nums[i]] = count_list[nums[i]]+1
	result = []
	for i in range(len(count_list)):
		for j in range(count_list[i]):
			result.append(i)
	return result


print sort_array([0, 2, 1, 2, 0])