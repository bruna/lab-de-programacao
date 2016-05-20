def quicksort(vetor):
    if len(vetor) <= 1:
        return vetor
    menores, igual, maiores = [],[],[]
    pivo = vetor[0]
    for x in vetor:
        if x > pivo:
            menores.append(x)
        elif x == pivo:
            igual.append(x)
        else:
            maiores.append(x)
    return quicksort(menores)+igual+quicksort(maiores)

abre = open("1.txt","r")
fecha = open("2.txt","w")
lista = abre.read().split("\n")
pessoas = int(lista[0])
qtdDeBolos = int(lista[1])
y = lista[2].split(" ")
bolos = []
for i in range(qtdDeBolos):
	bolos.append(int(y[i]))

bolos = quicksort(bolos)
esquerdo = 0
lista = list(range(1,bolos[0]+1))
direito = len(lista)-1
maxtam = 0

parar = False
posi = (direito + esquerdo)//2
metade = lista[posi]
todo = 0

while parar == False:
	if esquerdo > direito:
		parar = True
		break
	for j in range (len(bolos)):
		if metade <= bolos[j]:
			todo+=bolos[j]//metade
		else:
			break
	if todo < pessoas:
		direito = posi - 1 
		posi = (direito + esquerdo)//2
		metade = lista[posi]
	else:
		if maxtam < metade:
			maxtam = metade
		esquerdo = posi + 1
		posi = (direito + esquerdo)//2
		metade = lista[posi]
	todo = 0
fecha.write(str(maxtam)+"\n")
abre.close()
fecha.close()



