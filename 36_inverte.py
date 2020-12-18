n=int(input("Digite um número: "))
lista=[]
while n!=0:
        lista.append(n)
        n=int(input("Digite um número: "))
lista.reverse()
for i in lista:
        print(i)
