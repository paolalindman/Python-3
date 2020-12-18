def soma_matrizes(m1,m2): # soma de matrizes
	soma_matriz=[]
	i_m1 = len(m1)
	j_m1 = len(m1[0])
	i_m2 = len(m2)
	j_m2 = len(m2[0])
	if i_m1 != i_m2 or j_m1 != j_m2:
		return False
	else:
		for i in range(i_m1):
			matriz=[]
			for j in range(j_m1):
				soma = m1[i][j] + m2[i][j]
				matriz.append(soma)
			soma_matriz.append(matriz)
	return soma_matriz