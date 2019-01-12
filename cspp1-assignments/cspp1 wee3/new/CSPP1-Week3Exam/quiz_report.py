
def main():
	data = int(input())

	# print(data)
	li = []
	l2 = []
	total = 0
	summ = 0
	for i in range(data):
		response = input().split("|")
		li.append(response)
		# li.groupby(x[0], x[4])
		# for each in li:
			# if each[]
		# for each in range(len(response)):
			# if int(each[i]) == int(li[i]):
				# l2.append(i)
			# li.append(each)
			# dic[ea]  = li

	print(li)
	dic = []
	for x in li:
		if x[2] == x[3]:
			dic.append(x[4])
			# dic[x[0]] = x[4]
			# break
	print(dic)
	for each in dic:
		summ += int(each)
	print(summ)
		# for x in li:
			# if x[i] == x[i+1]:
			# l2 = {}
			# dic[x[0]] = x[4]	
			# print(dic)
			# print(x)
			# if x[2] == x[3]:
				# summ += int(x[4])
	# print(x[0],":" ,summ)
		# print(summ)
				# l2[x[0]] = x[4]
				# l2.append(x[4])
				# for y in l2:
		# print(l2)

			# dic ={}
			# dic[x] = li
			# print(dic)
			# print(x)
			# if x[2] == x[3]:
				# li.append(x[4])
				# print(li)

		# print(response)


if __name__ == '__main__':
	main()

