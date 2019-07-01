from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
import collections as col

x0 = [-1.2, 0]
N = 2
M = int(1.65*N + 0.05*N**2)
xc = []
e = 0.1

def function(x):
    fx = 100*(x[0]**2 - x[1])**2 + (x[0] - 1)**2
    return fx

def triangle():
    a = 1
    d0 = a * ((N + 1) ** (1 / 2) + N - 1) / N * 2 ** (1 / 2)
    d1 = a * ((N + 1) ** (1 / 2) - 1) / N * 2 ** (1 / 2)

    x1 = [x0[0] + d1, x0[1] + d0]
    x2 = [x0[0] + d0, x0[1] + d1]

    setx = []
    xvector = [x0, x1, x2]
    xmin = 0
    counter = 0
    while 1:
        xci = []
        fxlist = [function(xvector[0]), function(xvector[1]), function(xvector[2])]
        Hi = []
        R = []
        dist = []
        i = 0
        dist.append(math.sqrt( (xvector[2][0] - xvector[1][0])**2 + (xvector[2][1] - xvector[1][1])**2 ))
        dist.append(math.sqrt((xvector[1][0] - xvector[0][0]) ** 2 + (xvector[1][1] - xvector[0][1]) ** 2))
        R = sum(dist)
        Hi.append((fxlist[2] - fxlist[1]) / R)
        Hi.append((fxlist[1] - fxlist[0]) / R)
        H = sum(Hi)
        Lambda = []
        for i in range(len(Hi)):
            Lambda.append(Hi[i] / H)
        if a < 1:
            d0 = a * ((N + 1) ** (1 / 2) + N - 1) / N * 2 ** (1 / 2)
            d1 = a * ((N + 1) ** (1 / 2) - 1) / N * 2 ** (1 / 2)
            x1 = [xmin[0] + d1, xmin[1] + d0]
            x2 = [xmin[0] + d0, xmin[1] + d1]
            xvector = [xmin, x1, x2]
        for i in range(len(xvector)):
            for j in range(len(x0)):
                xci.append(Lambda[j] * xvector[i][j])
        for x in xvector:
            if function(x) == max(fxlist):
                xmax = x
            elif function(x) == min(fxlist):
                xmin = x
            else:
                xmead = x
        xnew = []
        for i in range(len(x0)):
            xnew.append(2*xci[i] - xmax[i])
        xvector = [xmin, xmead, xnew]

        if counter % M == 0:
            setx.append(xvector)

            for x in setx:
                for y in x:
                    for z in y:
                        unique = np.unique(setx, return_counts = True)
            for s in unique[1]:
                if s > 1:
                    a = a*0.5
                    break
            print('minimum x: ', xmin)
            print('function: ', function(xmin))
            print(counter)
        print(function(xmax))
        if function(xmin) < e:
            print('minimum x: ', xmin)
            print('function: ', function(xmin))
            print(counter)
            break
        counter = counter + 1

    return setx

def calcS(x):
    s = (x[0][0] - x[2][0])*(x[1][1] - x[2][1])/2 - (x[0][1] - x[2][1])*(x[1][0] - x[2][0])/2
    return(abs(s))

a = 2
d0 = a * ((N + 1) ** (1 / 2) + N - 1) / N * 2 ** (1 / 2)
d1 = a * ((N + 1) ** (1 / 2) - 1) / N * 2 ** (1 / 2)

x1 = [x0[0] + d1, x0[1] + d0]
x2 = [x0[0] + d0, x0[1] + d1]
xvector = [x0, x1, x2]
print('S: ', calcS(xvector))


#xvectorGraphic = np.array(triangle())
arrays = []
setx = triangle()
for i in range(len(setx)):
    arrays.append(np.array(setx[len(setx) - i - 1]))

plt.figure()
plt.scatter(arrays[len(arrays) - 1][:,0], arrays[len(arrays) - 1][:,1], s = 10, color = 'green')

for i in arrays:
    t1 = plt.Polygon(i[:3,:], color = 'green', fill=False)
    plt.gca().add_patch(t1)
plt.show()
