#ta com um \n a mais no final
#nao consegui tirar de jeito nenhum :(

class no():
    def __init__(self, chave, dado):
        self._dado = dado
        self._filhoesquerdo = None
        self._filhodireito = None
        self._pai = None
        self._chave = chave
        self.fatorBalanceamento = None
        
    def getFatorBalanceamento(self):
        return self.fatorBalanceamento
    def setFatorBalanceamento(self, F):
        self.fatorBalanceamento = F
        
    def getChave(self):
        return self._chave
    def setChave(self, x):
        self._chave = x
        
    def getDado(self):
        return self._dado
    def setDado(self, dado):
        self._dado = dado
        
    def getFilhoEsquerdo(self):
        return self._filhoesquerdo
    def setFilhoEsquerdo(self, tudo):
        self._filhoesquerdo = tudo
        
    def getFilhoDireito(self):
        return self._filhodireito
    def setFilhoDireito(self, D):
        self._filhodireito = D
        
    def getPai(self):
        return self._pai
    def setPai(self, P):
        self._pai = P
        
    def __str__(self):
        return str("No: " + str(self.getChave())+ "\t"+ "dado: "+ str(self.getDado()))
        
class arvoreAVL():
    def __init__(self):
        self._raiz = None
        
    def getRaiz(self):
        return self._raiz
    def setRaiz(self, R):
        self._raiz = R
        
    def pNivel(self, x):
        num = 1
        if x == self.getRaiz():
            return 1
        else:
            while x != self.getRaiz():
                num +=1
                x = x.getPai()
            return num
        
    def altura(self, x):
        if x == None:
            return -1
        hesq = self.altura(x.getFilhoEsquerdo())
        hdir = self.altura(x.getFilhoDireito())
        if hesq > hdir:
            return hesq + 1
        return hdir + 1
    
    def fatorBalanceamento(self, x):
        return self.altura(x.getFilhoDireito()) - self.altura(x.getFilhoEsquerdo())
        
    def percorrerEmOrdem(self, r):
        if r != None:
            self.percorrerEmOrdem(r.getFilhoEsquerdo())
            print (r)
            self.percorrerEmOrdem(r.getFilhoDireito())
            
    def buscaArvore(self, x, k):#busca o valor k , na raiz x
        if (x== None) or (x.getChave() == k):
            return x
        if k < x.getChave():
            return self.buscaArvore(x.getFilhoEsquerdo(), k)
        else:
            return self.buscaArvore(x.getFilhoDireito(), k)
    
    def minimo(self, x):
        while x.getFilhoEsquerdo() != None:
            x = x.getFilhoEsquerdo()
        return x
    def maximo(self, x):
        while x.getFilhoDireito() != None:
            x = x.getFilhoDireito()
        return x
    
    def sucessor(self, x):
        if x.getFilhoDireito() != None:
            return self.minimo(x.getFilhoDireito())
        y = x.getPai()
        while y != None and x is y.getFilhoDireito():
            x = y 
            y = y.getPai()
        return y 
    
    def antecessor(self, x):
        if x.getFilhoEsquerdo() != None:
            return self.maximo(x.getFilhoEsquerdo())
        y = x.getPai()
        while y != None and x == y.getFilhoEsquerdo():
            x = y 
            y = y.getPai()
        return y    
            
    def inserir(self, z):
        y = None
        x = self.getRaiz()
        while x != None:
            y = x
            if z.getChave() < x.getChave():
                x = x.getFilhoEsquerdo()
            else:
                x = x.getFilhoDireito()
        z.setPai(y) 
        
        if y == None:
            self.setRaiz(z)
        else:
            if z.getChave() < y.getChave():
                y.setFilhoEsquerdo(z)
            else:
                y.setFilhoDireito(z)
        self.balancear(z)        
                
    def remover(self, z):
        if z.getFilhoEsquerdo()==None or z.getFilhoDireito()==None:
            y = z 
        else: 
            y = self.sucessor(z)
        
        if y.getFilhoEsquerdo() != None:
            x = y.getFilhoEsquerdo()
        else:
            x = y.getFilhoDireito()
        if x != None:
            x.setPai(y.getPai())
        if y.getPai() == None:
            self.setRaiz(x)
        else:
            if y == y.getPai().getFilhoEsquerdo():
                y.getPai().setFilhoEsquerdo(x)
            else:
                y.getPai().setFilhoDireito(x)
        if y != z:
            z.setChave(y.getChave())
            z.setDado(y.getDado())
               
    def rotateLeft(self, x): 
        y = x.getFilhoDireito()
        x.setFilhoDireito(y.getFilhoEsquerdo())
        if y.getFilhoEsquerdo()!= None:
            y.getFilhoEsquerdo().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRaiz(y)
        else:
            if x == x.getPai().getFilhoEsquerdo():
                x.getPai().setFilhoEsquerdo(y)
            else:
                x.getPai().setFilhoDireito(y)
        y.setFilhoEsquerdo(x)
        x.setPai(y)
        
    def rotateRight(self, x):
        y = x.getFilhoEsquerdo()
        x.setFilhoEsquerdo(y.getFilhoDireito())
        if y.getFilhoDireito()!= None:
            y.getFilhoDireito().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRaiz(y)
        else:
            if x == x.getPai().getFilhoDireito():
                x.getPai().setFilhoDireito(y)
            else:
                x.getPai().setFilhoEsquerdo(y)
        y.setFilhoDireito(x)
        x.setPai(y)  

    def doubleRotateRight(self, x): 
        filhoesq = x.getFilhoEsquerdo()
        self.rotateLeft(filhoesq)
        self.rotateRight(x)
        
    def doubleRotateLeft(self, x):
        filhodir = x.getFilhoDireito()
        self.rotateRight(filhodir)
        self.rotateLeft(x)

    def balancear(self, z): 
        while z!= None:
            a = self.fatorBalanceamento(z)
            filesquerdo= z.getFilhoEsquerdo()
            fildireito = z.getFilhoDireito()
            if a >1:
                if self.fatorBalanceamento(fildireito) < 0:
                    self.doubleRotateLeft(z)
                else:
                    self.rotateLeft(z)
            if a < -1:
                if self.fatorBalanceamento(filesquerdo) > 0:
                    self.doubleRotateRight(z)
                else:
                    self.rotateRight(z)
            z = z.getPai()
        
        
