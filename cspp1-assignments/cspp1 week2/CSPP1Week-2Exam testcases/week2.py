def main():
	data = eval(input())
	summ = 0
	# li = []
	# li.append(data)
	for each in range(len(data)):
		for i1 in range(len(data[1])-1):
			# for i2 in range(len(data))

		# if type(each) == list:
		# print("hi")
			summ += each
			# summ += i
	print(summ)
	# print(avg)
	# for each in data:
	# 	summ += int(each) 
	# 	print(summ)

if __name__ == '__main__':
	main()