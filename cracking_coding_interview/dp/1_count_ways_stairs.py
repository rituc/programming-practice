"""
8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
"""

def count_ways(n):
	count = [0 for i in range(n+1)]
	if n<=2: return n

	count[0] = 0
	count[1] = 1
	count[2] = 2

	for i in range(3, n+1):
		count[i] = count[i-1] + count[i-2] + count[i-3]
	return count[n]

print count_ways(8)
print count_ways(4)
print count_ways(1)
print count_ways(2)
print count_ways(3)
print count_ways(5)
print count_ways(4)
print count_ways(0)