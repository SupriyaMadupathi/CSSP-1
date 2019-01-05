def main():
	data = eval(input())
	summ = 0
	# li = []
	x = ""
	# li.append(data)
	for each in data:
		if x != type(each):
			summ += each
		# for i1 in each:
		# 	# for i2 in i1:
		# 	li.append(i1)
		# 	# li.append(i1)
		# 	for x in li:
		# 		if y != type(x):
		# 			summ += x

	print(summ)
			

if __name__ == '__main__':
	main()