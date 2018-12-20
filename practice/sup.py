def main():
	s = "asdfghjk"
	res = ""
	for i in range(0, len(s), 3):
		words = s[i:i+3]
		new = words[::-1]
		res = res+new
	print(res)
if __name__ == '__main__':
	main()
