cont = 0
def funcao(n):
    global cont
    if ((int(n))==1):
        cont += 1
        contadorfinal = cont
        cont = 0
        return contadorfinal
    elif((int(n))%2==1):
        cont += 1
        return funcao((3*n)+1) 
    elif((int(n))%2==0):
        cont += 1
        return funcao(n/2)
import sys
abre = open(sys.argv[1]), 'r')
fecha = open(sys.argv[2], 'w')
testes = abre.readline()         
if (int(testes)<=1) and (int(testes)>=100):
    imp = ""
    imp="Numero de termos excederam o limite"
    fecha.write(imp)                   
else:
    for i in range(1,int(testes)+1):
        linha = abre.readline()
        lista_com_aeb = linha.split(" ")
        a = int(lista_com_aeb[0])
        b = int(lista_com_aeb[1])
        imp = " "
        if (a >= 1) and (a <= 10**5) and (b>=1) and (b<=10**5):
            resultados =[]
            for numero in range(a,(b+1)):
                resultados.append(funcao(numero))
            maior_resultado = max(resultados)
            imp ="Caso "+str(i)+": "+str(maior_resultado)+"\n"
            fecha.writelines(imp)
        else:
            imp ="Caso "+str(i)+": muito dificil\n"
            fecha.writelines(imp)
abre.close()
fecha.close()
