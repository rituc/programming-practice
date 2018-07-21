# https://leetcode.com/problems/climbing-stairs/description/
def climbing_stairs(n):
	if n == 0:
		return 0
	ways = [0 for i in range(n + 1)]
	ways[0] = 0
	ways[1] = 1
	if n >= 2:
		ways[2] = 2
	for i in range(3, n + 1):
		ways[i] = ways[i - 1] + ways[i - 2]
	return ways[n]


print climbing_stairs(3)
print climbing_stairs(0)

