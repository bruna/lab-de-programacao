# lab-de-programacao

import sys
x = open(sys.argv[1],"r")
bruna = open(sys.argv[2],"w")
y= x.readline()
p= int(y)
for i in range (1, (p+1)):
    z= x.readline()
    b= z.split(" ")
    a=int(b[0])
    c=int(b[1])
    r=""
    for j in range(0,c):
        if (a*j)%c==1:
            r+= "Caso " + str(i) + ":" + str(j)+ "\n"
            bruna.write(r)
            break
    else:
        r=r+ "Caso" + str(i)+ ": muito dificil\n"
        bruna.write(r)
x.close()
bruna.close()
