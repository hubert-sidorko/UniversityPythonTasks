import random

lista_ocen = [random.randint(0,5) for i in range(30)]

def indeksiocena(oceny):
    lista = []
    for i in range(0,30):
        wynik = (i, lista_ocen[i])
        lista.append(wynik)
    return lista

lista_krotek = indeksiocena(lista_ocen)

posortowana_rosnaco = sorted(lista_ocen)

slownik_oceny_indeksy = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [] }
for indeks, ocena in lista_krotek:
    if ocena == 0:
        slownik_oceny_indeksy['0'].append(indeks)
    elif ocena == 1:
        slownik_oceny_indeksy['1'].append(indeks)
    elif ocena == 2:
        slownik_oceny_indeksy['2'].append(indeks)
    elif ocena == 3:
        slownik_oceny_indeksy['3'].append(indeks)
    elif ocena == 4:
        slownik_oceny_indeksy['4'].append(indeks)
    elif ocena == 5:
        slownik_oceny_indeksy['5'].append(indeks)

slownik_statystyki = {}
for ocena in lista_ocen:
    if ocena in slownik_statystyki:
        slownik_statystyki[ocena] = slownik_statystyki[ocena] + 1
    else:
        slownik_statystyki[ocena] = 1

slownik_zaliczen = {'zal': [], 'nzal': []}
for indeks, ocena in lista_krotek:
    if ocena >= 3:
        slownik_zaliczen['zal'].append(indeks)
    else:
        slownik_zaliczen['nzal'].append(indeks)

def spr_zaliczenia(lista):
    wynik = []
    for indeks in lista:
        if indeks in slownik_zaliczen['zal']:
            wynik.append((indeks, 'zal'))
        else:
            wynik.append((indeks, 'nzal'))
    return wynik

print(lista_ocen)
print(lista_krotek)
print(posortowana_rosnaco)
print(slownik_oceny_indeksy)
print(slownik_statystyki)
print(slownik_zaliczen)
print(spr_zaliczenia([1, 2, 3, 4, 5, 6]))
