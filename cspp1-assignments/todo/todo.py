def todo(data):
	
	str1 = ""
	if int(data[3]) < 1:
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
			str1 += "Urgent" + ","
			# print(str1)
		else: 
			str1+= "Not Urgent " + ", "
		# print(str1)

		if data[6] == "todo" or data[6] == "done":
			str1+= "todo"
		else:
			data[6] != todo or data[6] != done
			str1="Invalid status dud"		
		# else:
			# str2 += "Invalid status"
		# 	continue
	print(str1)

def main():
	data = input().split(",")
	if data[1] == "":
		print("Title not provided")
	
	if data[0] == "task":
		todo(data)
		

if __name__ == '__main__':
	main()