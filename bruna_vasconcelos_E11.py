import sys
from math import floor
class Node:
    def __init__(self, valor):
        self.__valor=valor
        self.__prox=None
    def getValor(self):
        return self.__valor
    def setValor(self,valor):
        self.__valor=valor
    def getProx(self):
        return self.__prox
    def setProx(self,prox):
        self.__prox=prox


         
class Lista:
    def __init__(self):
        self._inicio=None
        self._fim=None
    def getInicio(self):
        return self._inicio.getValor()
    def setInicio(self,inicio):
        self._inicio=inicio
    def getFim(self):
        return self._fim.getValor()
    def setFim(self, fim):
        self._fim=fim
    def add(self, element):
        ad=Node(element)
        if self._inicio==None:
            self._inicio=ad
            self._fim=ad
        else:
            self._fim.setProx(ad)
            self._fim=ad
    def remove(self, element):
        if self._inicio==None:
            print ("Lista vazia")
        elif self._inicio.getValor()==element and self._inicio.getProx()==None:
            self._inicio=None
            self._inicio=None
        elif self._inicio.getValor()==element and self._inicio.getProx()!=None:
            self._inicio=self._inicio.getProx()
        else:
            delet=self._inicio.getProx()
            ant=self._inicio
            found=False
            while delet.getProx()!=None:
                if delet.getValor()==element:
                    ant.setProx(delet.getProx())
                    found=True
                    break
                else:
                    ant=delet
                    delet=delet.getProx()
            if found==False:
                print ("A lista nao tem esse elemento")
    def listar(self):
        if self._inicio==None:
            print ("Lista vazia")
        else:
            ult=self._inicio
            print (ult.getValor())
            while ult.getProx()!=None:
                ult=ult.getProx()
                print (ult.getValor())
    def index(self, elemento=None):
        if elemento==None:
            print ("Falta o valor")
        else:
            i=self._inicio
            cont=0
            found=False
            while i!=None and found==False:
                if elemento==i.getValor():
                    found=True
                else:
                    i=i.getProx()
                    cont+=1
            if found==True:
                return cont
            else:
                return -1
    def indexSearch(self, index):
        ult=self._inicio
        if self.index(ult.getValor())==index:
            return ult.getValor()
        while ult.getProx()!=None:
            ult=ult.getProx()
            if self.index(ult.getValor())==index:
                return ult.getValor()
        print ("Indice fora do intervalo")
    def lenght(self):
        i=self._inicio
        cont=0
        while i!=None:
            i=i.getProx()
            cont+=1
        return cont

class Pilha(Lista):
    def __init__(self):
        Lista.__init__(self)

    def pop(self):
        if self._inicio==None:
            print ("Lista vazia")
            return
        elif self._inicio.getProx()==None:
            element=self._inicio.getValor()
            self._inicio=None
            self._fim=None
            return element
        else:
            delet=self._inicio
            while delet.getProx()!=None:
                ant=delet
                delet=delet.getProx()
            self._fim=ant
            ant.setProx(None)
            return delet.getValor()
    def remove(self):
        if self._inicio==None:
            print ("Lista vazia")
            return
        elif self._inicio.getProx()==None:
            self._inicio=None
            self._fim=None
        else:
            delet=self._inicio
            while delet.getProx()!=None:
                ant=delet
                delet=delet.getProx()
            self._fim=ant
            ant.setProx(None)


tokens=Pilha()
tudo=""
abre=open(sys.argv[1], "r")
fecha=open(sys.argv[2],"w")
for linha in abre:
    tokens.setInicio(None)
    tokens.setFim(None)
    termos=linha.split(" ")
    n=len(termos)
    while n>0:
        n-=1
        try:
            x=int(termos[n])
            tokens.add(x)
        except:
            x=termos[n]
            first=tokens.pop()
            second=tokens.pop()
            if x=="+":
                res=first+second
                tokens.add(res)
            elif x=="-":
                res=first-second
                tokens.add(res)
            elif x=="*":
                res=first*second
                tokens.add(res)
            elif x=="/":
                res=int(float(first)/float(second))
                tokens.add(res)
    tudo+=str(tokens.getInicio())+"\n"

fecha.write(tudo)
abre.close()
fecha.close()
