# -*- coding: cp1252 -*-
alunos = {}
print "# Cadastro de alunos - UFRPE #"
while True:    
    print "\nEscolha uma opção:"
    print "1-Cadastrar"
    print "2-Atualizar"
    print "3-Imprimir dados"
    print "4-Sair"
    opcao = input(": ")
    if opcao == 1:        
        nome = raw_input("\nNome: ")
        curso = raw_input("Curso: ")
        print "Endereço"
        rua = raw_input("Rua: ")
        numero = raw_input("Nº: ")
        bairro = raw_input("Bairro: ")
        alunos[nome] = {"curso":curso, "endereco":{"rua":rua, "numero":numero, "bairro":bairro}}
        print "Dados salvos"
    elif opcao == 2:
        while True:
            print "\nEscolha uma opção:"
            print "1-Atualizar Nome"
            print "2-Atualizar Curso"
            print "3-Atualizar Rua"
            print "4-Atualizar Número da casa"
            print "5-Atualizar Bairro"
            print "6-Voltar"
            opcao = input(": ")
            if opcao == 1:
                nome = raw_input("Digite o antigo nome do aluno: ")                
                if alunos.has_key(nome): #verificar se existe alguma chave dentro no dicionario com o input
                    novoNome = raw_input("Digite o novo nome do aluno: ")
                    alunos[novoNome] = alunos.pop(nome) #pop exclui o que tava salvo e "atualiza" o valor da chave.
                else:
                    print "Nome de aluno inválido"
            elif opcao == 2:
                nome = raw_input("Digite o nome do aluno: ")                
                if alunos.has_key(nome):
                    curso = raw_input("Digite o novo curso: ")
                    alunos[nome]['curso'] = curso
                else:
                    print "Nome de aluno inválido"
            elif opcao == 3:
                nome = raw_input("Digite o nome do aluno: ")                
                if alunos.has_key(nome):
                    rua = raw_input("Digite o novo nome da rua: ")
                    alunos[nome]['endereco']['rua'] = rua
                else:
                    print "Nome de aluno inválido"
            elif opcao == 4:
                nome = raw_input("Digite o nome do aluno: ")                
                if alunos.has_key(nome):
                    numero = raw_input("Digite o novo numero da casa: ")
                    alunos[nome]['endereco']['numero'] = numero
                else:
                    print "Nome de aluno inválido"
            elif opcao == 5:
                nome = raw_input("Digite o nome do aluno: ")                
                if alunos.has_key(nome):
                    bairro = raw_input("Digite o novo nome do bairro: ")
                    alunos[nome]['endereco']['bairro'] = bairro
                else:
                    print "Nome de aluno inválido"
            elif opcao == 6:
                break
    elif opcao == 3:
        for chave, valor in alunos.iteritems():
            print "\nNome:", chave
            print "Curso:", valor["curso"]
            print "Endereco:", valor["endereco"]["rua"]+","+ valor["endereco"]["numero"],"-", valor["endereco"]["bairro"]
    elif opcao == 4:
        print "Obrigado."
        break
    else:
        print "\nOpção inválida!\n"

