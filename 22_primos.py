def éPrimo(k):
	primo=True
	i=2
	while i<k and primo:
		if k%i==0:
			primo=False
		i=i+1
	return primo

def	maior_primo(n):
	while éPrimo(n)==False:
		n=n-1
	if éPrimo(n)==True:
		return n
