def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
#import sys
abre= ("E8in.txt", "r")
fecha= ("E8out.txt", "w")

abrindo = abre.readline()
separando = abrindo.split()

alunos = int(separando[0])
qtdTimes = int(separando[1])

if (2<=alunos<=10000) and (2<=qtdTimes<=1000) and (qtdTimes < alunos):
    tdsJogadores, tdsHabilidades, time = [],[],[]
    
    for i in range(0,alunos):
        pessoa = abre.readline().strip("\n").split()
        tdsHabilidades.append(int(pessoa[1])) 
        tdsJogadores.append(pessoa)
        bubbleSort(tdsHabilidades)
    
    for a in range (0,qtdTimes):
        time.append([])
 
    for i in range (len(tdsJogadores)-1):	
        while int(tdsJogadores[i+1][1]) > int(tdsJogadores[i][1]):
            if i < 0:
                break
            x = tdsJogadores[i]
            tdsJogadores[i] = tdsJogadores[i+1]
            tdsJogadores[i+1]= x 
            i-=1
    
    while len(tdsJogadores) > 0:
        for x in range (qtdTimes):
            if len(tdsJogadores) == 0 :
                break
            time[x].append(tdsJogadores[0][0])
            del tdsJogadores[0]

for pos in range(0,qtdTimes):
        if pos > 0:
            fecha.write("\n")
        salvar = ("Time ",str(pos+1)+"\n")
        bubbleSort(time[pos])
        for aux in range(0,len(time[pos])):
            time[pos][aux]+= "\n"
        fecha.write("".join(salvar))
        if pos < qtdTimes:
            fecha.write("".join(time[pos]))
abre.close()
fecha.close()

