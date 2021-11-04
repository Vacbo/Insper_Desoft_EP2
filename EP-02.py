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

while jogador_com_zero_pecas == -1:
    for i in ordem:
        print('MESA:\n{}'.format(' '.join(str(v) for v in jogadores_mesa_monte['mesa'])))
        if i == 0:
            print('Jogador: Você com {} peça(s)'.format(len(jogadores_mesa_monte['jogadores'][i])))
            pecas_possiveis = posicoes_possiveis(jogadores_mesa_monte['mesa'], jogadores_mesa_monte['jogadores'][i])
            if pecas_possiveis == []:
                if jogadores_mesa_monte['monte'] == []:
                    print('Não tem peças possíveis. MONTE VAZIO - PULANDO A VEZ!')
                    break
                else:
                    print('Não tem peças possíveis. PEGANDO DO MONTE!')
                    press_enter = input('[pressione ENTER]')
                    jogadores_mesa_monte['jogadores'][i].append(jogadores_mesa_monte['monte'][0])
                    del jogadores_mesa_monte['monte'][0]
                    break
            print(' '.join(str(v) for v in jogadores_mesa_monte['jogadores'][i]))
            escolha = int(input('Escolha uma peça:'))
            check = False
            while not check:
                if escolha in pecas_possiveis:
                    adiciona_na_mesa(jogadores_mesa_monte['jogadores'][i][escolha], jogadores_mesa_monte['mesa'])
                    print('Colocou: {}'.format(jogadores_mesa_monte['jogadores'][i][escolha]))
                    del jogadores_mesa_monte['jogadores'][i][escolha]
                    check = True
                    jogador_com_zero_pecas = verifica_ganhador(jogadores_mesa_monte['jogadores'])
                else:
                    print('Posição inválida!')
                    escolha = int(input('Escolha uma peça {}:'.format(pecas_possiveis)))
        else:
            print('Jogador: {0} com {1} peça(s)'.format(i+1, len(jogadores_mesa_monte['jogadores'][i])))
            pecas_possiveis = posicoes_possiveis(jogadores_mesa_monte['mesa'], jogadores_mesa_monte['jogadores'][i])
            if pecas_possiveis == []:
                if jogadores_mesa_monte['monte'] == []:
                    print('Não tem peças possíveis. MONTE VAZIO - PULANDO A VEZ!')
                    break
                else:
                    print('Não tem peças possíveis. PEGANDO DO MONTE!')
                    jogadores_mesa_monte['jogadores'][i].append(jogadores_mesa_monte['monte'][0])
                    del jogadores_mesa_monte['monte'][0]
                    break
            escolha = random.choice(pecas_possiveis)
            adiciona_na_mesa(jogadores_mesa_monte['jogadores'][i][escolha], jogadores_mesa_monte['mesa'])
            print('Colocou: {}'.format(jogadores_mesa_monte['jogadores'][i][escolha]))
            del jogadores_mesa_monte['jogadores'][i][escolha]
            jogador_com_zero_pecas = verifica_ganhador(jogadores_mesa_monte['jogadores'])

#se monte estiver vazio e nenhum jogador puder colocar peças, encerrar
#bugfix: apertar enter em "escolha uma peça" dá erro