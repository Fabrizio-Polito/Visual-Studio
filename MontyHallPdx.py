import random


MIN=1
MAX=3
vittorie=0




for i in range(10000):

    porta=[1,1,1]
    porta_aperta=0
    scelta_finale=0

    premio= random.randint(0,2)
    porta[premio]=2

    scelta=random.randint(0,2) 

    while(porta_aperta==premio or porta_aperta==scelta):
        porta_aperta+=1

    while(scelta_finale==porta_aperta or scelta_finale==scelta):
        scelta_finale+=1
  
    if(scelta_finale==premio):
        vittorie+=1

print("\n\nhai vinto: ", vittorie)




