print('xxxxxxxxx    xx     xx  xxxxxxxxx xx    xx  xxxxxxxxx  xx      x')
print('xx     xx    xx     xx  x   x   x xx    xx  xx     xx  x x     x')
print('xx     xx     x     x       x     xx    xx  xx     xx  x  x    x')
print('xxxxxxxxx      xxxxx        x     xxxxxxxx  xx     xx  x   x   x')
print('xx              xxx         x     xx    xx  xx     xx  x    x  x')
print('xx               x          x     xx    xx  xx     xx  x      xx')
print('xx               x          x     xx    xx  xxxxxxxxx  x       x')
print()
print()
conferir = 'P2'
while conferir == 'P2':
    arquivo_de_entrada = input('Digite o nome do novo arquivo, (EX.: minhafoto): ')
    arquivo_de_entrada +='.pgm'
    f = open(arquivo_de_entrada)
    ler = f.readlines()
    conferir = ler[0]
    conferir = conferir[:2]
    if conferir == 'P2':
        break
    else:
        print('O formato do arquivo não é suportado. Por favor, insira uma imagem compativel com o programa.')
        print('A imagem deve ser no formado PGM, númerico. Tente novamente!')
        conferir = 'P2'        
lista1 = []
lista1.extend(ler[3:])
num = int(ler[2])
for x in range(len(lista1)):
    a = lista1[x]
    lista1[x] = a[:-1]
for x in range(len(lista1)):
    lista1[x] = lista1[x].split(' ')
for x in range(len(lista1)):
    lista1[x] = filter(lambda vazio: vazio != '', lista1[x])
lista1 = lista1[:-1]
m_l = 0
m_c = 0
for x in lista1:
    m_l+=1
    if m_c == 0:
        for y in x:
            m_c+=1
for x in range(m_l):
    for y in range(m_c):
        lista1[x][y] = int(lista1[x][y])
