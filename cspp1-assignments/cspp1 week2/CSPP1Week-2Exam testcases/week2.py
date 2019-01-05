def main():
	data = eval(input())
	summ = 0
	# li = []
	# li.append(data)
	for i in range(len(data)):
		# if type(i) == list:
			summ += i
		# else:
			# summ += i
	print(summ)
	# for each in data:
	# 	summ += int(each) 
	# 	print(summ)

if __name__ == '__main__':
	main()