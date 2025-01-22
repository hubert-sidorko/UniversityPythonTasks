lista_przykladowa = [1, 6, 6, 6, 6, 5, 2, 2, 4, 3]

def jeden(lista):
    wynik = len(lista)
    return wynik

def dwa(lista):
    nie_powtarzaja = []
    suma = 0
    for liczba in lista:
        if lista.count(liczba) == 1:
            nie_powtarzaja.append(liczba)
            suma += 1
    return nie_powtarzaja, suma

def trzy(lista):
    posortowana = sorted(lista)
    posortowana_bezpowtorek = set(posortowana)
    lista_gotowa = []
    for i in posortowana_bezpowtorek:
        lista_gotowa.append(i)
    return lista_gotowa

def cztery(lista):
    dl = len(lista)
    return lista[0:dl-1]

def piec(lista):
    ostatni = lista[-1]
    lista.append(ostatni)
    pomocnicza = []
    pomocnicza.append(ostatni)
    wynik = pomocnicza + lista
    return wynik

def szesc(lista):
    nieparzyste = []
    parzyste = []
    for i in range(len(lista)):
        if i % 2 == 0:
            parzyste.append(lista[i])
        else:
            nieparzyste.append(lista[i])
    return nieparzyste + parzyste

def zadanie(lista):
    wynik1 = jeden(lista)
    print(f"Długość listy to: {wynik1}")
    wynik2 = dwa(lista)
    print(f"Elementy, które się nie powtarzają: {wynik2[0]}; jest ich {wynik2[1]}")
    wynik3 = trzy(wynik2[0])
    print(f"Posortowana lista bez powtarzających się elementów: {wynik3}")
    wynik4 = cztery(wynik3)
    print(f"Lista bez ostatniego elementu: {wynik4}")
    wynik5 = piec(wynik4)
    print(f"Lista z ostatnim elementem dodanym na początku i na końcu: {wynik5}")
    wynik6 = szesc(wynik5)
    print(f"Najpierw elementy o indeksach nieparzystych, a potem parzystych: {wynik6}")

zadanie(lista_przykladowa)
