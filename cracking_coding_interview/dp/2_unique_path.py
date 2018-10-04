"""Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right."""

# https://leetcode.com/problems/unique-paths-ii/description/


def unique_path(arr):
	if not arr:
		return
	r,c = len(arr), len(arr[0])
	path = [[0 for j in range(c)] for i in range(r)]
	path[0][0] = 1-arr[0][0]
	for i in range(1, r):
		path[i][0] = path[i-1][0]*(1-arr[i][0])
	for i in range(c):
		path[0][i] = path[0][i-1]*(1-arr[0][i])
	for i in range(r):
		for j in range(c):
			path[i][j] = (path[i-1][j] + path[i][j-1])*(1-arr[i][j])
	return path[-1][-1]


a = [[0,0,0], [0,1,0],[0,0,0]]
print unique_path(a)