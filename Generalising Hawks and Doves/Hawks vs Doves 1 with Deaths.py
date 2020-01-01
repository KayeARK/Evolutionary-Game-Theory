import matplotlib.pyplot as plt
import seaborn as sns
import math
import random
from random import randint


#0 is the dove strategy
#1 is the hawk strategy

#getting 1 food allows survival, getting 2 food allows replication
#p/q<1 food is p/q chance of surviving
#1+p/q>1 food is p/q chance of replicating

population=([0]*100)+([1]*100) #array of individuals, with either hawk or dove strategy, this is the initial population
T=10000 #run time (let's call it days)
t=0 #start time
G=30 #total prize
C=100 #cost
N=2

hawks=[population.count(1)]
doves=[population.count(0)]
time=[0]

while t<T:
    
    n=5 #math.ceil(len(population)/N)    
    
    for i in range(n):        
        
        game=[]
        
        for j in range(N):
            if len(population)>N-1:
                game.append(random.choice(population))
        
        if game.count(1)==1: #one hawk
            for j in range(game.count(1)):
                p=random.uniform(0,1)
                if G<1:
                    if p>G:
                        population.remove(1)                        
                elif G%1==0:
                    for l in range(math.floor(G-1)):
                        population.append(1)
                else:
                    for l in range(math.floor(G-1)):
                        population.append(1)
                    if p<(G-1)%1:
                        population.append(1)
            for j in range(game.count(0)):
                population.remove(0)
                
        elif game.count(1)==0: #no hawks
            for j in range(game.count(0)):   
                p=random.uniform(0,1)
                if G/game.count(0)<1:
                    if p>G/game.count(0):
                        population.remove(0)                
                elif (G/game.count(0))%1==0:
                    for l in range(math.floor((G/game.count(0)))-1):
                        population.append(0)
                else:
                    for l in range(math.floor((G/game.count(0)))-1):
                        population.append(0)
                    if ((G/game.count(0))-1)%1>p:
                        population.append(0)            
            
        else: #two or more hawks
            for j in range(game.count(1)):
                p=random.uniform(0,1)
                if (G/game.count(1))-C*(game.count(1)-1)<1:
                    if p>(G/game.count(1))-C*(game.count(1)-1):
                        population.remove(1)                        
                elif (G/game.count(1))-C*(game.count(1)-1)%1==0:
                    for l in range(math.floor((G/game.count(1))-C*(game.count(1)-1))-1):
                        population.append(1)
                else:
                    for l in range(math.floor(((G/game.count(1))-C*(game.count(1)-1))-1)):
                        population.append(1)
                    if p<(((G/game.count(1))-C*(game.count(1)-1))-1)%1:
                        population.append(1)
            for j in range(game.count(0)):
                population.remove(0)     
        
    t = t + 1
    
    hawks.append(population.count(1))
    doves.append(population.count(0))
    time.append(t)
   
plt.plot(time,hawks, label="Hawks")
plt.plot(time,doves, label="Doves")
plt.xlabel("Generation Number")
plt.ylabel("Number of Individuals")
plt.legend()

#plt.rcParams['pdf.fonttype'] = 42
#plt.savefig('MultiplayerHawksandDovesPureStrategy.pdf',bbox_inches='tight',transparent = True)

plt.show()
