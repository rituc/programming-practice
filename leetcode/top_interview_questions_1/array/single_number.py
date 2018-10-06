# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/
def find_single_number(nums):
	if len(nums) == 0: return
	x = nums[0]
	for i in range(1, len(nums)):
		x = x ^ nums[i]
	return x

nums = [1,2,1]
nums = []
nums = [1,1,2,2,3,3,4,5,4]
print find_single_number(nums)