def missing_num(num, n):
	sum_num = 0
	for i in num:
		sum_num = i + sum_num
	n_sum = n*(n+1)/2.0
	return n_sum - sum_num

# print missing_num([1,2,3,5], 5)

def main():
	num_list = []
	n = int(raw_input())
	for i in range(n-1):
		num_list.append(int(raw_input()))

	print missing_num(num_list, n)

if __name__ == "__main__":
	main()