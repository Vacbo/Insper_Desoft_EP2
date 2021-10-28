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

print(cria_pecas())