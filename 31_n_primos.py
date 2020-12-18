def n_primos(x):
	fator=2
	n=2
	cont=1
	while n>=2 and n<=x:
		while n%fator!=0 and fator<=n/2:
			fator=fator+1
		if n%fator==0:
			primo=False
		else:
			primo=True
			cont=cont+1
		fator=2
		n=n+1
	return cont
				