import sys
a= open(sys.argv[1], "r")
fecha = open(sys.argv[2],"w") 
      
tudo = a.read()
tudo = tudo.split("\n")

for i in tudo:
    if i.isdigit():
        minhaArvore = arvoreAVL()
        
    if i == "F":
        minhaArvore = arvoreAVL()
        fecha.write("\n")
        
    if i.startswith("I"):
        um = i.split(" ")
        del um[0]
        for j in um:
            chave = int(j)
            valor = str(j) 
            minhaArvore.inserir(no(chave, valor))
    
    if i.startswith("N"):
        dois = i.split(" ")
        del dois[0]
        for b in dois:
            b = int(b)
            novono = minhaArvore.buscaArvore(minhaArvore.getRaiz(), b)
            if novono == None:
                fecha.write("-1\n")
            else:
                nivel = minhaArvore.pNivel(novono)
                nivel = str(nivel)
                fecha.write(nivel+ "\n")
    
    if i.startswith("L"):
        lista =[]
        tres = i.split(" ")
        del tres[0]
        posium = tres[0]
        posidos = tres[1]
        posium = int(posium)
        posidos =int(posidos)
        
        if posium < posidos: 
            cont = 1
            while cont==1:
                noum = minhaArvore.buscaArvore(minhaArvore.getRaiz(), posium)
                nodois = minhaArvore.buscaArvore(minhaArvore.getRaiz(), posidos)
                if noum != None:
                    valor1 = noum.getDado()
                    lista.append(valor1)
                posium+=1
                if noum == nodois:
                    cont = 2
        if lista:
            for w in lista:
                w= str(w)
                fecha.write(w+" ")
            fecha.write("\n")
        else:
            fecha.write("-1\n")
                
a.close()                
fecha.close()