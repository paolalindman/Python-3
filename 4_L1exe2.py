# Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

# Exemplo:

# Entrada de Dados:
# Digite a primeira nota: 4

# Digite a segunda nota: 5

# Digite a terceira nota: 6

# Digite a quarta nota: 7

# Saída de Dados:
# A média aritmética é 5.5

# Dica: uso do print
# Quando você usa o comando print para imprimir mais de uma coisa, ele inclui automaticamente
# espaços entre os argumentos impressos. Cuidado para não incluir espaços demais na sua 
# resposta! O corretor perceberá e tirará pontos


a=input("Digite a primeira nota: ")
b=input("Digite a segunda nota: ")
c=input("Digite a terceira nota: ")
d=input("Digite a quarta nota: ")
x=float(a)
y=float(b)
z=float(c)
o=float(d)
media=(x+y+z+o)/4
print("A média aritmética é",media)