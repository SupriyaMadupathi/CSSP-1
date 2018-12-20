n = int(input())
for i in range(n):
	str1 = input()
	str2 = str1[::-1]
	diff1 = 0
	diff2 = 0
	for each in range(1,len(str1)):
		# diff1 = ord(str1[each]) - ord(str1[each-1])
		# #print(diff1)
		# for each in range(1,len(str2)):
		# 	diff2 = ord(str1[each]) - ord(str1[each-1])
	#		print(diff2)
		# if(diff1 != diff2):
		if(ord(str1[each]) - ord(str1[each-1]) != ord(str1[each]) - ord(str1[each-1])):
			print("notfunny")
			break
		else:
			print("funny")
			break