max_tentativas = 6
tentativas = 0
oculta = "teste"
digitadas = ""
acertou_tudo = False

while (tentativas < max_tentativas) and not acertou_tudo:
    letra = raw_input("Digite uma letra: ")
    digitadas = digitadas + letra
    if letra in oculta: #acertou a letra digitada
        print "A palavra é: ",
        qtdeTracos = 0
        for i in oculta: #passando pela palavra para exibir as letras que já acertou
            if i in digitadas:
                print i,
            else:
                print "_",
                qtdeTracos += 1
        print "" #enter
        if qtdeTracos == 0: #ja acertou a palavra inteira
            print "Parabéns! Você acertou tudo!"
            acertou_tudo = True        
    else:
        tentativas += 1
        print "-> Você errou pela %d vez!"%tentativas

if acertou_tudo == False:
    print "Você perdeu. Tente novamente."

        
        
