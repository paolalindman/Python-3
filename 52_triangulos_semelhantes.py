class Triangulo:
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c
		
	def perimetro(self):
		return self.a+self.b+self.c
		
	def tipo_lado(self):
		soma=0
		if self.a/self.b == 1:
			soma +=1
		if self.a/self.c == 1:
			soma+=1
		if self.b/self.c == 1:
			soma+=1
		if soma == 1:
			return "isósceles"
		if soma == 3:
			return "equilátero"
		if soma == 0:
			return "escaleno"
	
	def retangulo(self):
		hipotenusa=max(self.a,self.b,self.c)
		soma = self.a + self.b + self.c
		cateto1 = min(self.a,self.b,self.c)
		cateto2 = soma-cateto1-hipotenusa
		if hipotenusa**2 == (cateto1**2+cateto2**2):
			return True
		else:
			return False
		
	def semelhantes(self,triangulo):
		lista1 = [self.a,self.b,self.c]
		lista2 = [triangulo.a,triangulo.b,triangulo.c]
		lista1.sort()
		lista2.sort()
		div1 = lista1[0]/lista2[0]
		div2 = lista1[1]/lista2[1]
		div3 = lista1[2]/lista2[2]
		if div1==div2==div3:
			return True		
		else:
			return False
		