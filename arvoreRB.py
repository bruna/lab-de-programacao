'''
Created on 04/11/2015

@author: Bruna
'''

class Node():
    def __init__(self, chave, dado):
        self._value = dado
        self._left = None
        self._right = None
        self._father = None
        self._key = chave
        self._color= "red"
        
    def getValue(self):
        return self._value
    def setValue(self, newValue):
        self._value = newValue
        
    def getRight(self):
        return self._right
    def setRight(self, newRight):
        self._right = newRight
        
    def getLeft(self):
        return self._left
    def setLeft(self, newLeft):
        self._left = newLeft
        
    def getKey(self):
        return self._key
    def setKey(self, newKey):
        self._key = newKey
        
    def getFather(self):
        return self._father
    def setFather(self, newFather):
        self._father = newFather
        
    def getColor(self):
        return self._color
    def setColor(self, newColor):
        self._color = newColor

    def __str__(self):
        return str("No: " + str(self.getKey())+ "\t"+ "dado: "+ str(self.getValue()))
 
 
class arvoreRB():
    
    def __init__(self):
        self.none = Node(None, None)
        self.none.setFather(self.none)
        self.none.setLeft(self.none)
        self.none.setRight(self.none)
        self.none.setColor("black")
        self._root = self.none
            
    def getRoot(self):
        return self._root
    def setRoot(self, R):
        self._root = R
       
    def rotateLeft(self, x): #t eh a arvore, e x o no
        y = x.getRight()
        x.setRight(y.getLeft())
        if y.getLeft()!= self.none:
            y.getLeft().setFather(x)
        y.setFather(x.getFather())
        if x.getFather() == self.none:
            self.setRoot(y)
        elif x == x.getFather().getLeft():
            x.getFather().setLeft(y)
        else:
            x.getFather().setRight(y)
        y.setLeft(x)
        x.setFather(y)
        
    def rotateRight(self, x):
        y = x.getLeft()
        x.setLeft(y.getRight())
        if y.getRight()!= self.none:
            y.getRight().setFather(x)
        y.setFather(x.getFather())
        if x.getFather() == self.none:
            self.setRoot(y)
        elif x == x.getFather().getRight():
            x.getFather().setRight(y)
        else:
            x.getFather().setLeft(y)
        y.setRight(x)
        x.setFather(y)

    def doubleRotateRight(self, x): #x eh no
        filhoesq = x.getLeft()
        self.rotateLeft(filhoesq)
        self.rotateRight(x)
        
    def doubleRotateleft(self, x):
        filhodir = x.getRight()
        self.rotateRight(filhodir)
        self.rotateLeft(x)
        
    def rbInsert(self, z):
        y = self.none
        x = self.getRoot()
        while x != self.none:
            y = x
            if z.getKey() < x.getKey():
                x = x.getLeft()
            else:
                x = x.getRight()
        z.setFather(y)
        if y == self.none:
            self.setRoot(z)
        elif z.getKey() < y.getKey():
            y.setLeft(z)
        else:
            y.setRight(z)
        z.setLeft(self.none)
        z.setRight(self.none)
        z.setColor("red")
        
        self.insertFixUp(z)
        
    def insertFixUp(self, z):
        while z.getFather().getColor()== "red":
            if z.getFather() == z.getFather().getFather().getLeft():
                y = z.getFather().getFather().getRight()
                if y.getColor() == "red":
                    z.getFather().setColor("black")
                    y.setColor("black")
                    z.getFather().getFather().setColor("red")
                    z = z.getFather().getFather()
                else:    
                    if z == z.getFather().getRight():
                        z = z.getFather()
                        self.rotateLeft(z)
                    z.getFather().setColor("black")
                    z.getFather().getFather().setColor("red")
                    self.rotateRight(z.getFather().getFather())
            else:#aki tem q trocar esquerda por direita
                y = z.getFather().getFather().getLeft()
                
                if y.getColor() == "red":
                    z.getFather().setColor("black")
                    y.setColor("black")
                    z.getFather().getFather().setColor("red")
                    z = z.getFather().getFather()
                else:
                    if z == z.getFather().getLeft():
                        z = z.getFather()
                        self.rotateRight(z)
                    z.getFather().setColor("black")
                    z.getFather().getFather().setColor("red")
                    self.rotateLeft(z.getFather().getFather())
        self.getRoot().setColor("black")
     
     
    def percorrerEmOrdem(self, r):
        if r != self.none:
            self.percorrerEmOrdem(r.getLeft())
            print (r)
            self.percorrerEmOrdem(r.getRight())
            
    def rbTransplant(self, u, v):
        if u.getFather() == self.none:
            self.setRoot(v)
        elif u == u.getFather().getLeft():
            u.getFather().setLeft(v)
        else:
            u.getFather().setRight(v)
        v.setFather(u.getFather())
        
    def TreeMinimum(self, x):
        while x.getLeft() != self.none:
            x = x.getLeft()
        return x
    def TreeMaximum(self, x):
        while x!= self.none:
            x = x.getRight()
        return x
    def treeSucessor(self, x):
        if x.getRight() != self.none:
            return self.TreeMinimum(x.getRight())
        y = x.getFather()
        while y != self.none and x ==y.getRight():
            x = y
            y = y.getFather()
        return y       
            
             
    def rbDeleteNumDois(self, z):
        if (z.getLeft() == self.none) or (z.getRight() == self.none):
            y = z 
        else:
            y = self.treeSucessor(z)
        if y.getLeft() != self.none:
            x = y.getLeft()
        else:
            x= y.getRight()
        x.setFather(y.getFather())
        if y.getFather() == self.none:
            self.setRoot(x)
        else:
            if y == y.getFather().getLeft():
                y.getFather().setLeft(x)
            else:
                y.getFather().setRight(x)
        if y != z:
            z.setKey(y.getKey())
        
        if y.getColor() == "black":
            self.rbDeleteFixUp(x)
        return y
        
    def rbDelete(self, z):
        y = z 
        yOriginalColor = y.getColor()
        if z.getLeft() == self.none:
            x = z.getRight()
            self.rbTransplant(z, z.getRight())
        elif z.getRight() == self.none:
            x = z.getLeft()
            self.rbTransplant(z, z.getLeft())
        else:
            y = self.TreeMinimum(z.getRight())
            yOriginalColor = y.getColor()
            x = y.getRight()
            if y.getFather() == z:
                x.setFather(y)
            else:
                self.rbTransplant(y, y.getRight())
                y.setRight(z.getRight())
                y.getRight.setFather(y)
            self.rbTransplant(z, y)
            y.setLeft(z.getLeft())
            y.getLeft().setFather(y)
            y.setColor(z.getColor())
        if yOriginalColor == "black":
            self.rbDeleteFixUp(x)
             
    def rbDeleteFixUp(self, x):
        while (x != self.getRoot()) and (x.getColor() == "black"):
            if x == x.getFather().getLeft():
                w = x.getFather().getRight()
                if w.getColor() == "red":
                    w.setColor("black")
                    x.getFather().setColor("red")
                    self.rotateLeft(x.getFather())
                    w = x.getFather().getRight()
                if (w.getLeft().getColor() == "black") and (w.getRight().getColor() == "black"):
                    w.setColor("red")
                    x = x.getFather()
                else:
                    if w.getRight().getColor() == "black":
                        w.getLeft().setColor("black")
                        w.setColor("red")
                        self.rotateRight(w)
                        w = x.getFather().getRight()
                    w.setColor(x.getFather().getColor())
                    x.getFather().setColor("black")
                    w.getRight().setColor("black")
                    self.rotateLeft(x.getFather())
                    x = self.getRoot()
            else:
                w = x.getFather().getLeft()
                if w.getColor() == "red":
                    w.setColor("black")
                    x.getFather().setColor("red")
                    self.rotateRight(x.getFather())
                    w = x.getFather().getLeft()
                if (w.getRight().getColor() == "black") and (w.getLeft().getColor() == "black"):
                    w.setColor("red")
                    x = x.getFather()
                else:
                    if w.getLeft().getColor() == "black":
                        w.getRight().setColor("black")
                        w.setColor("red")
                        self.rotateLeft(w)
                        w = x.getFather().getLeft()
                    w.setColor(x.getFather().getColor())
                    x.getFather().setColor("black")
                    w.getLeft().setColor("black")
                    self.rotateRight(x.getFather())
                    x = self.getRoot()
        x.setColor("black")
        
    def buscaArvore(self, x, k):#busca o valor k , na raiz x
        if (x== self.none) or (x.getKey() == k):
            return x#retorna o no
        if k < x.getKey():
            return self.buscaArvore(x.getLeft(), k)
        else:
            return self.buscaArvore(x.getRight(), k)


