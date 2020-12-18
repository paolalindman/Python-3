def ordena(lista):
	fim=len(lista)
	for i in range(fim-1):
		posicao = i
		for j in range(i+1,fim):
			if lista[j]<lista[posicao]:
				posicao=j
		lista[i],lista[posicao] = lista[posicao],lista[i]
	return lista
	