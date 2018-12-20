def main():
	s = "123123456"
	res = ""
	new = 0
	for i in range(0, len(s),1):
		num = s[i+1:len(s)-1]
		for i in num:
			new += int(i)
			break
	res = s[0]+str(new) + s[len(s) -1]
	print(res)
if __name__ == '__main__':
	main()