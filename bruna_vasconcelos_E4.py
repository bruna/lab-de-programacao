import sys
abre = open(sys.argv[1],"r")
fecha = open(sys.argv[2],"w")
qtd = abre.readline()
nums = abre.readline()
esp = str(nums)
if (2 <= int(qtd) <= 1000):
    separa = esp.split()
    menor = int(separa[0])
    for i in range (len(separa)):
        if int(separa[i])<menor:
            menor = int(separa[i])
    for a in range (menor,int(qtd)+1):
        if str(a) not in separa:
            result = a 
            falta = str(result)+" "
            fecha.write(falta)  
else:
    fecha.write("Numero fora do intervalo")
abre.close()
fecha.close()
