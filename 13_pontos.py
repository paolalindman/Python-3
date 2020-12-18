import math
x1=float(input("Digite a coordenada x (x1) do primeiro número: "))
y1=float(input("Digite a coordenada y (y1) do primeiro número: "))
x2=float(input("Digite a coordenada x (x2) do segundo número: "))
y2=float(input("Digite a coordenada y (y2) do segundo número: "))
d=math.sqrt((x1-x2)**2+(y1-y2)**2)
if d>=10:
	print("longe")
else:
	print("perto")	
