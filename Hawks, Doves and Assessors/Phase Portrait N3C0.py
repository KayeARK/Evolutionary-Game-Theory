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
        

U = (2*C*Y)-(2*C*Y*Y)-(4*C*Y*Z)+((G*Y*Z)/3)+(2*C*Y*Y*Z)-((1/7)*G*Y*Y*Z)+(2*C*Y*Z*Z)-((1/15)*G*Y*Z*Z); # dy/dt
V = (2*C*Z)-((G*Z)/3)-(2*C*Y*Z)+((1/7)*G*Y*Y*Z)-(4*C*Z*Z)+(2*C*Y*Z*Z)+((2/5)*G*Y*Z*Z)+(2*C*Z*Z*Z)+((G*Z*Z*Z)/3); # dz/dt

x = symbols('x', real=True, nonnegative=True)
expr = (2*C*x)-((G*x)/3)-(4*C*x*x)+(2*C*x*x*x)+((G*x*x*x)/3)
solution=solve(expr)
for i in range(len(solution)):
    if solution[i]>0 and solution[i]<1:
        s=solution[i]
    if len(solution)==2:
        s=0

def ODE(state,t):
  # unpack the state vector
  y = state[0]
  z = state[1]

  # compute state derivatives
  yd = (2*C*y)-(2*C*y*y)-(4*C*y*z)+((G*y*z)/3)+(2*C*y*y*z)-((1/7)*G*y*y*z)+(2*C*y*z*z)-((1/15)*G*y*z*z)
  zd = (2*C*z)-((G*z)/3)-(2*C*y*z)+((1/7)*G*y*y*z)-(4*C*z*z)+(2*C*y*z*z)+((2/5)*G*y*z*z)+(2*C*z*z*z)+((G*z*z*z)/3)

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
matplotlib.pyplot.savefig('PhasePortraitN3G1C0.pdf',bbox_inches='tight',transparent = True)

matplotlib.pyplot.show()

