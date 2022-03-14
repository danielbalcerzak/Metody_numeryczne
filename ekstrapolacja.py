def szukaj_wysokosc(x, y):
    return x - y

def ekstrapolacja_x_mniejsze(wezly, szukana):
    fx = wezly[0][1] + ((szukana-wezly[0][0])*(4 * wezly[1][1]-wezly[2][1]-3*wezly[0][1])) / \
         (2*szukaj_wysokosc(wezly[1][0], wezly[0][0]))
    return fx

def ekstrapolacja_x_wieksze(wezly, szukana):
    fx = wezly[2][1] +((szukana-wezly[2][0])*(3*wezly[2][1]+wezly[0][1]-4*wezly[1][1])) / \
        (2*szukaj_wysokosc(wezly[2][0], wezly[1][0]))
    return fx

def czy_x_mniejsze(wezly, szukana):
    if szukana < wezly[0][0]:
        return True
    else:
        return False

def funkcja_kwadratowa(x):
    return x**2

def stworz_wezly(lista):
    lista_wezlow = []
    for i in lista:
        krotka = (i, funkcja_kwadratowa(i))
        lista_wezlow.append(krotka)
    return lista_wezlow


def main():
    punkty_x = [-50, 25, 100]
    x_szukana_wartosc = 175
    wspolrzedne_punktow = stworz_wezly(punkty_x)
    if czy_x_mniejsze(wspolrzedne_punktow,x_szukana_wartosc):
        fx = ekstrapolacja_x_mniejsze(wspolrzedne_punktow, x_szukana_wartosc)
    else:
        fx = ekstrapolacja_x_wieksze(wspolrzedne_punktow, x_szukana_wartosc)

    wartosc_rzeczywista = funkcja_kwadratowa(x_szukana_wartosc)
    blad_bezwzgledny = abs(funkcja_kwadratowa(x_szukana_wartosc)-fx)
    blad_wzgledny = (abs(funkcja_kwadratowa(x_szukana_wartosc)- fx )) / funkcja_kwadratowa(x_szukana_wartosc) * 100

    print(f"Wezly to: {wspolrzedne_punktow}")
    print(f"Wartość dla x={x_szukana_wartosc} to {fx}")
    print(f"Wartość rzeczywista dla f(x) = 175^2 = {wartosc_rzeczywista}")
    print(f"Bląd bezwzględny wynosi {blad_bezwzgledny}")
    print(f"Bląd wzgldny wynosi {format(blad_wzgledny,'.3f')} %")


if __name__ == '__main__':
    main()
