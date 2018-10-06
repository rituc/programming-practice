# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/
"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

def contains_duplicate(nums):
	a = dict()
	for i in range(len(nums)):
		if nums[i] in a:
			return True
		else:
			a[nums[i]] = 1
	return False

nums = [1,2,3,4]
# nums = [1,1]
# nums = []
# nums = [2,3,4,5,4]
print contains_duplicate(nums)