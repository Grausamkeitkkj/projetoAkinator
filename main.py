import random

class akinator:

    bandas_deletadas = []

    bandas_heavy_metal = [
        "Metallica",
        "Iron Maiden",
        "Black Sabbath",
        "Judas Priest",
        "Megadeth",
        "Slayer",
        "Pantera",
        "Motorhead",
        "Death",
        "Cannibal Corpse"
    ]

    lista_perguntas_genericas = {
        1: 'A banda toca músicas com vocais guturais?',
        2: 'A banda tem letras que falam sobre morte, violência ou temas obscuros?',
        4: 'A banda tem guitarras com distorção pesada e solos rápidos?',
        7: 'A banda foi formada nos anos 80 ou 90?',
        8: 'A banda é considerada um dos pioneiros do gênero heavy metal?',
        10: 'A banda já ganhou algum prêmio importante da música?',
        11: 'A banda é considerada "clássica" no cenário do heavy metal?',
        12: 'A banda é conhecida por ter um mascote ou símbolo icônico?',
    }
    
    @staticmethod
    def jogo():
        banda_aleatoria = random.choice(akinator.bandas_heavy_metal)
        print("Banda escolhida aleatoriamente:", banda_aleatoria)
        
        while len(akinator.bandas_deletadas) < 9:
            pergunta_aleatoria = random.choice(list(akinator.lista_perguntas_genericas.values()))
            print(pergunta_aleatoria)
            
            resposta = input("(s/n): ")
            if pergunta_aleatoria == akinator.lista_perguntas_genericas[1] and resposta.lower() == "s":
                banda = ['Metallica', 'Iron Maiden', 'Black Sabbath', 'Judas Priest', 'Megadeth', 'Slayer', 'Pantera', 'Motorhead']
            else:
                banda = ['Death', 'Cannibal Corpse']
            for banda_nome in banda:
                akinator.bandas_heavy_metal.remove(banda_nome)
            
            print("Bandas deletadas:", akinator.bandas_deletadas)
            print("Bandas restantes:", akinator.bandas_heavy_metal)

# Testando o jogo
akinator.jogo()
