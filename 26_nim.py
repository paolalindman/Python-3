def partida():
	n=int(input("Quantas peças? "))
	m=int(input("Limite de peças por jogada? "))
	print()
	while m>=n:
		print("Limite de peças inválido. Escolha novamente.")
		print()
		m=int(input("Limite de peças por jogada? "))
		print()
	if n%(m+1)==0:
		print("Você começa!")
		print()
		i=usuario_escolhe_jogada(n,m)
		soma=1
		n=n-i
		if n>1:
			print("Agora restam",n,"peças no tabuleiro")
			print()
		if n==1:
			print("Agora resta apenas uma peça no tabuleiro.")
			print()	
	else:
		print("Computador começa!")
		print()
		i=computador_escolhe_jogada(n,m)
		soma=2
		n=n-i
		print("Agora restam",n,"peças no tabuleiro")
		print()
	while n>0:
		if soma%2!=0:
			i=computador_escolhe_jogada(n,m)
			n=n-i
		else:
			i=usuario_escolhe_jogada(n,m)
			n=n-i
		if n>1:
			print("Agora restam",n,"peças no tabuleiro")
			print()
		if n==1:
			print("Agora resta apenas uma peça no tabuleiro.")
			print()	
		soma=soma+1
	if n<=0:
		if soma%2==0:
			print("Fim do jogo! O computador ganhou!")
			print()
		else:
			print("Fim do jogo! Você ganhou!")
			print()
	return soma		
			
def computador_escolhe_jogada(n,m):
	i=0
	computador=True
	while computador:
		while i<=m and computador:
			x=n-i
			if x%(m+1)!=0:
				i=i+1
				computador=True
			else:	
				if i==1:
					print("O computador tirou 1 peça.")
					computador=False
				else:
					if i==0:
						i=m
						if i==1:
							print("O computador tirou 1 peça.")
							computador=False
						else:
							print("O computador tirou",i,"peças.")
							computador=False
					else:
						print("O computador tirou",i,"peças.")
						computador=False
	return i			
			
def usuario_escolhe_jogada(n,m):
	i=int(input("Quantas peças você vai tirar? "))
	print()
	usuario=True
	while usuario:
		while i<=0 or i>m or m>n:
			print("Oops! Jogada inválida! Tente de novo.")
			i=int(input("Quantas peças você vai tirar? "))
			print()
			usuario=True
		if i==1:
			print("Você tirou 1 peça.")
			usuario=False
		if i>1 and i<=m:
			print("Você tirou",i,"peças")
			usuario=False
	return i

def main():
	print("Bem-Vindo ao jogo do NIM! Escolha: ")
	print()
	escolha=int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
	print()
	joga=True
	while joga:
		while escolha<1 or escolha>2:
			print("Oops! Escolha inválida! Tente de novo!")
			print()
			escolha=int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
			print()
			joga=True
		if escolha==1:
			print("Você escolheu uma partida isolada!")
			print()
			partida()
			joga=False
		if escolha==2:
			print("Você escolheu um campeonato!")
			print()
			campeonato()		
			joga=False
			
def campeonato():
	rodada=1
	computador=0
	voce=0
	while rodada<4:
		print("**** Rodada",rodada,"****")
		print()
		soma=partida()
		if soma%2==0:
			computador=computador+1
		else:
			voce=voce+1
		rodada=rodada+1
	if rodada==4:
		print("**** Final do campeonato! ****")
		print()
		print("Placar: Você",voce,"X",computador,"Computador")
main()			
		
				
		
		
		
	
					
