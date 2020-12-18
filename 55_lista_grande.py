import random
def lista_grande(n):
	lista = []
	for i in range(n):
		numero = random.randint(0,99999)
		lista.append(numero)
	return lista
	