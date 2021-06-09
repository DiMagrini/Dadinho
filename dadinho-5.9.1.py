import random

def jogadas_do_jogador():
    global pontos_do_jogador 
    rolls = input('quantas roladas você quer? \n')
    i = int(rolls)
    ie = 0
    roladas = []
    while ie < i:
        dice = random.randint(1, 6)
        roladas.append(dice)
        #print ('essa rolada deu ' + str(dice))
        ie += 1
    pontos_do_jogador = sum(roladas) - i*2 
    print('você fez ' + str(pontos_do_jogador) + ' pontos.')

def jogadas_do_jogador2():
    rolls = input('quantas o seu AMIGUINHO quer? \n')
    i = int(rolls)
    ie = 0
    roladas = []
    while ie < i:
        dice = random.randint(1, 6)
        roladas.append(dice)
        #print ('essa rolada deu ' + str(dice))
        ie += 1
    pontos_do_jogador2 = sum(roladas) - i*2 
    print('você fez ' + str(pontos_do_jogador2) + ' pontos.')

    if pontos_do_jogador2 > pontos_do_jogador:
        print ('seu amigo ganhou XD')
    else: print('vc ganhou ¬¬')

def jogadas_do_pc():
    print('minha vez!')
    rolls = random.randrange(10)
    i = (rolls)
    ie = 0
    roladas = []
    while ie < i:
        dice = random.randint(1, 6)
        roladas.append(dice)
        #print ('essa rolada deu ' + str(dice))
        ie += 1
    pontos_do_pc = sum(roladas) - i*2
    print('eu fiz ' + str(pontos_do_pc) + ' pontos.')
    
    if pontos_do_jogador < pontos_do_pc:
        print ('ganhei! :P')
    else: print ('você ganhou... X|')

def regras():
    resposta = input ('você sabe as regras? \n')
    if resposta in ['não', 'nao']:
        print ('É simples: você pode rolar quantos dados quiser. A soma dos resultados de cada dado, menos o dobro da quantidade de dados que você rolou é igual a quantos pontos você fez. Quem fizer mais pontos ganha.\n')
    else:
        print ('beleza!')

def preferencia_do_jogador ():
    preferencia = (input('Você quer jogar comigo? ^^ \n'))
    if preferencia in ['com vc', 'com voce', 'com você', 'contigo', 'sim' , 's', 'isso', 'vamo', 'vamos']:
        jogadas_do_jogador()
        jogadas_do_pc()
    else: 
        PvP = input('ta jogando com alguem? >:(\n')
        if PvP in ['sim', 'to', 'tô', 'estou', 's']:
            print('blz então')
            jogadas_do_jogador()
            jogadas_do_jogador2()
        else:
            print('Ok... :c')
            jogadas_do_jogador()

def play_again():
    resposta = input ('quer mais uma? ')
    if resposta in ['s', 'sim', 'quero', 'bora', 'vamo', 'vamos']:
        return True
    else:
        print('ok. Até mais!')
       

print ('Oi! meu nome é Dadinho ^^\nbora jogar!')
regras()
preferencia_do_jogador()


while play_again() == True:
    ask = input ('comigo? :3 \n')
    if ask in ['sim, com vc','sim', 'contigo','com você', 'isso', 's']:
        print(':D')
        jogadas_do_jogador()
        jogadas_do_pc()
    elif ask in ['sozinho', 'solo', 'só eu','so eu']:
        jogadas_do_jogador()
    else:
       ask2 = input ('com o \'seu amiguinho\'?\n')
       if ask2 in ['sim', 'isso', 's']:
        print('ta ¬¬')
        jogadas_do_jogador()
        jogadas_do_jogador2()
       else:
        jogadas_do_jogador()

            


