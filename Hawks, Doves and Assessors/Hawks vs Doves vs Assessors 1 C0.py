import math
import random
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#0 is dove strategy
#1 is hawk strategy
#2 is assessors strategy

population=[]
N=5
G=1
C=0
Time=12

fixedpoint_t_mat=[]
fixedpoint_s_mat=[]

for m in range(100):

    a_n=randint(0,100)
    h_n=randint(0,100)
    d_n=randint(0,100)

    population=([0]*d_n)+([1]*h_n)+([2]*a_n)

    population_size=len(population)

    #for i in range(population_size):
    #    population.append(randint(0,2))
        




    def ODE(state,t):
        # unpack the state vector
        y = state[0]
        z = state[1]

        # compute state derivatives
        if N==2:
            yd = (C*y)-(C*y*y)-(2*C*y*z)+((G/4)*y*z)+(C*y*y*z)+(C*y*z*z)
            zd = (C*z)-((G/2)*z)-(C*y*z)+((G/4)*y*z)-(2*C*z*z)+((G/2)*z*z)+(C*y*z*z)+(C*z*z*z)
        if N==3:
            yd = (2*C*y)-(2*C*y*y)-(4*C*y*z)+((G*y*z)/3)+(2*C*y*y*z)-((1/7)*G*y*y*z)+(2*C*y*z*z)-((1/15)*G*y*z*z)
            zd = (2*C*z)-((G*z)/3)-(2*C*y*z)+((1/7)*G*y*y*z)-(4*C*z*z)+(2*C*y*z*z)+((2/5)*G*y*z*z)+(2*C*z*z*z)+((G*z*z*z)/3)
        if N==4:
            yd = (3*C*y)-(3*C*y*y)-(6*C*y*z)+((G*y*z)/4)+(3*C*y*y*z)-((1/10)*G*y*y*y*z)+(3*C*y*z*z)+((1/4)*G*y*z*z)-((3/8)*G*y*y*z*z)-((1/4)*G*y*z*z*z)
            zd = (3*C*z)-((G*z)/4)-(3*C*y*z)+((1/10)*G*y*y*y*z)-(6*C*z*z)+(3*C*y*z*z)+((3/8)*G*y*y*z*z)+(3*C*z*z*z)+(1/2*G*y*z*z*z)+((G*z*z*z*z)/4)
        if N==5:
            yd = (4*C*y)-(4*C*y*y)-(8*C*y*z)+((G*y*z)/5)+(4*C*y*y*z)-((1/13)*G*y*y*y*y*z)+(4*C*y*z*z)+((1/5)*G*y*z*z)-((4/11)*G*y*y*y*z*z)+((1/5)*G*y*z*z*z)-((2/3)*G*y*y*z*z*z)-((13/35)*G*y*z*z*z*z)
            zd = (4*C*z)-((G*z)/5)-(4*C*y*z)+((1/13)*G*y*y*y*y*z)-(8*C*z*z)+(4*C*y*z*z)+((4/11)*G*y*y*y*z*z)+(4*C*z*z*z)+((2/3)*G*y*y*z*z*z)+((4/7)*G*y*z*z*z*z)+((G*z*z*z*z*z)/5)

        

        # return the state derivatives
        return [yd, zd]

    state0 = [population.count(2)/population_size, population.count(0)/population_size]
    t = np.linspace(0, 60, 6000)
    state = odeint(ODE, state0, t)

    fixedpoint_t=state[-1][0]
    fixedpoint_t_mat.append(fixedpoint_t)






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
        
    fixedpoint_s=assessorpopulation[-1]/(hawkpopulation[-1]+assessorpopulation[-1])
    fixedpoint_s_mat.append(fixedpoint_s)

plt.plot([0,1],[0,1], zorder=0)
plt.scatter(fixedpoint_t_mat,fixedpoint_s_mat, c='black', s=5, zorder=5)

plt.xlabel("Theoretical fixed point reached")
plt.ylabel("Simulated fixed point reached")

plt.rcParams['pdf.fonttype'] = 42
plt.savefig('HawksDovesAssessorsN5C0FixedPointPlotTandS.pdf',bbox_inches='tight',transparent = True)

plt.show()
