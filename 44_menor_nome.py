def menor_nome(nomes):
	lista_nomes = []
	for i in range(len(nomes)):
		lista_nomes.append(nomes[i].strip().capitalize())
	n=[]
	for i in range(len(lista_nomes)):
		n.append(len(lista_nomes[i]))
	menor_nome = min(n)
	for i in range(len(lista_nomes)):
		if len(lista_nomes[i]) == menor_nome:
			return lista_nomes[i]
			
