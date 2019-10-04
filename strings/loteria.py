import random

m = ['El gallo', 'El diablito', 'La dama', 'El catrín', 'El paraguas', 'La sirena', 'La escalera', 'La botella', 'El barril','El árbol','El melón','El valiente','El gorrito','La muerte','La pera','La bandera','El bandolón','El violoncello','La garza','El pájaro','La mano','La bota','La luna','El cotorro','El borracho','El negrito','El corazón','La sandía','El tambor','El camarón','Las jaras','El músico','La araña','El soldado','La estrella','El cazo','El mundo','El apache','El nopal','El alacrán','La rosa','La calavera','La campana','El cantarito','El venado','El sol','La corona','La chalupa','El pino','El pescado','La palma','La maceta','El arpa','La rana']
n = []

def loteria():

    for x in range(len(m)):
        if len(m) == 1:
            n.append(m[0])
            m.pop()
        else:
            temp = random.randrange(0, len(m)-1)
            '''print(len(m))
            print(temp)'''
            n.append(m[temp])
            m.pop(temp)

    for f in range(len(n)):
        input()
        print(n[f])

loteria()