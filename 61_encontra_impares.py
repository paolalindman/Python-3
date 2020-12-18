def encontra_impares(lista):

	if len(lista) == 1:
		if lista[0]%2 != 0:
			return [lista[0]]
		else:
			return []
	
	else:
		if lista[0]%2 == 0:
			return encontra_impares(lista[1:])
		else:
			lista_impares = [lista[0]]
			lista_impares.extend(encontra_impares(lista[1:]))
			return lista_impares