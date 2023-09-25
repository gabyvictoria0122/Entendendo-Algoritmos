def contagem_regressiva(n):
    print(n)
    if n > 0:
        contagem_regressiva(n-1)
    else:
        return

contagem_regressiva(3)