import sys
class Nodo:
    def __init__(self, valor):
        self.__valor = valor
        self.__proximo = None
    def getValor(self): return self.__valor
    def setValor(self, valor): self.__valor = valor
    def getProximo(self): return self.__proximo
    def setProximo(self, proximo): self.__proximo = proximo

class Lista:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
    def getPrimeiro(self): return self.__primeiro
    def getUltimo(self): return self.__ultimo
    def inserirInicio(self, valor):
        NOVO = Nodo(valor)
        if self.__primeiro == None:
            self.__primeiro = NOVO
            self.__ultimo = self.__primeiro
        else:
            self.__ultimo.setProximo(NOVO)
            self.__ultimo = NOVO
    def removerInicio(self):
        if self.__primeiro == None: return
        if self.__primeiro == self.__ultimo:
            self.__primeiro = None
            self.__ultimo = None
        else:
            self.__primeiro = self.__primeiro.getProximo()
    def inserirFim(self, valor):
        NOVO = Nodo(valor)
        if self.__primeiro == None:
            self.__primeiro = NOVO
            self.__ultimo = self.__primeiro
        else:
            self.__ultimo.setProximo(NOVO)
            self.__ultimo = NOVO
    def removerFim(self):
        if self.__primeiro == None: return
        if self.__primeiro == self.__ultimo:
            self.__primeiro = None
            self.__ultimo = None
        else:
            nodoAuxiliar = self.__primeiro
            while nodoAuxiliar.getProximo() != self.__ultimo:
                nodoAuxiliar = nodoAuxiliar.getProximo()
            nodoAuxiliar.setProximo(None)
            self.__ultimo = nodoAuxiliar

abre = open(sys.argv[1], "r")
fecha=open(sys.argv[2],"w")
festas = int(abre.readline())
texto=""
if festas < 1 or festas > pow(10,5):
    print("Caso fora do intervalo")
else:
    for n in range(festas):
        oscara = []
        listabaralho = abre.readline().rstrip("\n").split()
        baralho = Lista()
        for i in listabaralho:
            baralho.inserirFim(i)
        linha = abre.readline().rstrip("\n")
        while linha != "-1":        
            deckConvidado = linha.split(" ")
            cara = Lista()
            for i in deckConvidado:
                cara.inserirFim(i)
            oscara.append(cara)
            linha = abre.readline().rstrip("\n")
        fim = False
        for rodada in range (1000):
            mesa = baralho.getPrimeiro().getValor()    
            for c in range (0,len(oscara)):                
                if oscara[c].getPrimeiro().getValor() == mesa:
                    oscara[c].removerInicio()
                else:
                    oscara[c].inserirFim(oscara[c].getPrimeiro().getValor())
                    oscara[c].removerInicio()
                if oscara[c].getPrimeiro() == None:
                    texto+=str(c+1)+"\n"
                    fim = True
            if fim==True:
                break
            baralho.removerInicio()
            baralho.inserirFim(mesa)
        else:
            texto+="0\n"

fecha.write(texto)
fecha.close()
