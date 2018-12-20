n = int(input())
diff = 0
for i in range(n):
	row = input().split()
	diff += (int(row[i]) - int(row[n-1-i]))
print(abs(diff))
