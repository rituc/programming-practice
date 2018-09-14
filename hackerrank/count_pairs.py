# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ar):
	result = 0
	count_map = {}
	for i in ar:
		if i in count_map:
			count_map[i] = count_map[i] + 1
		else:
			count_map[i] = 1
	for i in count_map.values():
		result = result + i/2
	return result

sockMerchant(	)