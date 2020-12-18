def insertion_sort(lista):
	for i in range(1,len(lista)):
		elemento = lista[i]
		posicao = i
		
		while posicao > 0 and lista[posicao-1] > elemento:
			lista[posicao] = lista[posicao-1]
			posicao = posicao - 1
		
		lista[posicao] = elemento
	
	return lista
	