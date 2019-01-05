def main():
	data = input()
	summ = 0
	li = []
	li.append(data)
	for i in range(len(li)):
		if type(i) == list:
			summ += li[i]
	print(summ)
	# for each in data:
	# 	summ += int(each) 
	# 	print(summ)

if __name__ == '__main__':
	main()