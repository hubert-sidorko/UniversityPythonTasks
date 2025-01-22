import math

def przyblizenie_cosinus(N, x):
    wynik = 0
    for i in range(N+1):
        obliczenie = (((-1)**i) / math.factorial(2*i)) * (x ** (2*i))
        wynik = wynik + obliczenie
    return wynik

cos_pi4 = math.pi / 4
for N in range(2,11):
    print(f"Dla {N}: przyblizenie jest rowne: {przyblizenie_cosinus(N, cos_pi4)}")
