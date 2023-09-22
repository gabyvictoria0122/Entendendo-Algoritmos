lista_ordenada = list(range(101))
tentando = True
lista_advinhada = lista_ordenada.copy() #Não tinha usado o copy

while tentando:
    if len(lista_advinhada) == 1:
        chute = lista_advinhada[0]
    else:
        chute = lista_advinhada[len(lista_advinhada) // 2]

    dica = int(input(f"Eu chuto o número {chute}. Você está pensando em um número maior (1), menor(2) ou acertei(3)?"))

    if dica == 3:
        print("Viu como sou esperta! :) ")
        tentando = False
    elif dica == 2:
        lista_advinhada = lista_advinhada[:lista_advinhada.index(chute)]
    elif dica == 1:
        lista_advinhada = lista_advinhada[lista_advinhada.index(chute) + 1:]
    else:
        print("Entrada incorreta. Não quero mais jogar :(")

    if not lista_advinhada:
        print("Você deve ter feito algo errado. Vou sair agora.")
        tentando = False

# Desempenho -> log n -> log 101 -> aproximadamente 30