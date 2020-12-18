def primeiro_lex(lista):
	menor=lista[0]
	for i in range(len(lista)):
		if lista[i] < menor:
			menor = lista[i]
		i += 1
	return menor
	