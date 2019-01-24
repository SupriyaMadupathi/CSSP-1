def todo(data):
	
	str1 = ""
	if data[1] == "":
				print("Title not provided")
			
	elif int(data[3]) < 1:
		print("Invalid timeToComplete " + data[3])
	else:
		str1 = data[1] + ", " +data[2] + ", "+ data[3] + ", "
		# print(str1)
		if data[4] == "y":
			str1 += "Important"+ ", "
		
		else:
			str1 += "Not Important" + ", "
		# print(str1)
			# print(str1)
		if data[5] == "y" :
			str1 += "Urgent" + ", "
			# print(str1)
		else: 
			str1+= "Not Urgent" + ", "
		# print(str1)

		if data[6] == "todo" or data[6] == "done":
			str1+= data[6]
		else:
			data[6] != todo or data[6] != done
			str1="Invalid status dud"		
		# else:
			# str2 += "Invalid status"
		# 	continue
	print(str1)

def addtask(data):
	str2 = []
	str2.append(data[1])
	str2.append(data[2])
	str2.append(data[3])
	# str2 = data[1] + ", " + data[2] + ", " + data[3] + ", "
	if data[4] == "y":
		str2.append("Important")
	else :
		str2.append("Not Important")
	if data[5] == "y":
		str2.append("Urgent")
	else:
		str2.append("Not Urgent")
	if data[6] == "todo" or data[6] == "done":
		str2.append(data[6]) 
	return str2
	# print_todoist(str2)
	# print(str2)
# def print_todoist():


def main():
	list1 = []
	l2 = []
	while True:
		try:
			data = input().split(",")
			if data[0] == "task":
				todo(data)

			elif data[0] == "add-task":
				temp = addtask(data)
				list1.append(temp)
				if data[6] == "todo":
					l2.append(data[3])
			elif data[0] == "print-todoist":
				# temp = addtask(data)
				for each in list1:
					str3 = ""
					for i in each:
						str3 += i + ", "

					print(str3[0: len(str3) -2])
				# print_todoist()

			elif data[0] == "get-next":
				for each in list1:
					print(list1)
					str4 = ""
					for i in each:
						print(str4)
						if list1[6] == "done":
							print("hiiii")
						# print("null")
						else:
							if list1[4] == "y" and list1[5] == "n":
								for i in each:
									str4 += i + ", "
								print(str4[0 : len(str4) - 2])


			elif data[0] == "total-time":
				summ = 0
				for each in l2:
					summ += int(each)
				print(summ)

		except EOFError:
			break
		

if __name__ == '__main__':
	main()