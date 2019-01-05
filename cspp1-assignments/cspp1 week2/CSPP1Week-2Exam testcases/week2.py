def main():
	data = eval(input())
	summ = 0
	# li = []
	# li.append(data)
	for each in range(len(data)):
		# if type(i) == list:
			summ += each
		# else:
			# summ += i
			print(summ)
	# for each in data:
	# 	summ += int(each) 
	# 	print(summ)

if __name__ == '__main__':
	main()