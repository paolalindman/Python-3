n=int(input("Digite um número inteiro: "))
adjacente=False
while n!=0 and not adjacente:
	x=n%10
	n=n//10
	y=n%10
	if x==y:
		adjacente=True	
if adjacente:
	print("sim")
else:
	print("não")
		
