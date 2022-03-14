import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange

lista_wezlow = []
szukana_liczba = 14
tablica_x = [1, 4, 9, 16, 25]
tablica_y =[]

def wezly_dla_wartosci(argument_funkcji):
    wartosc_funkcji = math.sqrt(argument_funkcji)
    return argument_funkcji, wartosc_funkcji

for i in tablica_x:
    lista_wezlow.append(wezly_dla_wartosci(i))
    # print(lista_wezlow)

def wspolczynnik(argument, funkcja):
    return lagrange(argument, funkcja)

for wezel in lista_wezlow:
    tablica_y.append(wezel[1])


wspolczynniki = wspolczynnik(tablica_x, tablica_y)

x2 = np.linspace(0,40,500)
y2 = []

for x in x2:
    y2.append(wspolczynniki(x))

y_rzeczywiste = []

for x in x2:
    y_rzeczywiste.append(math.sqrt(x))

plt.plot(x2, y2, 'r', x2, y_rzeczywiste, 'g')
plt.show()








