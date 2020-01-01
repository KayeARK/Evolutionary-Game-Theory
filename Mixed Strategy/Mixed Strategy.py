import matplotlib.pyplot as plt
import random

#0 is the dove strategy
#1 is the hawk strategy

#getting 1 food allows survival, getting 2 food allows replication
#p/q<1 food is p/q chance of surviving
#1+p/q>1 food is p/q chance of replicating

population=[0.5] #array of individuals, with either hawk or dove strategy, this is the initial population
populationcount=[]

       

N=1000 #number of food sources, each with 2 food in
T=50000 #run time (let's call it days)
t=0 #start time
mutationrate=0.05
mutationshift=0.001


time=[0]

while t<T:    
 
    xpopulation=[] #array representing spots taken at a food source
    xplay=[] #array of the strategy each individual actually uses

    for i in range(N):
        xpopulation.append([])
        xplay.append([])

    for i in range(len(population)): #an individual picks a food source to go to
        choice = random.randint(0,N-1)
        xpopulation[choice].append(population[i])        
        p=random.uniform(0,1)
        if p<population[i]:
            xplay[choice].append(1)
        else:
            xplay[choice].append(0)          


    for i in range(N):
        if len(xplay[i])==1: #if one individual is at a food source it replicates
            p=random.uniform(0,1)
            if p<mutationrate:
                if xpopulation[i][0]-mutationshift<0: 
                    population.append(round(xpopulation[i][0]+mutationshift,10))
                elif xpopulation[i][0]+mutationshift>1:
                    population.append(round(xpopulation[i][0]-mutationshift,10))
                else:
                    population.append(round(xpopulation[i][0]+random.choice((-1, 1))*mutationshift,10))
            else:
                population.append(xpopulation[i][0])
            
        if xplay[i].count(0)>2 and xplay[i].count(0)==len(xplay[i]): #if 3 or more doves meet they split the food equally
            for j in range(len(xplay[i])):
                p=random.uniform(0,1)
                if p>2/xplay[i].count(0):
                    population.remove(xpopulation[i][j])
                
        if xplay[i].count(1)>1: #if more than one hawk meets the hawks get no food food, the doves split half a food evenly
            for j in range(len(xplay[i])):
                if xplay[i][j]==1:
                    population.remove(xpopulation[i][j])
            for j in range(len(xplay[i])):   
                p=random.uniform(0,1)
                if xplay[i].count(0)>0 and p>1/(2*xplay[i].count(0)) and xplay[i][j]==0:
                    population.remove(xpopulation[i][j])
               
        if xplay[i].count(1)==1 and len(xplay[i])>1: #if one hawk meets many doves the hawk gets 3/2 food and doves split the rest evenly
            for j in range(len(xplay[i])):   
                p=random.uniform(0,1)
                if xplay[i].count(0)>0 and p>1/(2*xplay[i].count(0)) and xplay[i][j]==0:
                    population.remove(xpopulation[i][j])
                p=random.uniform(0,1)
                for j in range(len(xplay[i])):
                    if p>1/2 and xplay[i][j]==1:
                        p=random.uniform(0,1)
                        if p<mutationrate:
                            if xpopulation[i][0]-mutationshift<0: 
                                population.append(round(xpopulation[i][j]+mutationshift,10))
                            elif xpopulation[i][0]+mutationshift>1:
                                population.append(round(xpopulation[i][j]-mutationshift,10))
                            else:
                                population.append(round(xpopulation[i][j]+random.choice((-1, 1))*mutationshift,10))
                        else:
                            population.append(xpopulation[i][j])
            
    t = t + 1
    populationcount.append(population)

plt.hist(population)
plt.xlabel("Strategy, p")
plt.ylabel("Number of Individuals")
#plt.rcParams['pdf.fonttype'] = 42
#plt.savefig('MultiplayerHawksandDovesMixedStrategy.pdf',bbox_inches='tight',transparent = True)
plt.show()