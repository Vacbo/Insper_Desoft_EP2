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
