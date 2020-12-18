def é_hipotenusa(h):
	j=1
	hipo=False
	while j>0 and j<=h and hipo==False:
		import math
		i=math.sqrt(h**2-j**2)
		resto=i%1
		if resto==0.0 and i!=0.0:
			hipo=True
			return hipo
		if j==h and hipo==False:
			return hipo	
		j=j+1	


def soma_hipotenusas(n):
	h=1
	soma=0
	while h>=1 and h<=n:
		hipo=é_hipotenusa(h)
		if hipo==True:
			soma=soma+h
		h=h+1
	return soma