largura=int(input("Digite a largura: "))
altura=int(input("Digite a altura: "))
h=1
while h<=altura:
	a=1
	while a<=largura:
		if h==1 or h==altura:
			print("#",end="")
			a=a+1
		else:
			if a==1 or a==largura:
				print("#",end="")
				a=a+1
			else:
				print(" ",end="")
				a=a+1			
	print()	
	h=h+1
	