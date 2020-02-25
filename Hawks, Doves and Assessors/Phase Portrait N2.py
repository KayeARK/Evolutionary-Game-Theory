import numpy as np
import matplotlib.pyplot
import matplotlib
from scipy.integrate import odeint

G=1
C=1

ydom = np.linspace(0,1,21);
zdom = np.linspace(0,1,21);

[Y,Z] = np.meshgrid(ydom,zdom); # generate mesh of domain

for i in range(len(Y)):
    for j in range(len(Y[i])):
        if Y[i][j]+Z[i][j]>1:
            Y[i][j]=0
            Z[i][j]=0
        

U = (C*Y)-(C*Y*Y)-(2*C*Y*Z)+((G/4)*Y*Z)+(C*Y*Y*Z)+(C*Y*Z*Z); # dy/dt
V = (C*Z)-((G/2)*Z)-(C*Y*Z)+((G/4)*Y*Z)-(2*C*Z*Z)+((G/2)*Z*Z)+(C*Y*Z*Z)+(C*Z*Z*Z); # dz/dt

def ODE(state,t):
  # unpack the state vector
  y = state[0]
  z = state[1]

  # compute state derivatives
  yd = (C*y)-(C*y*y)-(2*C*y*z)+((G/4)*y*z)+(C*y*y*z)+(C*y*z*z)
  zd = (C*z)-((G/2)*z)-(C*y*z)+((G/4)*y*z)-(2*C*z*z)+((G/2)*z*z)+(C*y*z*z)+(C*z*z*z)

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

if 1-(G/(2*C))>0:

    state0 = [0.001, 1-(G/(2*C))]
    t = np.linspace(0, 60, 6000)
    state = odeint(ODE, state0, t)
    matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')

    state0 = [0.001, 0.5-(G/(4*C))]
    t = np.linspace(0, 60, 6000)
    state = odeint(ODE, state0, t)
    matplotlib.pyplot.plot(state[:,0],state[:,1], c='dodgerblue')

    state0 = [0.001, 1-(G/(4*C))]
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




matplotlib.pyplot.quiver(Y,Z,U,V,scale=3, pivot='mid', alpha=0.5)
matplotlib.pyplot.ylabel("z")
matplotlib.pyplot.xlabel("y")
matplotlib.pyplot.scatter(0,0,s=7,c='r')
matplotlib.pyplot.scatter(1,0,s=7,c='r')
matplotlib.pyplot.scatter(0,1,s=7,c='r')
if 1-(G/(2*C))>0:
    matplotlib.pyplot.scatter(0,1-(G/(2*C)),s=7,c='r')

matplotlib.pyplot.rcParams['pdf.fonttype'] = 42
matplotlib.pyplot.savefig('PhasePortraitN2G1C1.pdf',bbox_inches='tight',transparent = True)

matplotlib.pyplot.show()