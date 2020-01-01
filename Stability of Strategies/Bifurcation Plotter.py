from sympy import symbols, solve
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab
from matplotlib import cm#
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import seaborn

'''
N=1

amat=[]
Nmat=[]
solutions=[]
nrange=4
nstep=1
arange=201
astep=0.05

for i in range(nrange):   
    
    a=-astep
    N=N+nstep
    Nmat.append(N)
    solution_=[]
    
    for j in range(arange):
        
        a=a+astep
        amat.append(a)
        
        x = symbols('x', real=True, nonnegative=True)
        expr = (a/N)*(x**N) - (a/N)*x + x*((x-1)**2)*(N-1)

        solution=solve(expr)
        
        if len(solution)==3:
            solutions.append(solution[1])
            
        else:
            solutions.append(0)  
            

a = list(range(0,arange))
a[:] = [x * astep for x in a]
N = list(range(2,nrange+2))
    
X, Y = np.meshgrid(a, N)
X=np.hstack(X)
X=X.tolist()
Y=np.hstack(Y)
Y=Y.tolist()

Z = solutions
'''



X=[ 0.  ,  0.05,  0.1 ,  0.15,  0.2 ,  0.25,  0.3 ,  0.35,  0.4 , 0.45,  0.5 ,  0.55,  0.6 ,  0.65,  0.7 ,  0.75,  0.8 ,  0.85,        0.9 ,  0.95,  1.  ,  1.05,  1.1 ,  1.15,  1.2 ,  1.25,  1.3 , 1.35,  1.4 ,  1.45,  1.5 ,  1.55,  1.6 ,  1.65,  1.7 ,  1.75,        1.8 ,  1.85,  1.9 ,  1.95,  2.  ,  2.05,  2.1 ,  2.15,  2.2 ,        2.25,  2.3 ,  2.35,  2.4 ,  2.45,  2.5 ,  2.55,  2.6 ,  2.65,        2.7 ,  2.75,  2.8 ,  2.85,  2.9 ,  2.95,  3.  ,  3.05,  3.1 ,        3.15,  3.2 ,  3.25,  3.3 ,  3.35,  3.4 ,  3.45,  3.5 ,  3.55,        3.6 ,  3.65,  3.7 ,  3.75,  3.8 ,  3.85,  3.9 ,  3.95,  4.  ,        4.05,  4.1 ,  4.15,  4.2 ,  4.25,  4.3 ,  4.35,  4.4 ,  4.45,        4.5 ,  4.55,  4.6 ,  4.65,  4.7 ,  4.75,  4.8 ,  4.85,  4.9 ,        4.95,  5.  ,  5.05,  5.1 ,  5.15,  5.2 ,  5.25,  5.3 ,  5.35,        5.4 ,  5.45,  5.5 ,  5.55,  5.6 ,  5.65,  5.7 ,  5.75,  5.8 ,        5.85,  5.9 ,  5.95,  6.  ,  6.05,  6.1 ,  6.15,  6.2 ,  6.25,        6.3 ,  6.35,  6.4 ,  6.45,  6.5 ,  6.55,  6.6 ,  6.65,  6.7 ,        6.75,  6.8 ,  6.85,  6.9 ,  6.95,  7.  ,  7.05,  7.1 ,  7.15,        7.2 ,  7.25,  7.3 ,  7.35,  7.4 ,  7.45,  7.5 ,  7.55,  7.6 ,        7.65,  7.7 ,  7.75,  7.8 ,  7.85,  7.9 ,  7.95,  8.  ,  8.05,        8.1 ,  8.15,  8.2 ,  8.25,  8.3 ,  8.35,  8.4 ,  8.45,  8.5 ,        8.55,  8.6 ,  8.65,  8.7 ,  8.75,  8.8 ,  8.85,  8.9 ,  8.95,        9.  ,  9.05,  9.1 ,  9.15,  9.2 ,  9.25,  9.3 ,  9.35,  9.4 ,        9.45,  9.5 ,  9.55,  9.6 ,  9.65,  9.7 ,  9.75,  9.8 ,  9.85,        9.9 ,  9.95, 10.,0.  ,  0.05,  0.1 ,  0.15,  0.2 ,  0.25,  0.3 ,  0.35,  0.4 ,        0.45,  0.5 ,  0.55,  0.6 ,  0.65,  0.7 ,  0.75,  0.8 ,  0.85,        0.9 ,  0.95,  1.  ,  1.05,  1.1 ,  1.15,  1.2 ,  1.25,  1.3 ,        1.35,  1.4 ,  1.45,  1.5 ,  1.55,  1.6 ,  1.65,  1.7 ,  1.75,        1.8 ,  1.85,  1.9 ,  1.95,  2.  ,  2.05,  2.1 ,  2.15,  2.2 ,        2.25,  2.3 ,  2.35,  2.4 ,  2.45,  2.5 ,  2.55,  2.6 ,  2.65,        2.7 ,  2.75,  2.8 ,  2.85,  2.9 ,  2.95,  3.  ,  3.05,  3.1 ,        3.15,  3.2 ,  3.25,  3.3 ,  3.35,  3.4 ,  3.45,  3.5 ,  3.55,        3.6 ,  3.65,  3.7 ,  3.75,  3.8 ,  3.85,  3.9 ,  3.95,  4.  ,        4.05,  4.1 ,  4.15,  4.2 ,  4.25,  4.3 ,  4.35,  4.4 ,  4.45,        4.5 ,  4.55,  4.6 ,  4.65,  4.7 ,  4.75,  4.8 ,  4.85,  4.9 ,        4.95,  5.  ,  5.05,  5.1 ,  5.15,  5.2 ,  5.25,  5.3 ,  5.35,        5.4 ,  5.45,  5.5 ,  5.55,  5.6 ,  5.65,  5.7 ,  5.75,  5.8 ,        5.85,  5.9 ,  5.95,  6.  ,  6.05,  6.1 ,  6.15,  6.2 ,  6.25,        6.3 ,  6.35,  6.4 ,  6.45,  6.5 ,  6.55,  6.6 ,  6.65,  6.7 ,        6.75,  6.8 ,  6.85,  6.9 ,  6.95,  7.  ,  7.05,  7.1 ,  7.15,        7.2 ,  7.25,  7.3 ,  7.35,  7.4 ,  7.45,  7.5 ,  7.55,  7.6 ,        7.65,  7.7 ,  7.75,  7.8 ,  7.85,  7.9 ,  7.95,  8.  ,  8.05,        8.1 ,  8.15,  8.2 ,  8.25,  8.3 ,  8.35,  8.4 ,  8.45,  8.5 ,        8.55,  8.6 ,  8.65,  8.7 ,  8.75,  8.8 ,  8.85,  8.9 ,  8.95,        9.  ,  9.05,  9.1 ,  9.15,  9.2 ,  9.25,  9.3 ,  9.35,  9.4 ,        9.45,  9.5 ,  9.55,  9.6 ,  9.65,  9.7 ,  9.75,  9.8 ,  9.85,        9.9 ,  9.95, 10.,  0.  ,  0.05,  0.1 ,  0.15,  0.2 ,  0.25,  0.3 ,  0.35,  0.4 ,        0.45,  0.5 ,  0.55,  0.6 ,  0.65,  0.7 ,  0.75,  0.8 ,  0.85,        0.9 ,  0.95,  1.  ,  1.05,  1.1 ,  1.15,  1.2 ,  1.25,  1.3 ,        1.35,  1.4 ,  1.45,  1.5 ,  1.55,  1.6 ,  1.65,  1.7 ,  1.75,        1.8 ,  1.85,  1.9 ,  1.95,  2.  ,  2.05,  2.1 ,  2.15,  2.2 ,        2.25,  2.3 ,  2.35,  2.4 ,  2.45,  2.5 ,  2.55,  2.6 ,  2.65,        2.7 ,  2.75,  2.8 ,  2.85,  2.9 ,  2.95,  3.  ,  3.05,  3.1 ,        3.15,  3.2 ,  3.25,  3.3 ,  3.35,  3.4 ,  3.45,  3.5 ,  3.55,        3.6 ,  3.65,  3.7 ,  3.75,  3.8 ,  3.85,  3.9 ,  3.95,  4.  ,        4.05,  4.1 ,  4.15,  4.2 ,  4.25,  4.3 ,  4.35,  4.4 ,  4.45,        4.5 ,  4.55,  4.6 ,  4.65,  4.7 ,  4.75,  4.8 ,  4.85,  4.9 ,        4.95,  5.  ,  5.05,  5.1 ,  5.15,  5.2 ,  5.25,  5.3 ,  5.35,        5.4 ,  5.45,  5.5 ,  5.55,  5.6 ,  5.65,  5.7 ,  5.75,  5.8 ,        5.85,  5.9 ,  5.95,  6.  ,  6.05,  6.1 ,  6.15,  6.2 ,  6.25,        6.3 ,  6.35,  6.4 ,  6.45,  6.5 ,  6.55,  6.6 ,  6.65,  6.7 ,        6.75,  6.8 ,  6.85,  6.9 ,  6.95,  7.  ,  7.05,  7.1 ,  7.15,        7.2 ,  7.25,  7.3 ,  7.35,  7.4 ,  7.45,  7.5 ,  7.55,  7.6 ,        7.65,  7.7 ,  7.75,  7.8 ,  7.85,  7.9 ,  7.95,  8.  ,  8.05,        8.1 ,  8.15,  8.2 ,  8.25,  8.3 ,  8.35,  8.4 ,  8.45,  8.5 ,        8.55,  8.6 ,  8.65,  8.7 ,  8.75,  8.8 ,  8.85,  8.9 ,  8.95,        9.  ,  9.05,  9.1 ,  9.15,  9.2 ,  9.25,  9.3 ,  9.35,  9.4 ,       9.45,  9.5 ,  9.55,  9.6 ,  9.65,  9.7 ,  9.75,  9.8 ,  9.85,        9.9 ,  9.95, 10.  , 0.  ,  0.05,  0.1 ,  0.15,  0.2 ,  0.25,  0.3 ,  0.35,  0.4 ,        0.45,  0.5 ,  0.55,  0.6 ,  0.65,  0.7 ,  0.75,  0.8 ,  0.85,        0.9 ,  0.95,  1.  ,  1.05,  1.1 ,  1.15,  1.2 ,  1.25,  1.3 ,        1.35,  1.4 ,  1.45,  1.5 ,  1.55,  1.6 ,  1.65,  1.7 ,  1.75,        1.8 ,  1.85,  1.9 ,  1.95,  2.  ,  2.05,  2.1 ,  2.15,  2.2 ,        2.25,  2.3 ,  2.35,  2.4 ,  2.45,  2.5 ,  2.55,  2.6 ,  2.65,        2.7 ,  2.75,  2.8 ,  2.85,  2.9 ,  2.95,  3.  ,  3.05,  3.1 ,        3.15,  3.2 ,  3.25,  3.3 ,  3.35,  3.4 ,  3.45,  3.5 ,  3.55,        3.6 ,  3.65,  3.7 ,  3.75,  3.8 ,  3.85,  3.9 ,  3.95,  4.  ,        4.05,  4.1 ,  4.15,  4.2 ,  4.25,  4.3 ,  4.35,  4.4 ,  4.45,        4.5 ,  4.55,  4.6 ,  4.65,  4.7 ,  4.75,  4.8 ,  4.85,  4.9 ,        4.95,  5.  ,  5.05,  5.1 ,  5.15,  5.2 ,  5.25,  5.3 ,  5.35,        5.4 ,  5.45,  5.5 ,  5.55,  5.6 ,  5.65,  5.7 ,  5.75,  5.8 ,        5.85,  5.9 ,  5.95,  6.  ,  6.05,  6.1 ,  6.15,  6.2 ,  6.25,        6.3 ,  6.35,  6.4 ,  6.45,  6.5 ,  6.55,  6.6 ,  6.65,  6.7 ,        6.75,  6.8 ,  6.85,  6.9 ,  6.95,  7.  ,  7.05,  7.1 ,  7.15,        7.2 ,  7.25,  7.3 ,  7.35,  7.4 ,  7.45,  7.5 ,  7.55,  7.6 ,        7.65,  7.7 ,  7.75,  7.8 ,  7.85,  7.9 ,  7.95,  8.  ,  8.05,        8.1 ,  8.15,  8.2 ,  8.25,  8.3 ,  8.35,  8.4 ,  8.45,  8.5 ,        8.55,  8.6 ,  8.65,  8.7 ,  8.75,  8.8 ,  8.85,  8.9 ,  8.95,        9.  ,  9.05,  9.1 ,  9.15,  9.2 ,  9.25,  9.3 ,  9.35,  9.4 ,        9.45,  9.5 ,  9.55,  9.6 ,  9.65,  9.7 ,  9.75,  9.8 ,  9.85,        9.9 ,  9.95, 10.  ]
Y=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,        2, 2, 2,       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,        3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,        3, 3, 3,       4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,        4, 4, 4,       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,        5, 5, 5]
Z=[0, 0.975000000000000, 0.950000000000000, 0.925000000000000, 0.900000000000000, 0.875000000000000, 0.850000000000000, 0.825000000000000, 0.800000000000000, 0.775000000000000, 0.750000000000000, 0.725000000000000, 0.700000000000000, 0.675000000000000, 0.650000000000000, 0.625000000000000, 0.600000000000000, 0.575000000000000, 0.550000000000000, 0.525000000000000, 0.500000000000000, 0.475000000000000, 0.450000000000000, 0.425000000000000, 0.400000000000000, 0.375000000000000, 0.350000000000000, 0.325000000000000, 0.300000000000000, 0.275000000000000, 0.250000000000000, 0.225000000000000, 0.200000000000000, 0.175000000000000, 0.150000000000000, 0.125000000000000, 0.100000000000000, 0.0750000000000000, 0.0500000000000000, 0.0250000000000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.983471074380165, 0.967213114754098, 0.951219512195122, 0.935483870967742, 0.920000000000000, 0.904761904761905, 0.889763779527559, 0.875000000000000, 0.860465116279070, 0.846153846153846, 0.832061068702290, 0.818181818181818, 0.804511278195489, 0.791044776119403, 0.777777777777778, 0.764705882352941, 0.751824817518248, 0.739130434782609, 0.726618705035971, 0.714285714285714, 0.702127659574468, 0.690140845070423, 0.678321678321678, 0.666666666666667, 0.655172413793103, 0.643835616438356, 0.632653061224490, 0.621621621621622, 0.610738255033557, 0.600000000000000, 0.589403973509934, 0.578947368421053, 0.568627450980392, 0.558441558441558, 0.548387096774194, 0.538461538461538, 0.528662420382166, 0.518987341772152, 0.509433962264151, 0.500000000000000, 0.490683229813665, 0.481481481481481, 0.472392638036810, 0.463414634146341, 0.454545454545455, 0.445783132530120, 0.437125748502994, 0.428571428571429, 0.420118343195266, 0.411764705882353, 0.403508771929825, 0.395348837209302, 0.387283236994220, 0.379310344827586, 0.371428571428571, 0.363636363636364, 0.355932203389831, 0.348314606741573, 0.340782122905028, 0.333333333333333, 0.325966850828729, 0.318681318681319, 0.311475409836066, 0.304347826086957, 0.297297297297297, 0.290322580645161, 0.283422459893047, 0.276595744680851, 0.269841269841270, 0.263157894736842, 0.256544502617802, 0.250000000000000, 0.243523316062175, 0.237113402061856, 0.230769230769231, 0.224489795918367, 0.218274111675128, 0.212121212121212, 0.206030150753771, 0.200000000000000, 0.194029850746269, 0.188118811881188, 0.182266009852218, 0.176470588235294, 0.170731707317073, 0.165048543689320, 0.159420289855072, 0.153846153846154, 0.148325358851676, 0.142857142857143, 0.137440758293841, 0.132075471698113, 0.126760563380282, 0.121495327102804, 0.116279069767442, 0.111111111111111, 0.105990783410140, 0.100917431192661, 0.0958904109589041, 0.0909090909090909, 0.0859728506787340, 0.0810810810810811, 0.0762331838565042, 0.0714285714285714, 0.0666666666666667, 0.0619469026548691, 0.0572687224669613, 0.0526315789473684, 0.0480349344978184, 0.0434782608695652, 0.0389610389610390, 0.0344827586206897, 0.0300429184549365, 0.0256410256410256, 0.0212765957446809, 0.0169491525423729, 0.0126582278481013, 0.00840336134453781, 0.00418410041841004, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.987653693698439, 0.975604917723258, 0.963839667835877, 0.952344904633104, 0.941108466417103, 0.930118991736840, 0.919365850334691, 0.908839081421939, 0.898529338364967, 0.888427838995884, 0.878526320872053, 0.868817000902073, 0.859292538834555, 0.849946004172722, 0.840770846134702, 0.831760866327847, 0.822910193846954, 0.814213262541919, 0.805664790231103, 0.797259759663212, 0.788993401053538, 0.780861176040322, 0.772858762924450, 0.764982043070834, 0.757227088363123, 0.749590149615047, 0.742067645851893, 0.734656154384673, 0.727352401607438, 0.720153254455275, 0.713055712466704, 0.706056900399752, 0.699154061355883, 0.692344550370314, 0.685625828431203, 0.678995456893628, 0.672451092257424, 0.665990481280756, 0.659611456403780, 0.653311931459037, 0.647089897647251, 0.640943419759008, 0.634870632624494, 0.628869737774927, 0.622939000300691, 0.617076745892402, 0.611281358052252, 0.605551275463989, 0.599884989510802, 0.594281041931230, 0.588738022603980, 0.583254567453213, 0.577829356466521, 0.572461111818386, 0.567148596092442, 0.561890610596365, 0.556685993763640, 0.551533619636890, 0.546432396427811, 0.541381265149110, 0.536379198314175, 0.531425198700471, 0.526518298172969, 0.521657556564117, 0.516842060607143, 0.512070922919654, 0.507343281034718, 0.502658296476780, 0.498015153879963, 0.493413060146409, 0.488851243642538, 0.484328953431144, 0.479845458537477, 0.475400047247470, 0.470992026436488, 0.466620720926967, 0.462285472873501, 0.457985641173965, 0.453720600905366, 0.449489742783178, 0.445292472643008, 0.441128210943489, 0.436996392289364, 0.432896464973791, 0.428827890538935, 0.424790143353987, 0.420782710209786, 0.416805089929260, 0.412856792992954, 0.408937341178952, 0.405046267216526, 0.401183114452903, 0.397347436532537, 0.393538797088348, 0.389756769444378, 0.386000936329383, 0.382270889600849, 0.378566229979019, 0.374886566790460, 0.371231517720798, 0.367600708576194, 0.363993773053229, 0.360410352516813, 0.356850095785805, 0.353312658926017, 0.349797705050300, 0.346304904125416, 0.342833932785442, 0.339384474151409, 0.335956217656968, 0.332548858879799, 0.329162099378582, 0.325795646535267, 0.322449213402480, 0.319122518555824, 0.315815285950925, 0.312527244785012, 0.309258129362879, 0.306007678967049, 0.302775637731995, 0.299561754522253, 0.296365782814303, 0.293187480582049, 0.290026610185803, 0.286882938264611, 0.283756235631823, 0.280646277173784, 0.277552841751530, 0.274475712105385, 0.271414674762361, 0.268369519946254, 0.265340041490351, 0.262326036752651, 0.259327306533513, 0.256343654995650, 0.253374889586392, 0.250420820962135, 0.247481262914905, 0.244556032300961, 0.241644948971385, 0.238747835704568, 0.235864518140550, 0.232994824717150, 0.230138586607810, 0.227295637661123, 0.224465814341974, 0.221648955674243, 0.218844903185027, 0.216053500850327, 0.213274595042156, 0.210508034477018, 0.207753670165729, 0.205011355364517, 0.202280945527382, 0.199562298259658, 0.196855273272763, 0.194159732340071, 0.191475539253905, 0.188802559783580, 0.186140661634507, 0.183489714408293, 0.180849589563797, 0.178220160379182, 0.175601301914836, 0.172992890977215, 0.170394806083544, 0.167806927427357, 0.165229136844855, 0.162661317782057, 0.160103355262720, 0.157555135857004, 0.155016547650869, 0.152487480216167, 0.149967824581435, 0.147457473203338, 0.144956319938766, 0.142464260017563, 0.139981190015862, 0.137507007830016, 0.135041612651109, 0.132584904940024, 0.130136786403063, 0.127697159968093, 0.125265929761214, 0.122843001083926, 0.120428280390784, 0.118021675267535, 0.115623094409709, 0.113232447601668, 0.110849645696092, 0.108474600593887, 0.106107225224513, 0.103747433526715, 0.101395140429647, 0.0990502618343803, 0.0967127145957819, 0.0943824165047602, 0.0920592862708614, 0.0897432435052112, 0.0874342087037917, 0, 0.990146829105143, 0.980575233219055, 0.971268337448549, 0.962210772274162, 0.953388496986047, 0.944788648537705, 0.936399411516352, 0.928209905759449, 0.920210088798335, 0.912390670824657, 0.904743040284869, 0.897259198536158, 0.889931702261573, 0.882753612556588, 0.875718449774088, 0.868820153358131, 0.862053046014821, 0.855411801666393, 0.848891416715808, 0.842487184217065, 0.836194670603274, 0.830009694672493, 0.823928308571761, 0.817946780554130, 0.812061579312682, 0.806269359720496, 0.800566949826857, 0.794951338978407, 0.789419666949708, 0.783969213981399, 0.778597391635948, 0.773301734391293, 0.768079891901648, 0.762929621862541, 0.757848783424033, 0.752835331102035, 0.747887309142962, 0.743002846301564, 0.738180150995923, 0.733417506807199, 0.728713268294952, 0.724065857101694, 0.719473758322893, 0.714935517120896, 0.710449735563253, 0.706015069667739, 0.701630226637996, 0.697293962275129, 0.693005078551933, 0.688762421337582, 0.684564878261642, 0.680411376707268, 0.676300881924258, 0.672232395253446, 0.668204952454588, 0.664217622130570, 0.660269504241313, 0.656359728701285, 0.652487454055026, 0.648651866225493, 0.644852177330470, 0.641087624562613, 0.637357469129064, 0.633660995246837, 0.629997509190495, 0.626366338388864, 0.622766830567764, 0.619198352935976, 0.615660291411827, 0.612152049887984, 0.608673049532211, 0.605222728121961, 0.601800539410894, 0.598405952525446, 0.595038451389786, 0.591697534177538, 0.588382712788800, 0.585093512351056, 0.581829470742688, 0.578590138137848, 0.575375076571570, 0.572183859524029, 0.569016071522949, 0.565871307763211, 0.562749173742776, 0.559649284914079, 0.556571266350124, 0.553514752424517, 0.550479386504767, 0.547464820658180, 0.544470715369737, 0.541496739271364, 0.538542568882061, 0.535607888358349, 0.532692389254561, 0.529795770292512, 0.526917737140090, 0.524058002198391, 0.521216284396970, 0.518392308996851, 0.515585807400961, 0.512796516971618, 0.510024180854793, 0.507268547810829, 0.504529372051336, 0.501806413081993, 0.499099435551001, 0.496408209102952, 0.493732508237863, 0.491072112175183, 0.488426804722541, 0.485796374149048, 0.483180613062965, 0.480579318293552, 0.477992290776934, 0.475419335445808, 0.472860261122857, 0.470314880417699, 0.467783009627250, 0.465264468639354, 0.462759080839556, 0.460266673020896, 0.457787075296608, 0.455320121015608, 0.452865646680665, 0.450423491869163, 0.447993499156339, 0.445575514040918, 0.443169384873051, 0.440774962784472, 0.438392101620788, 0.436020657875829, 0.433660490627980, 0.431311461478430, 0.428973434491257, 0.426646276135294, 0.424329855227709, 0.422024042879240, 0.419728712441024, 0.417443739452966, 0.415169001593600, 0.412904378631376, 0.410649752377345, 0.408405006639176, 0.406170027176470, 0.403944701657324, 0.401728919616102, 0.399522572412380, 0.397325553191014, 0.395137756843304, 0.392959079969220, 0.390789420840639, 0.388628679365583, 0.386476757053408, 0.384333556980924, 0.382198983759408, 0.380072943502489, 0.377955343794878, 0.375846093661906, 0.373745103539858, 0.371652285247071, 0.369567551955771, 0.367490818164633, 0.365421999672039, 0.363361013550004, 0.361307778118772, 0.359262212922029, 0.357224238702753, 0.355193777379647, 0.353170752024160, 0.351155086838073, 0.349146707131625, 0.347145539302180, 0.345151510813401, 0.343164550174932, 0.341184586922558, 0.339211551598852, 0.337245375734263, 0.335285991828665, 0.333333333333333, 0.331387334633341, 0.329447931030369, 0.327515058725912, 0.325588654804872, 0.323668657219532, 0.321755004773886, 0.319847637108338, 0.317946494684741, 0.316051518771771, 0.314162651430634, 0.312279835501093, 0.310403014587799, 0.308532133046934, 0.306667135973138, 0.304807969186735, 0.302954579221227, 0.301106913311071, 0.299264919379707, 0.297428546027861, 0.295597742522085]


