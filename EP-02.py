from funcoes import *

#mesa=[[1,6],[6,6]]
#peca=[2,6]
#print(adiciona_na_mesa(peca,mesa))

#Começo do Jogo

#Distribuição de peças
pecas = cria_pecas()

#Texto Inicial
print('Bem-vindo(a) ao jogo de Dominó!\nO objetivo do jogo é ser o primeiro jogador a ficar sem nenhuma peça na mão.')
numero_de_jogadores = input('Digite o número de jogadores (2-4):')

#Check se o número de jogadores é válido
check = False
while not check:
    if numero_de_jogadores != '2' and numero_de_jogadores != '3' and numero_de_jogadores != '4':
        print('Número inválido!')
        numero_de_jogadores = input('Digite um número de jogadores válido (2-4):')
    else:
        check = True

#Função Inicia Jogo
jogadores_mesa_monte = inicia_jogo(int(numero_de_jogadores), pecas)

#Determina Ordem
ordem = []
for j in jogadores_mesa_monte['jogadores']:
    ordem.append(int(j))
random.shuffle(ordem)

print('MESA:\n{}'.format(' '.join(jogadores_mesa_monte['mesa'])))

for i in ordem:
    if i == 0:
        print('Jogador: Você com {} peça(s)'.format(len(jogadores_mesa_monte['jogadores'][i])))
        pecas_possiveis = posicoes_possiveis(jogadores_mesa_monte['mesa'], jogadores_mesa_monte['jogadores'][i])
        print('{}'.format(' '.join(jogadores_mesa_monte['jogadores'][i])))
        escolha = int(input('Escolha uma peça:'))
        check = False
        while not check:
            if escolha in pecas_possiveis:
                print('Colocou: {}'.format())
                check = True
            else:
                print('Posição inválida!')
                escolha = int(input('Escolha uma peça {}:'.format(pecas_possiveis)))