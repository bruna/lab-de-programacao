import random

print "##O numero de colunas da primeira matriz deve ser igual ao numero de linhas da segunda##\n"
linhas1 = input("Quantas linhas a primeira Matriz tem? ")
colunas1 = input("Quantas colunas a primeira Matriz tem? ")
linhas2 = input("Quantas linhas a segunda Matriz tem? ")
colunas2 = input("Quantas colunas a segunda Matriz tem? ")
if colunas1 != linhas2:
    print "O numero de colunas da primeiras matriz nao eh igual ao numero de linhas da segunda"
else:
    matriz1, matriz2, matriz3 = {}, {}, {}
    #Matriz 1 - dados
    for i in range (1, linhas1 + 1):
        for j in range (1, colunas1 + 1):
            matriz1[i,j] = random.randint(1,9)
    #Matriz 2 - dados
    for i in range (1, linhas2 + 1):
        for j in range (1, colunas2 + 1):
            matriz2[i,j] = random.randint(1,9)
    #Matriz 3 - dados da Multiplicacao
    for i in range (1, linhas1 + 1):        
        for j in range (1, colunas2 + 1):                        
            matriz3[i,j] = 0
            fim = 1
            while fim <= (linhas2):
                matriz3[i,j] += (matriz1[i, fim] * matriz2[fim, j])
                fim += 1

    #Impressoes em forma de matriz
    print "Matriz 1:"
    for i in range (1, linhas1 + 1):
        for j in range (1, colunas1 + 1):
            print matriz1[i,j],
        print

    print "Matriz 2:"
    for i in range (1, linhas2 + 1):
        for j in range (1, colunas2 + 1):
            print matriz2[i,j],
        print

    print "Matriz 3 - Multiplicacao:"
    for i in range (1, linhas1 + 1):        
        for j in range (1, colunas2 + 1):
            print matriz3[i,j],
        print
