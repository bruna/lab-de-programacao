matriz = {}
for a in range (1,5):
    for b in range (1,5):
        matriz[a,b] = input("Digite o numero da coordenada ("+str(a)+","+str(b)+"): ")

print "\nMatriz:"
medias = []
for a in range (1,5):
    soma = 0
    for b in range (1,5):
        print matriz[a,b],
        soma+= matriz[a,b]    
    medias.append(float(soma/4.0))
    print

print "\nMedias das linhas:"
print medias
