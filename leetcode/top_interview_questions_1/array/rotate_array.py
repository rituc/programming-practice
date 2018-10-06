# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# def rotate_array(nums, k):
# 	length = len(nums)
# 	counter = k
# 	i = 0
# 	k = k%length
# 	while (counter):
# 		temp = nums[i]
# 		nums[i] = nums[length - counter]
# 		nums[length - counter] = nums[i + k]
# 		nums[i + k] = temp
# 		i += 1
# 		counter -= 1

def rotate_array(nums, k):
	n = len(nums)
	k = k % n
	if not k: return
	nums[:] = nums[n-k:] + nums[:n-k]

nums = [1,2,3,4,5,6,7]
k = 3
# nums = [1,2,3]
# k= 2

rotate_array(nums, k)
print nums


