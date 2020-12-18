def conta_letras(frase,contar="vogais"):
	frase1=frase.lower()
	frase2=frase1.replace(" ","")
	vogais=frase2.count("a")+frase2.count("e")+frase2.count("i")+frase2.count("o")+frase2.count("u")
	consoantes=len(frase2)-vogais
	if contar == "consoantes":
		return consoantes
	else:
		return vogais
		