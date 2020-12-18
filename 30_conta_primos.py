def n_primos(x):
	n=2
	cont=0
	fator=2
	primo=False
	while n>=2 and n<=x:
		while primo==False and n<=x:
			if n%fator!=0 and fator<=n:
				fator=fator+1
				primo=False	
			if n%fator==0 and n==fator:
				primo=True
				cont=cont+1
			else:
				if n<x:
					primo=False
				else:
					primo=True
		fator=2	
		n=n+1
		primo=False
	
	return cont
x=10
n_primos(x)

