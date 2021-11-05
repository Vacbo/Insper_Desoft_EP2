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

jogador_com_zero_pecas = -1
empatou_jogo = -1

while jogador_com_zero_pecas == -1 or empatou_jogo == -1:
    if not jogador_com_zero_pecas == -1 or not empatou_jogo == -1:
        break
    for i in ordem:
        print('MESA:\n{}'.format(' '.join(str(v) for v in jogadores_mesa_monte['mesa'])))
        if i == 0:
            print('Jogador: Você com {} peça(s)'.format(len(jogadores_mesa_monte['jogadores'][i])))
            pecas_possiveis = posicoes_possiveis(jogadores_mesa_monte['mesa'], jogadores_mesa_monte['jogadores'][i])
            if pecas_possiveis == []:
                if jogadores_mesa_monte['monte'] == []:
                    print('Não tem peças possíveis. MONTE VAZIO - PULANDO A VEZ!')
                    empatou_jogo = empate(jogadores_mesa_monte)
                    if not jogador_com_zero_pecas == -1 or not empatou_jogo == -1:
                        break
                    continue
                else:
                    print('Não tem peças possíveis. PEGANDO DO MONTE!')
                    press_enter = input('[pressione ENTER]')
                    jogadores_mesa_monte['jogadores'][i].append(jogadores_mesa_monte['monte'][0])
                    del jogadores_mesa_monte['monte'][0]
                    continue
            print(' '.join(str(v) for v in jogadores_mesa_monte['jogadores'][i]))
            escolha = input('Escolha uma peça:')
            check = False
            while not check:
                if escolha.isdigit() and int(escolha) in pecas_possiveis:
                    adiciona_na_mesa(jogadores_mesa_monte['jogadores'][i][int(escolha)], jogadores_mesa_monte['mesa'])
                    print('Colocou: {}'.format(jogadores_mesa_monte['jogadores'][i][int(escolha)]))
                    del jogadores_mesa_monte['jogadores'][i][int(escolha)]
                    check = True
                    jogador_com_zero_pecas = verifica_ganhador(jogadores_mesa_monte['jogadores'])
                    empatou_jogo = empate(jogadores_mesa_monte)
                    if not jogador_com_zero_pecas == -1 or not empatou_jogo == -1:
                        break
                else:
                    print('Posição inválida!')
                    escolha = input('Escolha uma peça {}:'.format(pecas_possiveis))
        else:
            print('Jogador {0} com {1} peça(s)'.format(i+1, len(jogadores_mesa_monte['jogadores'][i])))
            pecas_possiveis = posicoes_possiveis(jogadores_mesa_monte['mesa'], jogadores_mesa_monte['jogadores'][i])
            if pecas_possiveis == []:
                if jogadores_mesa_monte['monte'] == []:
                    print('Não tem peças possíveis. MONTE VAZIO - PULANDO A VEZ!')
                    empatou_jogo = empate(jogadores_mesa_monte)
                    if not jogador_com_zero_pecas == -1 or not empatou_jogo == -1:
                        break
                    continue
                else:
                    print('Não tem peças possíveis. PEGANDO DO MONTE!')
                    jogadores_mesa_monte['jogadores'][i].append(jogadores_mesa_monte['monte'][0])
                    del jogadores_mesa_monte['monte'][0]
                    continue
            escolha = random.choice(pecas_possiveis)
            adiciona_na_mesa(jogadores_mesa_monte['jogadores'][i][escolha], jogadores_mesa_monte['mesa'])
            print('Colocou: {}'.format(jogadores_mesa_monte['jogadores'][i][escolha]))
            del jogadores_mesa_monte['jogadores'][i][escolha]
            jogador_com_zero_pecas = verifica_ganhador(jogadores_mesa_monte['jogadores'])
            empatou_jogo = empate(jogadores_mesa_monte)
            if not jogador_com_zero_pecas == -1 or not empatou_jogo == -1:
                break

#FAZER SCOREBOARD E DECORAR