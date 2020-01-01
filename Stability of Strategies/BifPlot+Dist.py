from sympy import symbols, solve
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab
from matplotlib import cm#
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import seaborn
import math
import random
from random import randint


N=3

amat=[]
solutions=[]
arange=201
astep=0.05

   
    
a=-astep
 
    
for j in range(arange):
        
    a=a+astep
    amat.append(a)
        
    x = symbols('x', real=True, nonnegative=True)
    expr = (a/N)*(x**N) - (a/N)*x + x*((x-1)**2)*(N-1)
    
    solution=solve(expr)

    if len(solution)==3:
        solutions.append(solution[1])
            
    elif j==0:
        solutions.append(1)
            
    else:
        solutions.append(0)
 
            

a = list(range(0,arange))
a[:] = [x * astep for x in a]

    
X=a
Y = solutions

plt.plot(X, Y, color='g', label='Stable')


one=[]
for i in range(len(X)):
    one.append(1)
    
plt.plot(X, one, color='r')

    
plt.plot([0,min(N*(N-1),(arange-1)*astep)], [0,0], color='r', label='Unstable')
plt.xlabel('\u03BB')
plt.ylabel('z')
plt.legend()


zmat=[]
lmat=[]

for p in range(100):

    print(p)
    population=[]
    G=random.randint(1,10)
    C=random.randint(1,10)
    Time=10
    #population_size=10000
    population=([0]*50)+([1]*50)

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
        for i in range(math.ceil(population_size/N)):
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
                
    zmat.append(dovepopulation[-1]/(hawkpopulation[-1]+dovepopulation[-1]))
    lmat.append(G/C)
                
plt.scatter(lmat,zmat, color='black', s=10)
'''
plt.rcParams['pdf.fonttype'] = 42
plt.savefig('FivePlayerBifurcationDiagram.pdf',bbox_inches='tight',transparent = True)
'''
plt.show()

'''                
timearray.append(Time+1)
hawkpopulation.append(population.count(1))
dovepopulation.append(population.count(0))
    
plt.plot(timearray,hawkpopulation, label="Hawks")
plt.plot(timearray,dovepopulation, label="Doves")
plt.xlabel("Generation Number")
plt.ylabel("Number of Individuals")
plt.legend()


plt.rcParams['pdf.fonttype'] = 42
plt.savefig('LouiseMultiplayerHawksandDovesPureStrategy.pdf',bbox_inches='tight',transparent = True)


plt.show()
'''