fig = plt.figure()
ax = fig.gca(projection='3d')

one=[]
for i in range(len(X)):
    one.append(1)

zero=[]
for i in range(len(X)):
    zero.append(0)

stability1=[]
for i in range(len(X)):
    stability1.append((X[i]*one[i]**(Y[i]-1))-(X[i]/Y[i])+(Y[i]-1)*(one[i]-1)**2+2*one[i]*(Y[i]-1)*(one[i]-1))

stablez1=[]
stablen1=[]
stablea1=[]
unstablez1=[]
unstablen1=[]
unstablea1=[]

for i in range(len(stability1)):
    if stability1[i]>0:
        unstablez1.append(one[i])
        unstablen1.append(Y[i])
        unstablea1.append(X[i])
    else:
        stablez1.append(one[i])
        stablen1.append(Y[i])
        stablea1.append(X[i])

ax.scatter3D(stablea1, stablen1, stablez1,c='green', s=1.5)
ax.scatter3D(unstablea1, unstablen1, unstablez1,c='red', s=1.5)

stability0=[]
for i in range(len(X)):
    stability0.append((X[i]*zero[i]**(Y[i]-1))-(X[i]/Y[i])+(Y[i]-1)*(zero[i]-1)**2+2*zero[i]*(Y[i]-1)*(zero[i]-1))

