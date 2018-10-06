# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

"""

def plus_one(nums):
	i = len(nums) - 1
	carry = 1
	while i :
		if nums[i] == 9:
			nums[i] = 0
			carry = 1
		else:
			nums[i] = nums[i] + 1
			break
		i -= 1

nums = [1,2,3]
nums = [1,2,3,9, 9]
nums = [1,2,3,9, 9, 1]
nums = [1,2,3,9, 9, 9]
nums = [1,2,3,9]
plus_one(nums)
print  nums