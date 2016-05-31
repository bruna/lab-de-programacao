matriz = {}
linhas = input("Linhas: ")
colunas = input("Colunas: ")
for i in range (1,linhas+1):
    for j in range (1,colunas+1):
         matriz[i,j] = input("Digite o numero da coordenada ("+str(i)+","+str(j)+"): ")

print "Matriz original: "
for i in range (1,linhas+1):
    for j in range (1,colunas+1):
        print matriz[i,j],
    print

transposta = {}
print "\nMatriz transposta: "
for i in range (1,colunas+1):
    for j in range (1,linhas+1):
        print matriz[j,i],
    print
