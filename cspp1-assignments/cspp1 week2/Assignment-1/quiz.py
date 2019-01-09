def loadquestions(data):
	li = []
	print("Load Questions")
	inp = int(data[1])
	# print(inp)
	for i in range(0, inp):
		li.append(input().split(":"))
	if inp > 1:
		print(inp, "are added to the quiz")
	else:
		print("no questions are to be added")

def startquiz(data):
	li = []
	print("Start Quiz")
	inp1 = int(data[1])
	print(inp1)


def main():
	while True:
		data = input()
		if data:
			data = input().split()
			if data[0] == "LOAD_QUESTIONS":
				loadquestions(data)
			if data[0] == "START_QUIZ":
				startquiz(data)
			if data[0] == "SCORE_REPORT":
				score(data)
		else :
			break
	# q = int(data[1])
	# loadquestions(data)
	# print(type(q))
	# print(data)
	# if data[0] == "LOAD_QUESTIONS":
		# print("|----------------|")
		# print("| Load Questions |")
		# print("|----------------|")




if __name__ == '__main__':
	main()