import math
import random
from random import randint
import matplotlib.pyplot as plt

#0 is dove strategy
#1 is hawk strategy

population=[]
N=2
G=2
C=3
F=1
Time=100
#population_size=10000
population=([0]*100)+([1]*100)

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
    for i in range(F):        #range(math.ceil(population_size/N)):
        N=randint(1,math.ceil((1/F)*len(population)))
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
            
 
''' 
    if HPayoff==0 and DPayoff==0:
        population=population
    else:
        population=[]
        for i in range(population_size):
            p=random.uniform(0,1)
            if HPayoff<0:
                HPayoff=0
            if p<(DPayoff)/(HPayoff+DPayoff):
                population.append(0)
            else:
                population.append(1)
'''

timearray.append(Time+1)
hawkpopulation.append(population.count(1))
dovepopulation.append(population.count(0))
    
plt.plot(timearray,hawkpopulation, label="Hawks")
plt.plot(timearray,dovepopulation, label="Doves")
plt.xlabel("Generation Number")
plt.ylabel("Number of Individuals")
plt.legend()


#plt.rcParams['pdf.fonttype'] = 42
#plt.savefig('LouiseMultiplayerHawksandDovesPureStrategy.pdf',bbox_inches='tight',transparent = True)


plt.show()