def crazy(l):
    listadaslinhas = []
    novalista = []
    for x in range(m_l):
        for y in range(m_c):
            if x == 0 and y == 0:
                l1 = [0,0,0]
                l2 = [0,l[x][y],l[x][y+1]]
                l3 = [0,l[x+1][y],l[x+1][y+1]]          
                k = ((l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2]))*(l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2])) + (l1[2]+2*l2[2]+ l3[2]- (l1[0]+2*l2[0]+ l3[0]))*(l1[2]+2*l2[2]+ l3[2] - (l1[0]+2*l2[0]+ l3[0])))**0
            elif x == m_l -1 and y == m_c -1:
                    l1 = [l[x-1][y-1],l[x-1][y],0]
                    l2 = [l[x][y-1],l[x][y],0]
                    l3 = [0,0,0]
                    k = ((l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2]))*(l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2])) + (l1[2]+2*l2[2]+ l3[2]- (l1[0]+2*l2[0]+ l3[0]))*(l1[2]+2*l2[2]+ l3[2] - (l1[0]+2*l2[0]+ l3[0])))**0.5
                    
            elif x > 0 and x != m_l -1 and y == 0:
                l1 = [0,l[x-1][y],l[x-1][y+1]]
                l2 = [0,l[x][y],l[x][y+1]]
                l3 = [0,l[x+1][y],l[x+1][y+1]]
                k = ((l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2]))*(l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2])) + (l1[2]+2*l2[2]+ l3[2]- (l1[0]+2*l2[0]+ l3[0]))*(l1[2]+2*l2[2]+ l3[2] - (l1[0]+2*l2[0]+ l3[0])))**0.5
            elif x > 0 and x != m_l -1 and y == m_c -1:
                l1 = [l[x-1][y-1],l[x-1][y],0]
                l2 = [l[x][y-1],l[x][y],0]
                l3 = [l[x+1][y-1],l[x+1][y],0]
                k = ((l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2]))*(l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2])) + (l1[2]+2*l2[2]+ l3[2]- (l1[0]+2*l2[0]+ l3[0]))*(l1[2]+2*l2[2]+ l3[2] - (l1[0]+2*l2[0]+ l3[0])))**0.5
            elif x ==0 and y == m_c -1:
                      l1 = [0,0,0]
                      l2 = [l[x][y-1],l[x][y],0]
                      l3 = [l[x+1][y-1],l[x+1][y],0]
                      k = ((l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2]))*(l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2])) + (l1[2]+2*l2[2]+ l3[2]- (l1[0]+2*l2[0]+ l3[0]))*(l1[2]+2*l2[2]+ l3[2] - (l1[0]+2*l2[0]+ l3[0])))**0.5 
            elif x == m_l -1 and y == 0:
                      l1 = [0,l[x-1][y],l[x-1][y+1]]
                      l2 = [0,l[x][y],l[x][y+1]]
                      l3 = [0,0,0]
                      k = ((l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2]))*(l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2])) + (l1[2]+2*l2[2]+ l3[2]- (l1[0]+2*l2[0]+ l3[0]))*(l1[2]+2*l2[2]+ l3[2] - (l1[0]+2*l2[0]+ l3[0])))**0.5
            elif (x > 0 and x < m_l -1) and (y > 0 and y < m_c -1):
                    l1 = [l[x-1][y-1],l[x-1][y],l[x-1][y+1]]
                    l2 = [l[x][y-1],l[x][y],l[x][y+1]]
                    l3 = [l[x+1][y-1],l[x+1][y],l[x+1][y+1]]
                    k = ((l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2]))*(l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2])) + (l1[2]+2*l2[2]+ l3[2]- (l1[0]+2*l2[0]+ l3[0]))*(l1[2]+2*l2[2]+ l3[2] - (l1[0]+2*l2[0]+ l3[0])))**0.5
            elif x == 0 and (y > 0 and y < m_c -1):
                l1 = [0,0,0]
                l2 = [l[x][y-1],l[x][y],l[x][y+1]]
                l3 = [l[x+1][y-1],l[x+1][y],l[x+1][y+1]]
                k = ((l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2]))*(l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2])) + (l1[2]+2*l2[2]+ l3[2]- (l1[0]+2*l2[0]+ l3[0]))*(l1[2]+2*l2[2]+ l3[2] - (l1[0]+2*l2[0]+ l3[0])))**0.5
            elif x == m_l - 1 and (y > 0 and y < m_c -1):
                l1 = [l[x-1][y-1],l[x-1][y],l[x-1][y+1]]
                l2 = [l[x][y-1],l[x][y],l[x][y+1]]
                l3 = [0,0,0]
                k = ((l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2]))*(l3[0]+2*l3[1]+ l3[2] - (l1[0]+2*l1[1]+ l1[2])) + (l1[2]+2*l2[2]+ l3[2]- (l1[0]+2*l2[0]+ l3[0]))*(l1[2]+2*l2[2]+ l3[2] - (l1[0]+2*l2[0]+ l3[0])))**0.5
            if k > num:
                k = num
            elif k < 0:
                k = 0
            listadaslinhas.append(int(k))
        novalista.append(listadaslinhas)
        listadaslinhas = filter(lambda x: x == 'none',listadaslinhas)                               
    return novalista
novalista = crazy(lista1)
contador = 0
for x in novalista:
    for y in x:
        if y >= contador:
            contador = y        
contador = str(contador)+ '\n'
for listas in novalista:
    listas.append('\n')
for listas in range(len(novalista)):
    for valores in range(m_c):
        novalista[listas][valores] = str(novalista[listas][valores])+ ' '
novo_nome = input('Digite o nome do seu arquivo de saída. (OBS.: O novo nome deve ser diferente do arquivo orignal!!!) \n:')
novo_nome+='.pgm'
novoarquivo = open(novo_nome,'w')
for x in range(3):
    novoarquivo.write(ler[x])
novoarquivo = open(novo_nome,'a')
for x in novalista:
    for y in x:
        novoarquivo.write(y)
novoarquivo.close()
print ('O arquivo ' + arquivo_de_entrada + ' foi convertido, e gerou uma nova imagem: ' + novo_nome)


        



















            
