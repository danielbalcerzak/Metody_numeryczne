# UKŁADY RÓWNAŃ

# A*X1 + B*X2 + C*X3 + D*X4 = E
# F*X1 + G*X2 + H*X3 + I*X4 = J
# K*X1 + L*X2 + M*X3 + N*X4 = O
# P*X1 + R*X2 + S*X3 + T*X4 = U
#
# a=[[A,B,C,D]    x=[[X1]   b= [[W]
#    [F,G,H,I]       [X2]       [X]
#    [K,L,M,N]       [X3]       [Y]
#    [P,R,S,T]       [X4]]      [Z]]
#
# ax = b
#
# X1 = A
#
#
#

zal_zer_przyb = 0

a = [[4, -1, -0.2, 2],
     [-1, 5, 0, -2],
     [0.2, 1, 10, -1],
     [0, -2, -1, 4]]

b = [[30],
     [0],
     [-10],
     [5]]

blad = 0.001


class X:

    def __init__(self, liczba1, liczba2, liczba3, liczba4, lista, lista_wynik):
        self.wynik = lista_wynik[0]
        self.pierwszy_wspolczynnik = lista[0]
        self.drugi_wspolczynnik = lista[1]
        self.trzeci_wspolczynnik = lista[2]
        self.czwarty_wspolczynnik = lista[3]
        self.x1 = liczba1
        self.x2 = liczba2
        self.x3 = liczba3
        self.x4 = liczba4

    def zwroc(self):
        return (self.wynik - self.drugi_wspolczynnik * self.x2 -
                self.trzeci_wspolczynnik * self.x3 -
                self.czwarty_wspolczynnik * self.x4) / self.pierwszy_wspolczynnik


class X2(X):

    def zwroc(self):
        return (self.wynik - self.pierwszy_wspolczynnik * self.x1 -
                self.trzeci_wspolczynnik * self.x3 -
                self.czwarty_wspolczynnik * self.x4) / self.drugi_wspolczynnik


class X3(X):

    def zwroc(self):
        return (self.wynik - self.pierwszy_wspolczynnik * self.x1 -
                self.drugi_wspolczynnik * self.x2 -
                self.czwarty_wspolczynnik * self.x4) / self.trzeci_wspolczynnik


class X4(X):

    def zwroc(self):
        if self.czwarty_wspolczynnik != 0:
            return (self.wynik - self.pierwszy_wspolczynnik * self.x1 -
                    self.drugi_wspolczynnik * self.x2 -
                    self.trzeci_wspolczynnik * self.x3) / self.czwarty_wspolczynnik
        else:
            return 0


x1 = X(zal_zer_przyb, zal_zer_przyb, zal_zer_przyb, zal_zer_przyb, a[0], b[0])
x2 = X2(x1.zwroc(), zal_zer_przyb, zal_zer_przyb, zal_zer_przyb, a[1], b[1])
x3 = X3(x1.zwroc(), x2.zwroc(), zal_zer_przyb, zal_zer_przyb, a[2], b[2])
x4 = X4(x1.zwroc(), x2.zwroc(), x3.zwroc(), zal_zer_przyb, a[3], b[3])


def czy_blad(liczba1, liczba2):
    if (liczba1 - liczba2) < blad:
        return True
    else:
        return False


def gauss_seidl(xjeden, xdwa, xtrzy, xcztery):
    x_1 = X(zal_zer_przyb, xdwa.zwroc(), xtrzy.zwroc(), xcztery.zwroc(), a[0], b[0])
    x_2 = X2(x_1.zwroc(), zal_zer_przyb, xtrzy.zwroc(), xcztery.zwroc(), a[1], b[1])
    x_3 = X3(x_1.zwroc(), x_2.zwroc(), zal_zer_przyb, xcztery.zwroc(), a[2], b[2])
    x_4 = X4(x_1.zwroc(), x_2.zwroc(), x_3.zwroc(), zal_zer_przyb, a[3], b[3])

    if czy_blad(x_1.zwroc(), xjeden.zwroc()) is True \
            and czy_blad(x_2.zwroc(), xdwa.zwroc()) is True \
            and czy_blad(x_3.zwroc(), xtrzy.zwroc()) is True \
            and czy_blad(x_3.zwroc(), xtrzy.zwroc()) is True:
        print(f"Wartości x1 = {round(x_1.zwroc(),6)}, x2 = {round(x_2.zwroc(),6)}, "
              f"x3 = {round(x_3.zwroc(),6)}, x4 = {round(x_4.zwroc(),6)} "
              f"można przyjąć za rozwiązanie")
        return False

    else:
        gauss_seidl(x_1, x_2, x_3, x_4)


gauss_seidl(x1, x2, x3, x4)
