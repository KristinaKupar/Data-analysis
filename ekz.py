#!/usr/bin/python
# -*- coding: utf-8 -*-
import pywt
from pylab import *
from numpy import *
import pandas as pd
from random import random
import math
from collections import Counter
import matplotlib.pyplot as plt
text_file = open("V11.txt", "r")
lines = text_file.readlines()
elems = []
for line in lines[:-1]:
    float_elements = [float(i) for i in line[:-2].split(",")]
    elems.append(float_elements)
text_file.close()

x = [i[0] for i in elems]
y1 = [i[1] for i in elems]
y2 = [i[2] for i in elems]

plt.title('Signals graphics')
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()

#task2
print('task2')
list1 = []
list2 = []
for i in elems:
    list1.extend(i[:2])
    list2.append(i[0])
    list2.append(i[2])

dispersion = np.var(elems)
print('dispersion: ', dispersion)
meanDeviation = np.mean(elems)
print('standard deviation: ', meanDeviation)
allElems = []
for i in elems:
    allElems.extend(i)

pd.Series(allElems[:50]).value_counts().plot('bar')
plt.title('distribution histogram')
plt.show()
autocor = np.correlate(allElems, allElems)
plt.plot(poly1d(autocor, y1))
plt.show
cor = np.correlate(list1, list2)
print('autocor: ', autocor, 'cor: ', cor)
spectrum1 = np.fft.fft(list1)
spectrum2 = np.fft.fft(list2)
#print('spectral density for first signal: ', spectrum1)
#print('spectral density for second signal: ', spectrum2)
spectrum = np.fft.fft(allElems)
print ('spectral density: ', spectrum)
#plt.title('spectral density')
#plt.plot(list1)
#plt.plot(list2)
#plt.show()
#task3
print('task 3')
coef = np.corrcoef(y1, y2)
for i in coef[0]:
    if i == 0:
        print('there is no correlation')
    else:
        if i < 0 and i < (-0.5):
            print('correlation is negative')
            coefcor = i
            y2 = [coefcor * i[2] for i in elems]
            plt.scatter(y1, y2)
            plt.title('linear dependence between signals')
            plt.show()
        if i < 0 and i > (-0.5):
            print('correlation is negative')
            poly = polyfit(y1, y2, 2)
            print('poly: ', poly)
            plt.title('polynom')
            po1d = poly1d(poly)
            #plt.scatter(y1, y2)
            plt.plot(y1, po1d(y1))
            plt.show()
        if i > 0 and i < 1:
            print('correlation is positive')
#print(coef)

y1_avr = sum(y1)/len(y1)
y2_avr = sum(y2)/len(y2)
b = (len(y1) * sum([i*z for i, z in zip(y1, y2)]) - y1_avr*y2_avr)/\
    (len(y1)*sum([i**2 for i in y1]) - y1_avr**2)
a = y2_avr - b*y1_avr

S_hyp_square = sum(map(lambda iter: (iter[1] - a - b*iter[0]) ** 2, zip(y1, y2)))/(len(y1)-2)
S_x_square = sum(map(lambda y1: (y1 - y1_avr) ** 2, y1))/(len(y1)-1)

S_y_square = sum(map(lambda y2: (y2 - y2_avr) ** 2, y2))/(len(y1)-1)
if float(input("Input Fisher with {0} and {1} freedom: ".format(len(y1)-2, len(y1)-1))) > (S_hyp_square/S_y_square):
    print("Model is good")
else:
    print("Model is not good")

#task4
st='haar'
c = 0
for i in range(2):
    (af1, df1) = pywt.dwt(y1[:1000],st)
    (af2, df2) = pywt.dwt(y2[:1000],st)
    subplot(2, 1, 1)
    if c == 0:
        plt.title('Haar wavelet')
    else:
        plt.title('Symlets wavelet')
    plot(af1,'b',linewidth=2, label='approximation factors')
    plot(af2,'y',linewidth=2)
    grid()
    legend(loc='best')
    subplot(2, 1, 2)
    plot(df1,'b',linewidth=2, label='detail factors')
    plot(df2,'y',linewidth=2)
    grid()
    legend(loc='best')
    show()
    c =+ 1
    st = 'sym7'
#task5
k = 2
alpha = 0.95
A = [y1, y2]
S = [(sum(map(lambda x: x**2, i)) - sum(i)**2/len(y1))/(len(y1)-1) for i in A]

g = max(S)/sum(S)
#if g > float(input("Input g when k = {0} n = {1} and Aplha = {2}:\n".format(k, len(y1), alpha))):
#        print("The hypothesis of equality of dispersion is rejected")


Sum_of_squares = sum([sum(map(lambda x: x**2, i)) for i in A])
Square_of_sum = sum([sum(i)**2 for i in A])
S0 = (Sum_of_squares - Square_of_sum/len(y1))/(5*(len(y1) - 1))
S = (Sum_of_squares - Square_of_sum/5*len(y1))/(5*len(y1) - 1)
SA = (sum([(sum(i)/len(i) - sum(
        [sum(x)/len(x) for x in A])/5)**2 for i in A]))*len(y1)/(5-1)
#print("S0 =", S0)
#print("SA =", SA)
#print("SA/S0 =", SA/S0)
if SA/S0 > meanDeviation:
        print("Factor A has significant influence")
else:
    print("Factor A has not significant influence")