import numpy as np
import matplotlib.pyplot
import matplotlib
from scipy.integrate import odeint
from sympy import symbols, solve

G=1
C=0

ydom = np.linspace(0,1,21);
zdom = np.linspace(0,1,21);

[Y,Z] = np.meshgrid(ydom,zdom); # generate mesh of domain

for i in range(len(Y)):
    for j in range(len(Y[i])):
        if Y[i][j]+Z[i][j]>1:
            Y[i][j]=0
            Z[i][j]=0
        

U = (4*C*Y)-(4*C*Y*Y)-(8*C*Y*Z)+((G*Y*Z)/5)+(4*C*Y*Y*Z)-((1/13)*G*Y*Y*Y*Y*Z)+(4*C*Y*Z*Z)+((1/5)*G*Y*Z*Z)-((4/11)*G*Y*Y*Y*Z*Z)+((1/5)*G*Y*Z*Z*Z)-((2/3)*G*Y*Y*Z*Z*Z)-((13/35)*G*Y*Z*Z*Z*Z); # dy/dt
V = (4*C*Z)-((G*Z)/5)-(4*C*Y*Z)+((1/13)*G*Y*Y*Y*Y*Z)-(8*C*Z*Z)+(4*C*Y*Z*Z)+((4/11)*G*Y*Y*Y*Z*Z)+(4*C*Z*Z*Z)+((2/3)*G*Y*Y*Z*Z*Z)+((4/7)*G*Y*Z*Z*Z*Z)+((G*Z*Z*Z*Z*Z)/5); # dz/dt

'''
x = symbols('x', real=True, nonnegative=True)
expr = ((G/C)/5)*(x**5) - ((G/C)/5)*x + x*((x-1)**2)*(5-1)
solution=solve(expr)
for i in range(len(solution)):
    if solution[i]>0 and solution[i]<1:
        s=solution[i]
    if len(solution)==2:
        s=0
'''

def ODE(state,t):
  # unpack the state vector
  y = state[0]
  z = state[1]

  # compute state derivatives
  yd = (4*C*y)-(4*C*y*y)-(8*C*y*z)+((G*y*z)/5)+(4*C*y*y*z)-((1/13)*G*y*y*y*y*z)+(4*C*y*z*z)+((1/5)*G*y*z*z)-((4/11)*G*y*y*y*z*z)+((1/5)*G*y*z*z*z)-((2/3)*G*y*y*z*z*z)-((13/35)*G*y*z*z*z*z)
  zd = (4*C*z)-((G*z)/5)-(4*C*y*z)+((1/13)*G*y*y*y*y*z)-(8*C*z*z)+(4*C*y*z*z)+((4/11)*G*y*y*y*z*z)+(4*C*z*z*z)+((2/3)*G*y*y*z*z*z)+((4/7)*G*y*z*z*z*z)+((G*z*z*z*z*z)/5)

  # return the state derivatives
  return [yd, zd]

state0 = [0.001, 0.001]
t = np.linspace(0, 60, 6000)
state = odeint(ODE, state0, t)
matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')

state0 = [0.001, 0.999]
t = np.linspace(0, 60, 6000)
state = odeint(ODE, state0, t)
matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')

state0 = [0.005, 0.994]
t = np.linspace(0, 60, 6000)
state = odeint(ODE, state0, t)
matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')

state0 = [0.030, 0.969]
t = np.linspace(0, 60, 6000)
state = odeint(ODE, state0, t)
matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')

state0 = [0.001, 0.999]
t = np.linspace(0, 60, 6000)
state = odeint(ODE, state0, t)
matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')

state0 = [0, 0.999]
t = np.linspace(0, 60, 6000)
state = odeint(ODE, state0, t)
matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')




matplotlib.pyplot.quiver(Y,Z,U,V,scale=2, pivot='mid', alpha=0.5)
matplotlib.pyplot.ylabel("z")
matplotlib.pyplot.xlabel("y")
matplotlib.pyplot.scatter(0,1,s=7,c='r')
matplotlib.pyplot.plot([0,1],[0,0],c='r')

matplotlib.pyplot.rcParams['pdf.fonttype'] = 42
matplotlib.pyplot.savefig('PhasePortraitN5G1C0.pdf',bbox_inches='tight',transparent = True)

matplotlib.pyplot.show()



