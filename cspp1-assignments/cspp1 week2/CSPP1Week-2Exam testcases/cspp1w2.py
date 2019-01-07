def main():
	data = eval(input())
	s = 0
	for each in data:
		if str != type(each):
			s += each
	print(s)

if __name__ == '__main__':
	main()