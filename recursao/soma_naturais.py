def soma(n, somado):
    somado += n
    n -= 1
    if n < 0:
        return print(somado)
    else:
        soma(n, somado)


soma(7, 0)


# para calcular a soma de números naturais, é mais eficiente usar uma abordagem iterativa ou a fórmula matemática para a soma de uma progressão aritmética (Soma = n * (n + 1) / 2).