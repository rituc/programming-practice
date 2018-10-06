# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
# Given two arrays, write a function to compute their intersection.

def find_arr_intersection(nums1, nums2):
	nums1.sort()
	nums2.sort()
	n = min(len(nums1), len(nums2))
	a = []
	for i in range(n):
		if nums1[i] == nums2[i]:
			a.append(nums1[i])
	return a

def find_arr_intersection1(nums1, nums2):
	count = dict()
	a = []
	for i in nums1:
		if i in count:
			count[i] = count[i] + 1
		else:
			count[i] = 1

	for i in nums2:
		if i in count and count[i] > 0:
			a.append(i)
			count[i] =  count[i]-1
	return a




nums2 = [4,1,2,3, 2]
nums1 = [5, 1, 2, 2, 23, 4]
print find_arr_intersection1(nums1, nums2)





