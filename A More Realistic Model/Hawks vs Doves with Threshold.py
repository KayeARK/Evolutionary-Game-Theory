import math
import random
from random import randint
import matplotlib.pyplot as plt

#0 is dove strategy
#1 is hawk strategy

population=[]
N=3
G=4
C=1
F=100
Time=100
#population_size=10000
population=([0]*500)+([1]*500)

population_size=len(population)

#for i in range(population_size):
    #population.append(randint(0,1))





timearray=[]
hawkpopulation=[]
dovepopulation=[]


for k in range(Time):
    population_size=len(population)
    HPayoff=0
    DPayoff=0
    
    if population_size/N < F:
        games=math.ceil(population_size/N)
    
    else:
        games=F
   
    for i in range(F):#range(games): #range(math.ceil(population_size/N)):
        game=[]
        for j in range(N):
            game.append(population[randint(0,population_size-1)])
        if game.count(1)==1:
            HPayoff=HPayoff + G
        if game.count(1)==0:
            DPayoff=DPayoff + G
        if game.count(1)>1:
            HPayoff=HPayoff + G-((game.count(1)-1)*game.count(1)*C)   
    
    timearray.append(k)
    hawkpopulation.append(population.count(1))
    dovepopulation.append(population.count(0))    
   
    if DPayoff>0:
        for i in range(DPayoff):
            population.append(0)
    else:
        if -DPayoff<population.count(0):     
            for i in range(-DPayoff):
                population.remove(0)
        else:
            for i in range(population.count(0)):
                population.remove(0)
            
    if HPayoff>0:
        for i in range(HPayoff):
            population.append(1)
    else:
        if -HPayoff<population.count(1):     
            for i in range(-HPayoff):
                population.remove(1)
        else:
            for i in range(population.count(1)):
                population.remove(1)
                
timearray.append(Time+1)
hawkpopulation.append(population.count(1))
dovepopulation.append(population.count(0))
    
plt.plot(timearray,hawkpopulation, label="Hawks")
plt.plot(timearray,dovepopulation, label="Doves")
plt.xlabel("Generation Number")
plt.ylabel("Number of Individuals")
plt.legend()


plt.rcParams['pdf.fonttype'] = 42
plt.savefig('ThresholdF100N3G4C1LouiseMultiplayerHawksandDovesPureStrategy.pdf',bbox_inches='tight',transparent = True)


plt.show()