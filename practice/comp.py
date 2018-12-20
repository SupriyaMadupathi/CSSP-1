n = int(input())
count = 0
for i in range(2, n):
	if (i % 2 != 0):
		for j in range(2, i):
			if (i % j == 0):
				count += 1
				if (count > 0):
					print(i)
					break
			 	 

