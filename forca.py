gabarito = ['d','a','v','i']

gabarito_pessoa = ['-','-','-','-']

tentativas = 0
acertos = 0
completou = False

while tentativas != 10:
    
    letra_usuario = input("\nQual palavra? ")
    
    if (letra_usuario in gabarito):
        achar_indice = gabarito.index(letra_usuario)
        gabarito_pessoa[achar_indice] = letra_usuario
    else:
        print("Algo de errado")

    for x in gabarito_pessoa:
        print(x,end=',')
    
    if gabarito_pessoa == gabarito:
        print("\nparabens acabou!")
        break
    
    
    tentativas +=1
