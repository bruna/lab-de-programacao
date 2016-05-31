matriz = {}
for a in range (1,5):
    for b in range (1,5):
        matriz[a,b] = input("Digite: ")

print "\nMatriz:"
for a in range (1,5):
    for b in range (1,5):
        print matriz[a,b],
    print

for c in range (1,5):
    valor = matriz[2,c]
    matriz[2,c] = matriz[3,c]
    matriz[3,c] = valor
    valor = matriz[1,c]
    matriz[1,c] = matriz[4,c]
    matriz[4,c] = valor

print "\nMatriz modificada:"
for a in range (1,5):
    for b in range (1,5):
        print matriz[a,b],
    print
