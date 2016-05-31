class No:
	def __init__(self,valor=None):
		self._valor=valor
		self._prox=None
		self._ant=None
	def getValor(self):
		return self._valor
	def setValor(self,valor):
		self._valor=valor
	def getProximo(self):
		return self._prox
	def setProximo(self,prox):
		self._prox=prox
	def getAnterior(self):
		return self._ant
	def setAnterior(self,ant):
		self._ant=ant
class ListDuplamenteEncadeada:
	def __init__(self):
		self._inicio =None
		self._fim=None
	def estavazio(self):
		return ((self._inicio==None) and (self._fim==None))

	def inserir(self,valor):
		novono=No(valor)
		if self.estavazio():
			self._inicio=novono	
			self._fim=novono
		else:
			novono.setProximo(self._inicio)
			self._inicio.setAnterior(novono)
			self._inicio=novono
	def getInicio(self):
		return self._inicio
	def buscar(self,valor):
		if self.estavazio():
			return None
		i = self._inicio
		if i.getValor()==None:
			return 
		while(i != None):
			if i.getValor() == valor:
				return i
			i=i.getProximo()
		return -1
	def excluir(self,valor):
		nox = self.buscar(valor)
		noanterior = nox.getAnterior()
		noproximo=nox.getProximo()
		if noanterior == None and noproximo == None:
			nox.setValor(None)
			self._inicio = nox
			self._fim = nox			
		elif noanterior == None:
			noproximo.setAnterior(None)
			self._inicio = noproximo 
		elif noproximo == None:
			noanterior.setProximo(None)
			self._fim = noanterior
		else:
			noanterior.setProximo(noproximo)
			noproximo.setAnterior(noanterior)		
		

	def imprime(self):
		i = self._inicio
		cont = 0
		while(i != None):
			print (i.getValor(), end = " ")
			i = i.getProximo()
		print()
		return None

class pilha(ListDuplamenteEncadeada):

	def __init__(self):
		ListDuplamenteEncadeada.__init__(self)
	
	def empilhar(self,valor):
		self.inserir(valor)
	def desempilhar(self):
		elemento = self._inicio.getValor()
		self.excluir(self._inicio.getValor())
		print(elemento)
		return elemento

class fila(ListDuplamenteEncadeada):
	def __init__(self):
		ListDuplamenteEncadeada.__init__(self)
	def Entra(self,valor):
		self.inserir(valor)
	def Sai(self):
		elemento = self._fim.getValor()
		self.excluir(elemento)
		print(elemento)
		return elemento
		
f = fila()
f.Entra(6)
f.Entra(5)
f.Entra(7)
f.Entra(2)
f.Entra(8)
f.Entra(4)
f.imprime()
f.Sai()
f.imprime()
f.Sai()
f.imprime()

		
		
'''

p = pilha()
p.empilhar(1)
p.empilhar(2)
p.empilhar(3)
p.imprime()
p.desempilhar()
print()
p.imprime()
'''


'''
lista = ListDuplamenteEncadeada()
lista.inserir(1)
lista.inserir(2)
lista.inserir(5)
lista.inserir(7)
lista.inserir(10)
lista.inserir(3)
lista.imprime()
print()
print()
lista.excluir(3)
lista.imprime()
lista.excluir(1)
lista.imprime()
lista.excluir(2)
lista.excluir(10)
lista.excluir(7)
lista.imprime()
lista.excluir(5)
lista.imprime()
'''