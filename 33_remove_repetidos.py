def remove_repetidos(lista):
	lis=[]
	for i in lista:
		if i not in lis:
			lis.append(i)
	return sorted(lis)
		