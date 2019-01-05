def main():
	data = input()
	summ = 0
	li = []
	li.append(data)
	for each in range(len(li)):
		if type(each) == list:
			summ += each
			print(summ)
	# for each in data:
	# 	summ += int(each) 
	# 	print(summ)

if __name__ == '__main__':
	main()