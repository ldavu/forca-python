gabarito = ['d','a','v','i']

gabarito_pessoa = ['-','-','-','-']

tentativas = 1
acertos = 0
completou = False

while tentativas != 10:
    
    letra_usuario = input("\nQual palavra? ")
    
    if (letra_usuario in gabarito):
        achar_indice = gabarito.index(letra_usuario)
        gabarito_pessoa[achar_indice] = letra_usuario
    else:
        print("Letra errada!")

    for x in gabarito_pessoa:
        print(x,end=', ')
    
    if (gabarito_pessoa == gabarito) and (tentativas == len(gabarito)):
        print(f"\nparabens acabou em {tentativas} tentativas, liga mestre!")
    elif(gabarito_pessoa == gabarito):
        print(f"Parabéns você acabou em {tentativas} tentativas!")
    else:
        print("")
    
    
    tentativas += 1
