matriz = {}
for i in range (1,4):
    for j in range (1,4):
        matriz[i,j] = input("Digite um numero para a posicao (" + str(i) + ", " + str(j) + ") da matriz\n:")

somaPares, somaImpares = 0,0
for i in range (1,4):
    for j in range (1,4):
        if matriz[i,j] % 2 == 0:
            somaPares += matriz[i,j]
        else:
            somaImpares += matriz[i,j]

print "Matriz:"
for i in range (1,4):
    print matriz[i,1], matriz[i,2], matriz[i,3]
print "Soma dos pares:", somaPares
print "Soma dos impares:", somaImpares
