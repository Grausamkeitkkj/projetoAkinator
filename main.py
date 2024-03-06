import random

class akinator:

    bandas_heavy_metal = {
            'Death Metal': ['Death', 'Cannibal Corpse', 'Morbid Angel', 'Obituary', 'Entombed'],
            'Thrash Metal': ['Megadeth', 'Testament','Sodom', 'Sepultura', 'Tungsteno', 'Exodus', 'Slayer'],
            'Black Metal': ['Lore Liedge', 'Horde', 'Burzum', 'Nachzehrer', 'Forgotten Woods', 'Mayhem', 'Emperor'],
            'Power Metal': ['Helloween', 'Blind Guardian', 'DragonForce', 'Sabaton', 'Stratovarius'],
            'Doom Metal': ['Black Sabbath', 'Candlemass', 'Electric Wizard', 'My Dying Bride', 'Paradise Lost'],
            'Progressive Metal': ['Dream Theater', 'Tool', 'Opeth', 'Between the Buried and Me', 'Symphony X'],
    }

    lista_perguntas_genericas = {
        1: 'A banda toca músicas com vocais guturais e riffs rápidos?',
        2: 'A banda tem letras que falam sobre morte, violência ou temas obscuros?',
        3: 'A banda utiliza blast beats ou outros ritmos complexos de bateria?',
        4: 'A banda tem guitarras com distorção pesada e solos rápidos?',
        5: 'A banda tem um tecladista ou outros instrumentos que não são típicos do heavy metal?',
        6: 'A banda é conhecida por suas performances energéticas ao vivo?',
        7: 'A banda foi formada nos anos 80 ou 90?',
        8: 'A banda é considerada um dos pioneiros do gênero heavy metal?',
        9: 'A banda influenciou muitas outras bandas de heavy metal?',
        10: 'A banda já ganhou algum prêmio importante da música?',
        11: 'A banda é considerada "clássica" no cenário do heavy metal?',
        12: 'A banda é conhecida por ter um mascote ou símbolo icônico?',
        13: 'A banda já fez turnês internacionais?',
        14: 'A banda tem um grande número de fãs seguidores?',
        15: 'Qual é o álbum mais famoso da banda?',
        16: 'Qual é a música mais conhecida da banda?'    
    }
    
    def jogo():
        genero_escolhido = random.choice(list(akinator.bandas_heavy_metal.keys()))
        banda_escolhida = random.choice(akinator.bandas_heavy_metal[genero_escolhido])