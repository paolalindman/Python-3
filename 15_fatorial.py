n=int(input("Digite o valor de n: "))
fatorial=n
i=1
while i<n and n!=0:
	fatorial=fatorial*(n-i)
	i=i+1
if n==0:
	fatorial=1	
print(fatorial)
