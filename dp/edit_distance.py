# https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
def edit_distance(word1, word2):
	m = len(word1)
	n = len(word2)

	dp = [[0 for i in range(n+1)] for j in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i == 0:
				dp[i][j] = j
			elif j==0:
				dp[i][j] = i
			elif word1[i-1] == word2[j-1]:
				dp[i][j] = dp[i-1][j-1]

			else:
				dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

	return dp[m][n]

str1 = "sunday"
str2 = "saturday"

print edit_distance(str1, str2)


