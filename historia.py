import random
#Funçao que gera a introduçao da historia
def gerar_intoducao():
    introduções = ["A vida é cheia de momentos especiais que nos ensinam e fazem crescer"]
    return random.choice(introduções)

#Funçao que gera o desenvolvimento da historia
def gerar_desenvolvimento():
    desenvolvimentos =["As vezes","passamos por desafios que parecem impossiveis","mas com determinaçao","conseguimos supera-los"]
    return random.choice(desenvolvimentos)

#Funçao que gera o final da historia
def gerar_final():
    finais = ["A amizade e o amor são importantes para tornar a jornada mais leve. Cada dia é uma nova oportunidade para aprender e ser melhor. No final, são as memórias e as conexões que fazem tudo valer a pena."]
    return random.choice(finais)
    #Funçao principal que geara toda a historia
def gerar_historia():
        introdução = gerar_intoducao()
        desenvolvimento = gerar_desenvolvimento()
        final = gerar_final()

        historia =f"{introdução}{desenvolvimento}{final}"
        return historia
    
    #xibe a história gerada
if __name__=="_main_":
    print(gerar_historia())
     