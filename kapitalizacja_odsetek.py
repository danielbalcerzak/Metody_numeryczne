import math

ilosc_lat = int(input('Podaj ilość lat: '))
ilosc_kapitalizacji_lokaty = int(input('Podaj ilosc kapitalizacji w roku lokaty: '))
kwota_poczatkowa = int(input('Podaj kwote poczatkowa lokaty: '))
wysokosc_oprocentowania = float(input('Podaj wysokosc oprocentowania w skali roku: '))
procent = wysokosc_oprocentowania / 100
ilosc_kapitalizacji = ilosc_kapitalizacji_lokaty * ilosc_lat


def licz_zaokr():
    global ilosc_kapitalizacji
    kwota_aktualna = kwota_poczatkowa
    while ilosc_kapitalizacji != 0:
        kwota_aktualna = round(kwota_aktualna, 2) * (1 + (procent / ilosc_kapitalizacji_lokaty))
        ilosc_kapitalizacji -= 1
    return kwota_aktualna


def licz_rekurencyjnie(pozostala_liczba_kapitalizaji):
    if pozostala_liczba_kapitalizaji == 0:
        return kwota_poczatkowa
    else:
        return licz_rekurencyjnie(pozostala_liczba_kapitalizaji - 1) * (1 + (procent / ilosc_kapitalizacji_lokaty))


def licz_niezaokr():
    suma = kwota_poczatkowa * (1 + (procent / ilosc_kapitalizacji_lokaty)) ** (ilosc_lat * ilosc_kapitalizacji_lokaty)
    return suma


#lokata = licz_niezaokr()
lokata = licz_rekurencyjnie(ilosc_kapitalizacji)
lokata_zaokr = licz_zaokr()

blad_bezwzgledny = math.fabs(lokata - lokata_zaokr)
blad_wzgledny = (blad_bezwzgledny / lokata) * 100

if lokata > lokata_zaokr:
    print("lokata niezaokrąglona jest bardziej opłacalna, kwota: ", lokata)
else:
    print("lokata zaokrąglona jest bardziej opłacalna, kwota: ", lokata_zaokr)

print('\n')
print('Blad bezwzgleny wynosi ', blad_bezwzgledny)
print('Blad wzgledny wynosi ', blad_wzgledny, '%')
print('\n')
print(lokata, '\t', lokata_zaokr)
