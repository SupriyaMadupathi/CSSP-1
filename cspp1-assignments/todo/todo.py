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
	str2 = data[1] + ", " + data[2] + ", " + data[3] + ", "
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
	while True:
		try:
			data = input().split(",")
			if data[0] == "task":
				todo(data)

			elif data[0] == "add-task":
				addtask(data)
			elif data[0] == "print-todoist":
				temp = addtask(data)
				print(temp)
				# print_todoist()

		except EOFError:
			break
		

if __name__ == '__main__':
	main()