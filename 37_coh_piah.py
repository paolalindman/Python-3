import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma_modulo = 0
    i = 0
    while i < len(as_a):
   		modulo = abs(as_a[i]-as_b[i])
   		soma_modulo = soma_modulo + modulo
   		i = i + 1
   		Sab = soma_modulo / 6
    return Sab
    
    pass
   		
   		
def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = []
    for sentenca in sentencas:
    	frase = separa_frases(sentenca)
    	frases = frases + frase
    lista_palavras = []
    for frase in frases:
    		palavras = separa_palavras(frase)
    		lista_palavras = lista_palavras + palavras
    soma_tamanhos=0
    total_palavras=0
    for palavra in lista_palavras:
    	tamanho=len(palavra)
    	soma_tamanhos=soma_tamanhos+tamanho
    	total_palavras = total_palavras + 1
    wal_a = soma_tamanhos/total_palavras
    total_palavras_diferentes = n_palavras_diferentes(lista_palavras)
    ttr_a = total_palavras_diferentes/total_palavras
    total_palavras_unicas = n_palavras_unicas(lista_palavras)
    hlr_a = total_palavras_unicas/total_palavras
    carac_sentencas = 0
    conta_sentencas = 0
    for sentenca in sentencas:
    	carac_sentenca = len(sentenca)
    	carac_sentencas = carac_sentencas + carac_sentenca
    	conta_sentencas = conta_sentencas + 1
    sal_a = carac_sentencas/conta_sentencas
    carac_frases = 0
    conta_frases = 0
    for frase in frases:
    	carac_frase = len(frase)
    	carac_frases = carac_frases + carac_frase
    	conta_frases = conta_frases + 1
    pal_a = carac_frases/conta_frases
    sac_a = conta_frases/conta_sentencas
    return [wal_a,ttr_a,hlr_a,sal_a,sac_a,pal_a]
    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve 
    devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_Sab = []
    for texto in textos:
    	as_a = calcula_assinatura(texto)
    	Sab = compara_assinatura(as_a,ass_cp)
    	lista_Sab.append(Sab)
    i=1
    n=0
    min_Sab = lista_Sab[0]
    while i < len(lista_Sab):
    	if lista_Sab[i] < min_Sab:
    		min_Sab = lista_Sab[i]
    		i = i + 1
    		n=i
    	else:
    		i = i + 1
    return n
    print("O autor do texto",n, "está infectado com COH-PIAH")
    pass