import math
import numpy as np
import matplotlib.pyplot as plt


def generuj_wezly_dla(X_lista):
    wezly_y = []
    for x in X_lista:
        wezly_y.append((x, math.sqrt(x)))
    return wezly_y


def macierz_A(wezly, stopien):
    macierz = np.zeros((stopien + 1, stopien + 1))
    x, _ = zip(*wezly)
    for wiersz in range(stopien + 1):
        wykladnik = stopien + wiersz
        for kolumna in range(stopien + 1):
            macierz[wiersz][kolumna] = suma_poteg(x, wykladnik)
            wykladnik -= 1
    return macierz


def macierz_B(wezly, stopien):
    macierz = np.zeros((stopien + 1,))
    for wiersz in range(stopien + 1):
        wykladnik = wiersz
        for x, y in wezly:
            macierz[wiersz] += x ** wykladnik * y
    return macierz


def wspolczyniki_aproksymacja(wezly, stopien):
    macierz_a = macierz_A(wezly, stopien)
    macierz_b = macierz_B(wezly, stopien)
    odwrocona_macierz_a = np.linalg.inv(macierz_a)
    wspolczynniki = np.matmul(odwrocona_macierz_a, macierz_b)
    return np.flip(wspolczynniki)


def aproksymacja_wielomianowa(wezly, x, stopien):
    wspolczynniki = wspolczyniki_aproksymacja(wezly, stopien)
    return wartosc_wielomanu(wspolczynniki, x)


def wartosc_wielomanu(wspolczynniki, x):
    y = 0
    wykladnik = 0
    for a in wspolczynniki:
        y += (x ** wykladnik) * a
        wykladnik += 1
    return y


def suma_poteg(wektor, wykladnik):
    suma = 0
    for x in wektor:
        suma += x ** wykladnik
    return suma



def oblicz_wspolczynnik_determinacji(X, Y, wspolczynniki):
    srednia = np.average(Y)
    licznik_wspolczynnika = 0
    mianownik_wspolczynnika = 0
    for x, y in zip(X, Y):
        wartosc_teoretyczna = wartosc_wielomanu(wspolczynniki, x)
        licznik_wspolczynnika += (wartosc_teoretyczna - srednia) ** 2
        mianownik_wspolczynnika += (y - srednia) ** 2
    return licznik_wspolczynnika / mianownik_wspolczynnika


def wyswietl_wspolczynniki(wspolczynniki):
    print('Współczynniki wielomianu:')
    for wspolczynnik in wspolczynniki:
        print(wspolczynnik)


def main():
    wezly_x = [100, 121, 144, 169, 196, 225]
    wezly = generuj_wezly_dla(wezly_x)
    x = 20
    stopien = 5

    wartosc_x = aproksymacja_wielomianowa(wezly, x, stopien)
    blad = abs(wartosc_x - math.sqrt(x))
    wartosc_rzeczywista = math.sqrt(x)

    print(f'Węzły {wezly}')
    print(f'Aproksymowana wartość dla x= {x} wynosi{wartosc_x}')
    print(f'Wartosc rzeczywista {wartosc_rzeczywista}')
    print(f'Błąd bezwzględny wynosi {blad}')
    print(f'Błąd względny wynosi {blad / wartosc_rzeczywista * 100} %')

    X = np.arange(0, 500, 0.5)
    Y = [math.sqrt(x) for x in X]
    wspolczynnik_determinacji = oblicz_wspolczynnik_determinacji(X, Y,
                                                                 wspolczyniki_aproksymacja(wezly, stopien))
    print(f'Współczynnik determinacji R^2 wynosi\t\t{wspolczynnik_determinacji}')

if __name__ == "__main__":
    main()
