class No():
    def __init__(self, chave, dado):
        self._dado = dado
        self._filhoesquerdo = None
        self._filhodireito = None
        self._pai = None
        self._chave = chave
        
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
    def setFilhoEsquerdo(self, E):
        self._filhoesquerdo = E
        
    def getFilhoDireito(self):
        return self._filhodireito
    def setFilhoDireito(self, D):
        self._filhodireito = D
        
    def getPai(self):
        return self._pai
    def setPai(self, P):
        self._pai = P
        
    def __str__(self):
        return str(str(self.getChave())+ " " )
        
class ArvoreBinaria():
    def __init__(self):
        self._raiz = None
        
    def getRaiz(self):
        return self._raiz
    def setRaiz(self, R):
        self._raiz = R
        
    def percorrerEmOrdem(self, r):
        if r != None:
            self.percorrerEmOrdem(r.getFilhoEsquerdo())
            fecha.write(str(r.getDado())+ " ")
            self.percorrerEmOrdem(r.getFilhoDireito())
            
    def percorrerPreOrdem(self, r):
        if r != None:
            fecha.write(str(r.getDado())+ " ")
            self.percorrerEmOrdem(r.getFilhoEsquerdo())
            self.percorrerEmOrdem(r.getFilhoDireito())            
            
            
    def percorrerPosOrdem(self, r):
        if r != None:
            self.percorrerEmOrdem(r.getFilhoEsquerdo())
            self.percorrerEmOrdem(r.getFilhoDireito())             
            fecha.write(str(r.getDado())+" ")                       
        
    def busca(self, x, k):
        if (x== None) or (x.getChave() == k):
            return x
        if k < x.getChave():
            return self.busca(x.getFilhoEsquerdo(), k)
        else:
            return self.busca(x.getFilhoDireito(), k)
    
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
            if z.getChave() <= x.getChave():
                x = x.getFilhoEsquerdo()
            else:
                x = x.getFilhoDireito()
        z.setPai(y) 
        
        if y == None:
            self.setRaiz(z)
        else:
            if z.getChave() <= y.getChave():
                y.setFilhoEsquerdo(z)
            else:
                y.setFilhoDireito(z)              
                
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
    
    def leftRotate(self, t, x): 
        y = x.getFilhoDireito()
        x.setFilhoDireito(y.getFilhoEsquerdo())
        x = y.getFilhoEsquerdo().getPai()
        y.setPai(x.getPai())
        if x.getPai() == None:
            t.setRaiz(y)
        else:
            if x == x.getPai().getFilhoEsquerdo():
                x.getPai().setFilhoEsquerdo(y)
            else:
                x.getPai().setFilhoDireito(y)
        y.setFilhoEsquerdo(x)
        x.setPai(y)
        
    def rightRotate(self, t, x):
        y = x.getFilhoEsquerdo()
        x.setFilhoEsquerdo(y.getFilhoDireito())
        x = y.getFilhoDireito().getPai()
        y.setPai(x.getPai())
        if x.getPai() == None:
            t.setRaiz(y)
        else:
            if x == x.getPai().getFilhoDireito():
                x.getPai().setFilhoDireito(y)
            else:
                x.getPai().setFilhoEsquerdo(y)
        y.setFilhoDireito(x)
        x.setPai(y)  
        
import sys        
abre = open(sys.argv[1], "r")
fecha = open(sys.argv[2],"w") 
comandos = abre.read()
comandos = comandos.split("\n")
caso = 1

for i in comandos:
    if i.isdigit():
        arvore = ArvoreBinaria()
        fecha.write("Caso "+ str(caso)+ ":\n" )
        caso+=1
        
    if i.startswith("A"):
        primeiro = i.split(" ")
        del primeiro[0]
        for a in primeiro:
            chave = int(a)
            valor = str(a) 
            arvore.inserir(No(chave, valor))
    
    if i.startswith("B"):
        segundo = i.split(" ")
        del segundo[0]
        for b in segundo:
            chavedeK = int(b)
            if arvore.busca(arvore.getRaiz(), chavedeK) != None:
                arvore.remover(arvore.busca(arvore.getRaiz(), chavedeK))

    
    if i.startswith("C"):
        terceiro = i.split(" ")
        del terceiro[0]
        for j in terceiro:
            newChave = int(j)
            q = arvore.busca(arvore.getRaiz(), newChave)
            if q != None:
                if q.getChave() != newChave:
                    ant = arvore.antecessor(q)
                if q.getChave() == newChave:
                    while q.getChave() == newChave:
                
                        ant = arvore.antecessor(q)
                        q = ant

                if ant == None:
                    fecha.write("0\n")
                else:
                    fecha.write(str(ant.getDado())+ "\n")
            if q == None or arvore.getRaiz() == None:
                fecha.write("0\n")
                
    if i == "PRE":
        raiz = arvore.getRaiz()
        if raiz == None:
            fecha.write("0\n")
        else:
            arvore.percorrerPreOrdem(raiz)
            fecha.write("\n")

    if i == "IN":
        raiz = arvore.getRaiz()
        if raiz == None:
            fecha.write("0\n")
        else:
            arvore.percorrerEmOrdem(raiz)
            fecha.write("\n")
            
    if i == "POST":
        raiz = arvore.getRaiz()
        if raiz == None:
            fecha.write("0\n")
        else:
            arvore.percorrerPosOrdem(raiz)
            fecha.write("\n")

abre.close()
fecha.close()