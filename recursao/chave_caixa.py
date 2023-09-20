# loop while

def procure_pela_chave(main_box):
    pilha = main_box.crie_uma_pilha_para_buscar()
    while pilha is not vazia:
        caixa = pilha.pague_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print "achei a chave!"

# recursão

def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item) #recursão
        elif item.e_uma_chave():
            print "achei a chave!"