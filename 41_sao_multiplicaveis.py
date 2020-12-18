def sao_multiplicaveis(m1,m2): #retorna se uma matriz é multiplicável por outra, ou seja, 
							   #se o num de colunas de m1 é igual ao num delinhas de m2
	j_m1 = len(m1[0])
	i_m2 = len(m2)
	if j_m1 == i_m2:
		return True
	else:
		return False
		