stablez0=[]
stablen0=[]
stablea0=[]
unstablez0=[]
unstablen0=[]
unstablea0=[]

for i in range(len(stability0)):
    if stability0[i]>0:
        unstablez0.append(zero[i])
        unstablen0.append(Y[i])
        unstablea0.append(X[i])
    else:
        stablez0.append(zero[i])
        stablen0.append(Y[i])
        stablea0.append(X[i])

ax.scatter3D(stablea0, stablen0, stablez0,c='green', s=1.5)
ax.scatter3D(unstablea0, unstablen0, unstablez0,c='red', s=1.5)
   
for i in range(Z.count(0)):
    d=Z.index(0)
    del Z[d]
    del X[d]
    del Y[d]

stability=[]
for i in range(len(X)):
    stability.append((X[i]*Z[i]**(Y[i]-1))-(X[i]/Y[i])+(Y[i]-1)*(Z[i]-1)**2+2*Z[i]*(Y[i]-1)*(Z[i]-1))

stablez=[]
stablen=[]
stablea=[]
unstablez=[]
unstablen=[]
unstablea=[]

for i in range(len(stability)):
    if stability[i]>0:
        unstablez.append(Z[i])
        unstablen.append(Y[i])
        unstablea.append(X[i])
    else:
        stablez.append(Z[i])
        stablen.append(Y[i])
        stablea.append(X[i])

ax.scatter3D(stablea, stablen, stablez,c='green',s=1.5, label='Stable')
ax.scatter3D(unstablea, unstablen, unstablez,c='red',s=1.5, label='Unstable')
ax.set_xlabel('\u03BB')
ax.set_ylabel('N')
ax.set_zlabel('z')
ax.legend()

plt.rcParams['pdf.fonttype'] = 42
plt.savefig('BifurcationDiagram.pdf',bbox_inches='tight',transparent = True)

plt.show()