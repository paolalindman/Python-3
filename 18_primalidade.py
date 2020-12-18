n=int(input("Digite um número inteiro: "))
terminou=False
divisor=1
soma=0
while not terminou:
	x=n%divisor
	if x==0:
		soma=soma+1
		divisor=divisor+1
	elif soma==2 and divisor>n:
			terminou=True
	elif soma>2:
			terminou=True
	else:
		divisor=divisor+1				
if soma>2:
	print("não primo")
else:
	print("primo")
	
	