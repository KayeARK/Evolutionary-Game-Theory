import math
import random
from random import randint
import matplotlib.pyplot as plt

#0 is dove strategy
#1 is hawk strategy
#2 is assessors strategy
iteration=[]
assessors=[]
doves=[]
hawks=[]

for l in range(100):    
    iteration.append(l)
    print(l)
    population=[]
    N=5
    G=randint(1,5)
    C=randint(1,10)
    Time=10
    #population_size=10000
    population=([0]*10)+([1]*10)+([2]*10)

    population_size=len(population)

    #for i in range(population_size):
        #population.append(randint(0,1))

    timearray=[]
    hawkpopulation=[]
    dovepopulation=[]
    assessorpopulation=[]

    for k in range(Time):
        population_size=len(population)
        HPayoff=0
        DPayoff=0
        APayoff=0
        for i in range(math.ceil(population_size/N)):
            game=[]
            for j in range(N):
                game.append(population[randint(0,population_size-1)])
            
            if game.count(0)>0 and game.count(1)>0 and game.count(2)>0:
                HPayoff=HPayoff+game.count(1)*((G/(game.count(1)+game.count(2)))-(game.count(1)+game.count(2)-1)*C)
                APayoff=APayoff+game.count(2)*(G/(game.count(1)+game.count(2)))
                
            if game.count(0)>0 and game.count(1)>0 and game.count(2)==0:
                HPayoff=HPayoff+game.count(1)*((G/game.count(1))-(game.count(1)-1)*C)
                
            if game.count(0)>0 and game.count(1)==0 and game.count(2)>0:
                DPayoff=DPayoff+game.count(0)*(G/(N+2*game.count(2)))
                APayoff=APayoff+game.count(2)*(3*G/(N+2*game.count(2)))
                
            if game.count(0)==0 and game.count(1)>0 and game.count(2)>0:
                HPayoff=HPayoff+game.count(1)*((G/N)-(N-1)*C)
                APayoff=APayoff+game.count(2)*(G/N)
                
            if game.count(0)>0 and game.count(1)==0 and game.count(2)==0:
                DPayoff=DPayoff+game.count(0)*(G/N)
                
            if game.count(0)==0 and game.count(1)>0 and game.count(2)==0:
                HPayoff=HPayoff+game.count(1)*(G/N-(N-1)*C)
                
            if game.count(0)==0 and game.count(1)==0 and game.count(2)>0:
                APayoff=APayoff+game.count(2)*(G/N)     
        
        timearray.append(k)
        hawkpopulation.append(population.count(1))
        dovepopulation.append(population.count(0))
        assessorpopulation.append(population.count(2))
       
        if DPayoff>0:
            for i in range(int(DPayoff)):
                population.append(0)
        else:
            if -DPayoff<population.count(0):     
                for i in range(-int(DPayoff)):
                    population.remove(0)
            else:
                for i in range(population.count(0)):
                    population.remove(0)
                
        if HPayoff>0:
            for i in range(int(HPayoff)):
                population.append(1)
        else:
            if -HPayoff<population.count(1):     
                for i in range(-int(HPayoff)):
                    population.remove(1)
            else:
                for i in range(population.count(1)):
                    population.remove(1)
                    
        if APayoff>0:
            for i in range(int(APayoff)):
                population.append(2)
        else:
            if -APayoff<population.count(2):     
                for i in range(-int(APayoff)):
                    population.remove(2)
            else:
                for i in range(population.count(2)):
                    population.remove(2)

    timearray.append(Time+1)
    hawkpopulation.append(population.count(1))
    dovepopulation.append(population.count(0))
    assessorpopulation.append(population.count(2))
    assessors.append(assessorpopulation[-1]/(assessorpopulation[-1]+hawkpopulation[-1]+dovepopulation[-1]))
    doves.append(dovepopulation[-1]/(assessorpopulation[-1]+hawkpopulation[-1]+dovepopulation[-1]))
    hawks.append(hawkpopulation[-1]/(assessorpopulation[-1]+hawkpopulation[-1]+dovepopulation[-1]))

#plt.plot(iteration, assessors, label="Assessors")
#plt.plot(iteration, hawks, label="Hawks")
#plt.plot(iteration, doves, label="Doves")
plt.xlabel("Proportion of Population")
plt.ylabel("Number of Occurrences")
plt.hist(assessors, label="Assessors")
#plt.hist(hawks, label="Hawks")
plt.hist(doves, label="Doves")
plt.legend(loc='upper center')

plt.rcParams['pdf.fonttype'] = 42
plt.savefig('LouiseMultiplayerHawksDovesAssessorsPureStrategyyGraphN5.pdf',bbox_inches='tight',transparent = True)

plt.show()