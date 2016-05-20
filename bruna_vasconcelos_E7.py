#import sys
abre= open("E7.in", "r")
fecha = open("E7.out","w")
soad = abre.read()
soad = soad.split("\n")

lista1, lista2, listanums, listamaiores = [],[],[],[]

for i in soad: 
    if soad.index(i)%2 == 0:
        lista1.append(i)
    else:
        listanums.append(i)
    
for j in lista1:
    x, y = j.split(" ")
    z = int(x)-int(y) 
    lista2.append(z)   

n=0
listinha, listafinal = [],[]
for b in listanums:
    if lista2[n]==1:
        v= (max(b))
        listafinal.append(v)
    else:
        num =int(lista2[n])
        indice= (num-1)
        scr = []
        for m in b:
            scr.append(m)

        while num>0:
            if (indice < 1):
                numero = max(scr)
                listinha.append(numero)
            else:
                ia = -1*indice
                numax = max(scr[0:ia])
                listinha.append(numax)
                ind = scr.index(numax)
                ind += 1
                del scr[0:ind]
            num -=1
            indice-=1
        listafinal.append(listinha)
        listinha=[]
    n+=1    
 
for juvenal in listafinal:
    conta = ''.join(juvenal)
    fecha.write(conta + "\n")
abre.close()
fecha.close()
