import matplotlib.pyplot as plt
import random
import seaborn as sns
import math

#0 is the dove strategy
#1 is the hawk strategy

#getting 1 food allows survival, getting 2 food allows replication
#p/q<1 food is p/q chance of surviving
#1+p/q>1 food is p/q chance of replicating

population=[0,1] #array of individuals, with either hawk or dove strategy, this is the initial population
F=50 #number of food sources, each with 2 food in
T=100 #run time (let's call it days)
t=0 #start time
G=2 #total prize
C=10 #cost

hawks=[population.count(1)]
doves=[population.count(0)]
time=[0]


while t<T:
  
    x=[] #array representing spots taken at a food source
    
    for i in range(F):
        x.append([])

    for i in range(len(population)): #an individual picks a food source to go to
        choice = random.randint(0,F-1)
        x[choice].append(population[i])
    
    for i in range(F):
        if len(x[i])==1: #if one individual is at a food source it replicates
            p=random.uniform(0,1)
            if G%1==1:
                for l in range(math.floor(G-1)):
                    population.append(x[i][0])
            elif G<1:
                if p>G:
                    population.remove(x[i][0])
            elif G>1:
                for l in range(math.floor(G-1)):
                    population.append(x[i][0])
                if G%1>p:
                    population.append(x[i][0])               
             
        if x[i].count(0)>1 and x[i].count(0)==len(x[i]): #if 2 or more doves meet they split the food equally
            for j in range(x[i].count(0)):   
                p=random.uniform(0,1)
                if G/x[i].count(0)<1:
                    if p>G/x[i].count(0):
                        population.remove(0)                
                elif (G/x[i].count(0))%1==0:
                    for l in range(math.floor((G/x[i].count(0)))-1):
                        population.append(0)
                else:
                    for l in range(math.floor((G/x[i].count(0)))-1):
                        population.append(0)
                    if ((G/x[i].count(0))-1)%1>p:
                        population.append(0)
                
        if x[i].count(1)==1 and len(x[i])>1: #if one hawk meets any number of doves, the hawk gets the food, the doves get no food.
            for j in range(x[i].count(1)):
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
            for j in range(x[i].count(0)):
                population.remove(0) 
 
        if x[i].count(1)>1: #if two or more hawks meet, doves get nothing and hawks split with a cost
            for j in range(x[i].count(1)):
                p=random.uniform(0,1)
                if (G/x[i].count(1))-C*(x[i].count(1)-1)<1:
                    if p>(G/x[i].count(1))-C*(x[i].count(1)-1):
                        population.remove(1)                        
                elif (G/x[i].count(1))-C*(x[i].count(1)-1)%1==0:
                    for l in range(math.floor((G/x[i].count(1))-C*(x[i].count(1)-1))-1):
                        population.append(1)
                else:
                    for l in range(math.floor(((G/x[i].count(1))-C*(x[i].count(1)-1))-1)):
                        population.append(1)
                    if p<(((G/x[i].count(1))-C*(x[i].count(1)-1))-1)%1:
                        population.append(1)
            for j in range(x[i].count(0)):
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













'''
while t<T:
    

    
    dovepayoff=0
    hawkpayoff=0
    
    x=[] #array representing spots taken at a food source

    for i in range(F):
        x.append([])

    for i in range(len(population)): #an individual picks a food source to go to
        choice = random.randint(0,F-1)
        x[choice].append(population[i])
        
    for i in range(F):
        dcount=x[i].count(0)
        hcount=x[i].count(1)
        
        if hcount>0:
            hawkpayoff=hawkpayoff+G-(hcount*(hcount - 1)*C)
        if dcount>0 and hcount==0:
            dovepayoff=dovepayoff+G           
            
        
    if dovepayoff>0:
        for i in range(dovepayoff):
            population.append(0)
    else:
        if -dovepayoff<population.count(0):     
            for i in range(-dovepayoff):
                population.remove(0)
        else:
            for i in range(population.count(0)):
                population.remove(0)
            
    if hawkpayoff>0:
        for i in range(hawkpayoff):
            population.append(1)
    else:
        if -hawkpayoff<population.count(1):     
            for i in range(-hawkpayoff):
                population.remove(1)
        else:
            for i in range(population.count(1)):
                population.remove(1)
         

    t=t+1

    hawks.append(population.count(1))
    doves.append(population.count(0))
    time.append(t)
'''