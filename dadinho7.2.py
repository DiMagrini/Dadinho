import random
#funções
class Jogador:
    def __init__(self, mencao, win, jogada):
        self.mencao = mencao
        self.win = win
        self.jogada = jogada

    def rolagem(self, n_dados):
        soma = []
        for cnt in range(n_dados):
            dado = random.randint(1, 6)
            #print(dado) #para conferencia de dados
            soma.append(dado)
        if n_dados > 20:
            return sum(soma) - n_dados*3
        else: return sum(soma) - n_dados*2

player1 = Jogador('Você fez ', 'Você ganhou :|\n', 'quantos dados você quer rolar? \n')
player2 = Jogador('Seu amigo fez ', 'Seu amigo ganhou kk\n', 'quantos dados seu amigo quer rolar? \n')
pc = Jogador('eu fiz ', 'Eu ganhei :P\n', random.randrange(15))

class jogo:
    def __init__(self, jogador, mencao1, mencao2, win1, win2):
        self.jogador = jogador
        self.mencao1 = mencao1
        self.mencao2 = mencao2
        self.win1 = win1
        self.win2 = win2

    def partida(self, pts_1, pts_2):
        print('\n' + self.mencao1 + str(pts_1) + ' pontos.\nE ' + self.mencao2.lower() + str(pts_2) + '.\n')
        if pts_1 > pts_2:
            print(self.win1)
        elif pts_1 == pts_2:
            print('oxi empatou kkkk')
        else: print(self.win2)

PvE = jogo(player1, player1.mencao, pc.mencao, player1.win, pc.win)
PvP = jogo(player2, player1.mencao, player2.mencao, player1.win, player2.win)

#algoritimo da "pseudo IA" do dadinho
print ('\nOi! meu nome é Dadinho ^^\nBora jogar!')

if input('você sabe as regras? \n') in ['não', 'nao', 'n', 'nao faço ideia']:
    print ('É simples: você pode rolar quantos dados quiser. A soma dos resultados de cada dado, menos o dobro da quantidade de dados que você rolou é igual a quantos pontos você fez. Quem fizer mais pontos ganha.\nVocê pode jogar sozinho, com um amigo ou do melhor jeito: comigo! *-*\n')
else:
    print ('\nBlz!')

preferencia = 'ta pronto?\n'
preferencia2 = '\nquer jogar comigo? ^^\n'
preferencia3 = 'Ah... vai jogar com um amigo?\n'.lower()
feliz = 'eba!'

while input(preferencia) in ['quero', 'sim' , 's', 'isso', 'vamo', 'vamos', 'mais uma', 'to']:
    if input(preferencia2) in ['quero', 'sim' , 's', 'isso', 'vamo', 'vamos', 'mais uma']:
        print(feliz)
        PvE.partida(player1.rolagem(int(input(player1.jogada))), pc.rolagem(pc.jogada))
        feliz = 'Desce pro play, Neymar'
    else:
        if input(preferencia3) in ['sim' , 's', 'isso', 'com um amigo', 'com meu amigo', 'com um amg', 'com amigo', 'com amg']:
            print('ta ¬¬')
            PvP.partida(player1.rolagem(int(input(player1.jogada))), player2.rolagem(int(input(player2.jogada))))
            preferencia3 = 'Com o seu amigo de novo?\n'
        else: 
            print('ok')
            print('Deu ' + str(player1.rolagem(int(input(player1.jogada)))) + ' pontos.')
    
    preferencia = 'mais uma?\n'
    preferencia2 = 'comigo?\n'

print('então até mais! \o\n')