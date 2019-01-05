def main():
	data = eval(input())
	summ = 0
	count = 0
	# li = []
	# li.append(data)
	for each in range(len(data)):
		# if type(i) == list:
			summ += each
			count += 1
			avg = summ//count
		# else:
			# summ += i
	# print(summ)
	print(avg)
	# for each in data:
	# 	summ += int(each) 
	# 	print(summ)

if __name__ == '__main__':
	main()