# -------------------------------------------------------------------------------------------------
# 1. Crie um método (preenche_vetor) que receba um vetor e preencha o vetor com números aleatórios.
# -------------------------------------------------------------------------------------------------
import random 

def preenche_vetor(vetor): 
    for x in range(len(vetor)): 
        vetor[x] = random.randint(1, 100)

vetor = [0] * 10

preenche_vetor(vetor)
print("Vetor preenchido:", vetor)
