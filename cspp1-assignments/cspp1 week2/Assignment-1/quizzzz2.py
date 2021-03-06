adict = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
class Question:
	def __init__(self,question, options, correctans, maxmarks, negmarks):
		# print(correctch(correctans))
		# print(options)
		self.question = question
		self.options = options
		self.correctans = correctans
		self.maxmarks = maxmarks
		self.negmarks = negmarks
	def getquestext(self):
		return self.question
	def getoptions(self):
		return self.options
	def getcorrectans(self):
		# return correctch()
		# print(self.correctans)
		# print(self.options)
		listch = self.options.split(",")
		for i in range(len(listch)):
			if i == int(self.correctans) - 1:
				each = listch[i].split()
				# print(each[1])
				return each[1]
	def getmaxmarks(self):
		return self.maxmarks
	def getnegmarks(self):
		return self.negmarks
	# def correctch(self):
	# 	print("-----")
	# 	listch = self.options.split(",")
	# 	for i in range(len(listch)):
	# 		if i == int(self.correctans):
	# 			each = listch[i].split()
	# 			print(each[1])
	# 			return each[1]


class Quiz:
	allquestions = []
	partchoice = []
	totscore = 0
	def __init__(self):
		pass
	def addquestion(self, Question):
		self.allquestions.append(Question)
	def startquiz(self):
		for each in self.allquestions:
			print(each.getquestext() + "(" + each.getmaxmarks() + ")")
			str1 = ""
			for eachopt in each.getoptions().split(","):
				# print(each.getoptions().split(","))
				str1 += eachopt + "\t"
			str1 = str1[:-1]
			print(str1 + "\n")
	def partoptions(self, list1):
		for each in list1:
			eachx = each.split()
			# if eachx[1] in adict:
				# self.partchoice.append(adict[eachx[1]])
			# else:
			self.partchoice.append(eachx[1])
		# print(self.partchoice)
	def matchans(self):
		for each in self.allquestions:
			print(each.getquestext())
			for part_ch in self.partchoice:
				# print(self.partchoice)
				# print(part_ch)
				# print(each.getcorrectans())
				if each.getcorrectans() == part_ch:
					print(" Correct Answer! - Marks Awarded: " + each.getmaxmarks())
					self.totscore += int(each.getmaxmarks())
					del self.partchoice[self.partchoice.index(part_ch)]
					break
				else:
					print(" Wrong Answer! - Penalty: " + each.getnegmarks())
					self.totscore += int(each.getnegmarks())
					del self.partchoice[self.partchoice.index(part_ch)]
					break
		print("Total Score: " + str(self.totscore))


def main():
	quiz = Quiz()
	k = ""
	try:
		while True:
			n = input().split()
			# print(n)
			if n[0] == "LOAD_QUESTIONS":
				print("|----------------|")
				print("| Load Questions |")
				print("|----------------|")
				try:
					if n[1] == "0":
						k = n[1]
						raise Exception("Quiz does not have questions")
					else:
						for i in range(int(n[1])):
							string = input().split(":")
							# print(string)
							# try:
							# print(string[1])
							if string[0] == "" or string[1] == "" or string[2] == "" or string[3] == "" or string[4] == "":
								k = "0"
								raise Exception("Error! Malformed question")
							elif len(string[1].split(",")) < 2:
								k = "0"
								raise Exception(string[0] + " does not have enough answer choices")
							elif int(string[2]) > 4:
								k = "0"
								raise Exception("Error! Correct answer choice number is out of range for " + string[0])
							elif int(string[3]) < 0:
								k = "0"
								raise Exception("Invalid max marks for question about sony")
							elif int(string[4]) > 0:
								k = "0"
								raise Exception("Invalid penalty for " + string[0])
							else:
								Ques = Question(string[0], string[1], string[2], string[3], string[4])
								quiz.addquestion(Ques)
						print(n[1] + " are added to the quiz")
							# except Exception as e:
								# print(e)

				except Exception as e:
					print(e)
			if n[0] == "START_QUIZ":
				print("|------------|")
				print("| Start Quiz |")
				print("|------------|")
				if k != "0":
					quiz.startquiz()
					list1 = []
					for i in range(int(n[1])):
						list1.append(input())
					quiz.partoptions(list1)
			if n[0] == "SCORE_REPORT":
				print("|--------------|")
				print("| Score Report |")
				print("|--------------|")
				if k != "0":
					quiz.matchans()
	except EOFError:
		pass
main()