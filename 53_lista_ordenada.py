def ordenada(lista):
	fim = len(lista)
	for i in range (fim-1):
		posicao = i
		for j in range (i+1, fim):
			if lista[i]>lista[j]:
				return False
	return True
				