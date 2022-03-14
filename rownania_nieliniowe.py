from math import exp, pow

# ILOŚ ITERACJI
ITERACJA = 18

# WSPÓŁCZYNNNIKI e^x + A*x^2 + B*x + C = 0
A = 1
B = 0
C = -2

# ZADANY PRZEDZIAŁ
OD = 0
DO = 1

# SPRAWDZENIE CZY ZADANY PRZEDZIAŁ JEST PRZEDZIAŁEM PIERWIASTKA:

def czy_przedzial_jest_pierwiastkiem():
    FodA = exp(OD) + A * (pow(OD, 2) + B * OD + C)
    FodB = exp(DO) + A * (pow(DO, 2) + B * DO + C)

    if FodA*FodB < 0:
        return True
    else:
        return False

def liczba_a(a, fx, fa, polowa):
    if fx*fa < 0:
        return a
    else:
        return polowa

def liczba_b(b, fx, fb, polowa):
    if fx*fb < 0:
        return b
    else:
        return polowa

def metoda_polowienia(a, b, iteracja):
    iteracja = 0
    polowa = (a + b) / 2
    fodx = exp(polowa) + A*(pow(polowa,2) + B * polowa + C)
    foda = exp(a) + A * (pow(a, 2) + B * a + C)
    fodb = exp(b) + A * (pow(b, 2) + B * b + C)
    print("a=", a, "b=", b, "Błąd =", a-b)
    iteracja += 1

    if abs(a-b) < 0.00000001:
        print("koniec")
    else:
        metoda_polowienia(liczba_a(a, fodx, foda, polowa), liczba_b(b, fodx, fodb, polowa), iteracja)


if czy_przedzial_jest_pierwiastkiem() is True:
    metoda_polowienia(OD,DO, ITERACJA)
else:
    print("W podanym przedziale nie znajduje się pierwiastek")