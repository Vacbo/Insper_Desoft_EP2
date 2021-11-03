#Funções

import random
def cria_pecas():
    pecas_domino=[]
    i1=0
    i2=0
    while len(pecas_domino)<28:
        pecas_domino.append([i1,i2])
        i2+=1
        if i2==6:
            pecas_domino.append([i1,i2])
            i1+=1
            i2=i1
    random.shuffle(pecas_domino)
    return pecas_domino

#print(cria_pecas())

def inicia_jogo(n_jogadores,pecas_a_distribuir):
    saida={}
    for x in range(0,n_jogadores):
        i=0
        while i<7:
            if 'jogadores' not in saida:
                saida['jogadores']={}
            if x not in saida['jogadores']:  
                saida['jogadores'][x]=[pecas_a_distribuir.pop(0)]
            else:
                saida['jogadores'][x].append(pecas_a_distribuir.pop(0))
            i+=1
    saida['monte']=pecas_a_distribuir
    saida['mesa']=[]
    return saida

#print(inicia_jogo(2,cria_pecas()))

def verifica_ganhador(pecas_de_cada_jogador):
    for k in pecas_de_cada_jogador:
        if pecas_de_cada_jogador[k]==[]:
            return k
    return -1

def soma_pecas(pecas_de_um_jogador):
    soma=0
    for pecas in pecas_de_um_jogador:
        for n in pecas:
            soma+=n
    return soma

def posicoes_possiveis(mesa, pecas_de_um_jogador):
    posicoes_possiveis=[]
    valores_pontas_mesa=[]
    if mesa==[]:
        for i in range(0,len(pecas_de_um_jogador)):
            posicoes_possiveis.append(i)
        return posicoes_possiveis
    else:
        valores_pontas_mesa.append(mesa[0][0])
        valores_pontas_mesa.append(mesa[len(mesa)-1][1])
        for val in valores_pontas_mesa:
            for pec in pecas_de_um_jogador:
                for v in pec:
                    if val==v:
                        posicoes_possiveis.append(pecas_de_um_jogador.index(pec))
        posicoes_possiveis=list(set(posicoes_possiveis))
        return posicoes_possiveis
    
#mesa=[[0,2],[2,1],[1,6],[6,5],[5,0]]
#pecas=[[1,3],[1,4],[4,6],[2,3],[2,4],[6,6],[2,6]]
#print(posicoes_possiveis(mesa, pecas))

def adiciona_na_mesa(peca_a_colocar,mesa):
    valores_pontas_mesa=[]
    if mesa==[]:
        mesa.append(peca_a_colocar)
    else:
        valores_pontas_mesa.append(mesa[0][0])
        valores_pontas_mesa.append(mesa[len(mesa)-1][1])
        if peca_a_colocar[1]==valores_pontas_mesa[0]:
            mesa.insert(0,peca_a_colocar)
        elif peca_a_colocar[0]==valores_pontas_mesa[0]:
            mesa.insert(0,peca_a_colocar[::-1])
        elif peca_a_colocar[0]==valores_pontas_mesa[1]:
            mesa.insert(len(mesa),peca_a_colocar)
        elif peca_a_colocar[1]==valores_pontas_mesa[1]:
            mesa.insert(len(mesa),peca_a_colocar[::-1])
    return mesa

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
        print('Jogador: Você com {} peça(s)\n{1}'.format(len(jogadores_mesa_monte['jogadores'][i])))
        pecas_possiveis = posicoes_possiveis(jogadores_mesa_monte['mesa'], jogadores_mesa_monte['jogadores'][i])
        escolha = int(input('Escolha uma peça:'))
        check = False
        while not check:
            if escolha in pecas_possiveis:
                print('Colocou: {}'.format())
                check = True
            else:
                print('Posição inválida!')
                escolha = int(input('Escolha uma peça {}:'.format(pecas_possiveis)))