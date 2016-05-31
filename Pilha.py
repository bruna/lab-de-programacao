#Classe Pilha
# Esta classe usa o recurso de heranca (herda a classe Lista)
#Algoritmos e Estrutura de Dados
#Prof. Tiago A. E. Ferreira

from Lista import List

class Stack ( List ):
    """ Classe que define uma Pilha a partir de uma lista encadeada"""

    def push(self,data):
        "Insere um elemento na Pilha"
        self.insertAtBegin(data)


    def pop(self):
        "Remove o primeiro elemento da Pilha"
        return self.removeFromBegin()