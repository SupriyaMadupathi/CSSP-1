def nnl(nl): # non nested list function
	nn = []
	for x in nl:
		if type(x) == type(5):
			nn.append(x)
		if type(x) == type([]):
			n = nnl(x)
		for y in n:
	        nn.append(y)

	return sum(nn)


	 print(nnl([[9, 4, 5], [3, 8,[5]], 6])) # output:[9,4,5,3,8,5,6]

	 a = sum(nnl([[9, 4, 5], [3, 8,[5]], 6]))