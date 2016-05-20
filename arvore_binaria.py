'''
Created on 03/11/2015

@author: Bruna
'''

class No:
    def __init__(self, chave, dado):
        self._filhoesquerdo = None 
        self._filhodireito = None
        self._pai = None 
        self._dado  = dado
        self._chave = chave
        
    def getFilhoEsquerdo(self):
        return self._filhoesquerdo
    def setFilhoEsquerdo(self,esquerdo):
        self._filhoesquerdo = esquerdo
        
    def getFilhoDireito(self):
        return self._filhodireito
    def setFilhoDireito(self,direito):
        self._filhodireito = direito
        
    def getPai(self):
        return self._pai
    def setPai(self,pai):
        self._pai = pai
        
    def getChave(self):
        return self._chave
    def setChave(self,chave):
        self._chave = chave
        
    def getDado(self):
        return self._dado
    def setDado(self,dado):
        self._dado = dado
    def __str__(self):
        s = "chave= " + str(self.getChave()) + " e o dado eh "+self.getDado()
        return s
        
            
class ArvoreBinaria():
    def __init__(self):
        self._raiz = None
        
    def getRaiz(self):
        return self._raiz
    def setRaiz(self,R):
        self._raiz = R
        
    def percorrerPreOrdem(self,r):
        if r != None:
            print(r)
            self.percorrerEmOrdem(r.getFilhoEsquerdo())
            self.percorrerEmOrdem(r.getFilhoDireito())
            
    def percorrerEmOrdem(self,r):
        if r != None:
            self.percorrerEmOrdem(r.getFilhoEsquerdo())
            print (r)
            self.percorrerEmOrdem(r.getFilhoDireito())
            
    def percorrerPosOrdem(self,r):
        if r != None:
            self.percorrerEmOrdem(r.getFilhoEsquerdo())
            self.percorrerEmOrdem(r.getFilhoDireito())
            print (r)
            
    def busca(self, x,k):
        if (x == None) or (k == x.getChave()):
            return x        #retorna o no
        elif (k < x.getChave()):
            return self.busca(x.getFilhoEsquerdo(), k)
        else:
            return self.busca(x.getChave(), k)
        
    def buscaIterativa(self,x,k):
        while (x != None) and (k != x.getChave()):
            if (k < x.getChave()):
                x = x.getFilhoEsquerdo()
                x = x.getFilhoDireito()
        return x
    
    def minimo(self,x):
        while x.getFilhoEsquerdo() != None:
            x = x.getFilhoEsquerdo()
        return x
    
    def maximo(self,x):
        while x.getFilhoDireito() != None:
            x = x.getFilhoDireito()
        return x
    
    def sucessor(self,x):
        if x.getFilhoDireito() != None:
            return self.minimo(x.getFilhoDireito())
        y = x.getPai()
        while (y != None) and (x == y.getFilhoDireito()):
            x = y
            y = y.getPai()
        return y        #pode ser None
    
    def antecessor(self,x):
        if x.getFilhoEsquerdo() != None:
            return self.maximo(x.getFilhoEsquerdo())
        y = x.getPai()
        while (y != None) and (x == y.getFilhoEsquerdo()):
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
                
    def deletar(self,z):
        if (z.setFilhoEsquerdo() ==  None) or (z.setFilhoDireito() == None):
            y = z
        else:
            y = z.sucessor()
            
        if y.setFilhoEsquerdo() != None:
            x = y.setFilhoEsquerdo()
        else:
            x = y.setFilhoDireito()
        
        if x != None:
            x.setPai(y.getPai())
        if y.getPai() == None:
            self.setRaiz(x)
        else:
            if y == y.getPai().getFilhoEsquerdo():
                y.getPai().getFilhoEsquerdo(x)
            else:
                y.getPai().setFilhoDireito(x)
        if y != z:
            z.setChave(y.getChave())
            z.setDado(y.getDado())
        return y
                

################# programa pra testar ##############
                
arvore = ArvoreBinaria()
lista = [30,37,25,24,38,40,50]


for i in lista:
    no = No(i,"bruna")
    arvore.inserir(no)

        
arvore.percorrerPreOrdem(arvore.getRaiz())
print("\n")
arvore.percorrerEmOrdem(arvore.getRaiz())
print("\n")
arvore.percorrerPosOrdem(arvore.getRaiz())

#####################################################           
    
         
class ArvoreAVL(ArvoreBinaria):             
    def altura(self,x):
        if x == None:
            return -1
        h1 = self.altura(x.getFilhoEsquerdo())
        h2 = self.altura(x.getFilhoDireito())
        if h1 > h2:
            return h1 + 1
        return h2 + 1

    def fatorBalanceamento(self,x):
        return self.altura(x.getFilhoEsquerdo()) - self.altura(x.getFilhoDireito())
        
    def leftRotate(self,x): # x eh o no
        y = x.getFilhoDireito()
        x.setFilhoDireito(y.getFilhoEsquerdo) #faz da subarvore esquerda de y a subarvore direita de x 
        if x.getFilhoEsquerdo() != None:
            x = y.getFilhoEsquerdo().setPai(x)
        x.setPai(y.getPai())
        if x.setPai == None:
            self.setRaiz(y)
        else:
            if x == x.getPai(y).getFilhoEsquerdo():
                x.getPai().setFilhoEsquerdo(y)
            else:
                x.getPai().setFilhoDireito(y)
        y.setFilhoEsquerdo(x)
        x.setPai(y)
        
    def rightRotate(self, x):
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



#===============================================================================
#                      teste arvore AVL 
# 
# arvore2 = ArvoreAVL()
# arvore2.inserir(
# arvore2.inserir(20)
# arvore2 = arvore2.percorrerEmOrdem(arvore2.getRaiz())
# arvore2 = arvore2.rightRotate()
# 
# 
#===============================================================================





            
            
        
        
        



            
            
    
    
        
        
    
    