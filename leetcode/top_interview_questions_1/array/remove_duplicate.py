# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

def remove_dups(nums):
	if len(nums) >= 2:
		k = 1
		i = 1
		while(i < len(nums)):
			if nums[i] == nums[i-1]:
				i +=1
			else:
				nums[k] = nums[i]
				k += 1
				i += 1
		return k
	else:
		return len(nums)

# nums = [1,1,2]
# nums = []
# nums = [1]
# nums = [1,1,1,1,1,1,1]
# nums = [1,2]
# nums = [1,2,3,3,3,4]
nums = [0,0,1,1,1,2,2,3,3,4]
print remove_dups(nums)