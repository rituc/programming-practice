# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

def three_sum(nums):
	res = []
	nums.sort()
	print nums
	for i in range(0, len(nums)-2):
		if i > 0 and nums[i] == nums[i - 1]:
			continue
		l, r = i+1, len(nums) -1
		while(l < r):
			s = nums[i] + nums[l] + nums[r]
			# print "s: ", s
			# print "r: ", r
			# print "l: ", l

			if(s<0):
				l = l + 1
			elif s>0:
				r = r-1
			else:
				res.append([nums[i], nums[l], nums[r]])
				while (l < r and nums[l] == nums[l + 1]):
					l = l + 1
				while (l < r and nums[r] == nums[r - 1]):
					r = r - 1
				l += 1
				r -= 1
	return res


# def threeSum(self, nums):
# 	res = []
# 	nums.sort()
# 	for i in xrange(len(nums)-2):
# 		if i > 0 and nums[i] == nums[i-1]:
# 			continue
# 		l, r = i+1, len(nums)-1
# 		while l < r:
# 			s = nums[i] + nums[l] + nums[r]
# 			if s < 0:
# 				l +=1
# 			elif s > 0:
# 				r -= 1
# 			else:
# 				res.append((nums[i], nums[l], nums[r]))
# 				while l < r and nums[l] == nums[l+1]:
# 					l += 1
# 				while l < r and nums[r] == nums[r-1]:
# 					r -= 1
# 				l += 1; r -= 1
# 	return res


print "Started"
print three_sum([-1,0,1,2,-1,-4])
print "Completed"




