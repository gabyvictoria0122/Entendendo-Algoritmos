def par_impar(n):
    n -= 1
    if n < 0:
        return
    else:
        if n % 2== 0:
            print("Par: ", n)
        else:
            print("Impar: ", n)
    par_impar(n)

par_impar(5)