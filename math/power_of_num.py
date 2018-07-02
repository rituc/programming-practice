class PowerOfNum:
	def is_power_of_num(self, n, num):
		if(n<1):
			return False
		while(n%num==0):
			n /= num

		return n == 1


def main():
	print PowerOfNum().is_power_of_num(27,3)

if __name__ == "__main__":
	main()


