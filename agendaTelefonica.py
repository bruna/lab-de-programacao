agenda = {}
while True:
    cpf = input("CPF: " )
    nome = raw_input("Nome: ")
    idade = input("Idade: ")
    telefone = input("Telefone: ")
    agenda[cpf] = (nome, idade, telefone)
    print "Dados salvos"
    fim = raw_input("\nContinuar digitando? s/n: ")
    if fim == 'n' : break

for chave, valor in agenda.iteritems():
    print chave, ":", valor[0],'-',valor[1],'-',valor[2] 

