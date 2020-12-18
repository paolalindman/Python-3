def incomodam(n):
	if n >= 1:
		return "incomodam " + incomodam(n-1)
	else:
		return ""

def elefantes(n, elefante = 0):
	elefante += 1
	if n <= 1 or elefante >= n:
		return ""
	else:
		if elefante == 1:
			return "Um elefante incomoda muita gente\n"	+ str(2) + " elefantes " + incomodam(2) + "muito mais\n" + elefantes(n,elefante)
		if elefante >= 2:
			return str(elefante) + " elefantes incomodam muita gente\n" + str(elefante+1) + " elefantes " + incomodam(elefante+1) + "muito mais\n" + elefantes(n,elefante)
