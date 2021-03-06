import numpy as np
import matplotlib.pyplot
import matplotlib
from scipy.integrate import odeint
from sympy import symbols, solve

G=13
C=1

ydom = np.linspace(0,1,21);
zdom = np.linspace(0,1,21);

[Y,Z] = np.meshgrid(ydom,zdom); # generate mesh of domain

for i in range(len(Y)):
    for j in range(len(Y[i])):
        if Y[i][j]+Z[i][j]>1:
            Y[i][j]=0
            Z[i][j]=0
        

U = (3*C*Y)-(3*C*Y*Y)-(6*C*Y*Z)+((G*Y*Z)/4)+(3*C*Y*Y*Z)-((1/10)*G*Y*Y*Y*Z)+(3*C*Y*Z*Z)+((1/4)*G*Y*Z*Z)-((3/8)*G*Y*Y*Z*Z)-((1/4)*G*Y*Z*Z*Z); # dy/dt
V = (3*C*Z)-((G*Z)/4)-(3*C*Y*Z)+((1/10)*G*Y*Y*Y*Z)-(6*C*Z*Z)+(3*C*Y*Z*Z)+((3/8)*G*Y*Y*Z*Z)+(3*C*Z*Z*Z)+(1/2*G*Y*Z*Z*Z)+((G*Z*Z*Z*Z)/4); # dz/dt

x = symbols('x', real=True, nonnegative=True)
expr = (3*C*x)-((G*x)/4)-(6*C*x*x)+(3*C*x*x*x)+((G*x*x*x*x)/4)
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
  yd = (3*C*y)-(3*C*y*y)-(6*C*y*z)+((G*y*z)/4)+(3*C*y*y*z)-((1/10)*G*y*y*y*z)+(3*C*y*z*z)+((1/4)*G*y*z*z)-((3/8)*G*y*y*z*z)-((1/4)*G*y*z*z*z)
  zd = (3*C*z)-((G*z)/4)-(3*C*y*z)+((1/10)*G*y*y*y*z)-(6*C*z*z)+(3*C*y*z*z)+((3/8)*G*y*y*z*z)+(3*C*z*z*z)+(1/2*G*y*z*z*z)+((G*z*z*z*z)/4)

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

if s>0:

    state0 = [0.001, s]
    t = np.linspace(0, 60, 6000)
    state = odeint(ODE, state0, t)
    matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')

    state0 = [0.001, s/2]
    t = np.linspace(0, 60, 6000)
    state = odeint(ODE, state0, t)
    matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')

    state0 = [0.001, (s+1)/2]
    t = np.linspace(0, 60, 6000)
    state = odeint(ODE, state0, t)
    matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')

else:

    state0 = [0.001, 1/2]
    t = np.linspace(0, 60, 6000)
    state = odeint(ODE, state0, t)
    matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')

    state0 = [0.001, 1/4]
    t = np.linspace(0, 60, 6000)
    state = odeint(ODE, state0, t)
    matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')

    state0 = [0.001, 3/4]
    t = np.linspace(0, 60, 6000)
    state = odeint(ODE, state0, t)
    matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')




matplotlib.pyplot.quiver(Y,Z,U,V,scale=12, pivot='mid', alpha=0.5)
matplotlib.pyplot.ylabel("z")
matplotlib.pyplot.xlabel("y")
matplotlib.pyplot.scatter(0,0,s=7,c='r')
matplotlib.pyplot.scatter(1,0,s=7,c='r')
matplotlib.pyplot.scatter(0,1,s=7,c='r')
if s>0:
    matplotlib.pyplot.scatter(0,s,s=7,c='r')

matplotlib.pyplot.rcParams['pdf.fonttype'] = 42
matplotlib.pyplot.savefig('PhasePortraitN4G13C1.pdf',bbox_inches='tight',transparent = True)

matplotlib.pyplot.show()

