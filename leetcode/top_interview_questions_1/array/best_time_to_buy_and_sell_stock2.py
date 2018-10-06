# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
def cal_profit(nums):
	profit = 0
	for i in range(len(nums)-1):
		if(nums[i] < nums[i+1]):
			profit += nums[i+1]-nums[i]
	return profit

nums = [7,1,5,3,6,4]
nums = [1,2,3,4,5]
nums = [7,6,5,4,3,2,1]

print cal_profit(nums)