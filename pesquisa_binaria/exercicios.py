# lista_nomes = ["Adonis", "Alec", "Alexis", "Anson", "Baylor", "Byron", "Cairo", "Callen", "Cedric", "Conrad", "Dangelo", "Damon", "Duncan", "Eason", "Eden", "Erin", "Finley", "Haley", "Harmoni", "Harper", "Hazel", "Holden", "Huxley", "Iker", "Itzel", "Jadel", "Jagger", "Jamal", "Jazlyn", "Jericho", "Jewel", "Kalel", "Kamden", "Keenam", "Killiam", "Kylo", "Kolton", "Lamar", "Landen", "Leif", "Lennox", "Marquis", "Mavis", "Melvin", "Neil", "Nikolai", "Orion", "Quinton", "Reid", "Rohan", "Samson", "Solomon", "Sullivan", "Sutton", "Tanner", "Urijah", "Vance", "Wade", "Wilder", "Xander", "Ylki", "Zavier", "Zion"]

# def pesquisa_binaria_nomes () :


lista_num = list(range(100))

def pesquisa_binaria_nums(lista_num, x):
    alto = len(lista_num) - 1
    baixo = 0
    i = 0
    while baixo <= alto:
        meio = (alto + baixo) // 2
        chute = lista_num[meio]
        i += 1
        if x == chute:
            return meio, i

        if chute > x :
            alto = meio - 1
                
        else:
            baixo = meio + 1
        
    return None

print(pesquisa_binaria_nums(lista_num, 99))