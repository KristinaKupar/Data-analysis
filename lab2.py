from __future__ import division
import numpy as np
import random

N = 1000
M = 100
MG = 162
z = 0.88

#A), D)

yi = np.array([random.uniform(M+10, MG+2*M) for i in range(N)])
xiRandom = []

for i in range(len(yi)):
    xiRandom.append(random.choice(yi))


xiSystematic = []
for i in range (len(yi), 10):
    xiSystematic.append(i)
print(len(xiSystematic))


#print(Y, Ys, DY2)
#B)
Y = sum(yi)
Ys = sum(yi)/N
DY2 = sum((yi - Ys)**2)/(N-1)

def forXi(xi):
    Ymids = (np.sum(xi))/M
    S = (np.sum((xi - Ymids)**2)/(M - 1))**(1/2)
    SOrYmids = [S, Ymids]
    return(SOrYmids)

Ymids = forXi(xiRandom)[1]
S = forXi(xiRandom)[0]
print(Ymids, S)
Ymid = N*Ymids
print(Ymid)

Ymids = forXi(xiSystematic)[1]
S = forXi(xiSystematic)[0]
print(Ymids, S)

Ymid = N*Ymids
print(Ymid)

DYmids = (S**2/M)*(1 - M/N)
DYmid = DYmids*N**2

YmidsMin = Ymids - ((1 - M/N)**(1/2))*z*S/(M**(1/2))
YmidsMax = Ymids + ((1 - M/N)**(1/2))*z*S/(M**(1/2))

NYmidsMin = YmidsMin*N
NYmidsMax = YmidsMax*N


#E)

xi = np.array(np.random.sample(M))
Stratum1 = []
Stratum2 = []
Stratum3 = []

for i in xiRandom:
    if i <= (M+20):
        Stratum1.append(i)
    elif (M+20) < i < (M+80):
        Stratum2.append(i)
    elif i >= (M+80):
        Stratum3.append(i)


def Nh(Stratum):
    return(len(Stratum))

def RandomSample(Stratum):
    RandomSample = []
    for i in range(len(Stratum)//5):
        RandomSample.append(random.choice(Stratum))
    return(RandomSample)

xiStratified = RandomSample(Stratum1) + RandomSample(Stratum2) + RandomSample(Stratum3)

Nh = [Nh(Stratum1), Nh(Stratum2), Nh(Stratum3)]
nh = [len(RandomSample(Stratum1)), len(RandomSample(Stratum2)), len(RandomSample(Stratum3))]

def wh(Nh, nh, j):
    wh = []
    for j in range(len(Nh)):
        wh.append(Nh[j]/nh[j])
    return(wh[j])

wh = wh(Nh, nh, 0)

def ymidh(Stratum, j):
    return(sum(Stratum)/Nh[j])

ymidh = [ymidh(Stratum1, 0), ymidh(Stratum2, 1), ymidh(Stratum3, 2)]

Yh = [sum(Stratum1), sum(Stratum2), sum(Stratum3)]
Y = sum(Yh)
yu = Y/N

def S2h(Stratum, h):
    S2h = []
    for i in range(Nh[h]):
        S2h.append(((Stratum[i] - ymidh[h])**2))
    return(sum(S2h)/(Nh[h] - 1))

S2h = S2h(Stratum1, 0)

def Wh(Nh, N, i):
    Wh = []
    for i in range(len(Nh)):
        Wh.append(float(Nh[i]/N))
    return(Wh[i])
Wh = Wh(Nh, N, 0)

def valuation(Yh, nh, h):
    valymidh = []
    for h in range(len(Yh)):
        valymidh.append(Yh[h]/nh[h])
    return(valymidh)

h = 0
valymidh = valuation(Yh, nh, h)

def funYmidh(Yh, h):
    Ymidh = []
    for h in range(len(Nh)):
        Ymidh.append(valymidh[h]*Nh[h])
    return(Ymidh)

Ymidh = funYmidh(Yh, 0)

print(Ymidh)

def s2h(Stratum, h):
    s2h = []
    for i in range(nh[h]):
        s2h.append(((Stratum[i] - ymidh[h])**2))
    return(sum(s2h)/(nh[h] - 1))

s2h = s2h(Stratum1, 0)

Yst = sum(Ymidh)
yst = float(Yst/N)

DYst = []
for h in range(3):
    DYst.append((1 - nh[h]/Nh[h])*s2h/nh[h]*Nh[h]**2)

DYst = sum(DYst)
Dyst = DYst/N**2

ystMin = yst - z*Dyst**(1/2)
ystMax = yst - z*Dyst**(1/2)

