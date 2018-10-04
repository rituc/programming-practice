# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents

def coin_change(n, s):
	table = [ 0 for k in range(n)]
	table[0] = 1
	for i in range(0, len(s)):
		for j in range(s[i], n+1):
			table[j] += table[j-s[i]]

coin_change(10, [1,2,3])