import os

def zapis_do_pliku():
    folder = "liczby_folder"
    if not os.path.exists(folder):
        os.mkdir(folder)

    parzyste = os.path.join(folder, "even.txt")
    nieparzyste = os.path.join(folder, "odd.txt")

    plik_parzyste = open(parzyste, "a")
    plik_nieparzyste = open(nieparzyste, "a")

    print("Podaj liczby naturalne. Liczba 0 kończy program.")

    while True:
        liczba = int(input("Podaj liczbę naturalną: "))
        if liczba == 0:
            print("Koniec programu. Liczby zapisane.")
            break
        if liczba % 2 == 0:
            plik_parzyste.write(f"{liczba}\n")
        else:
            plik_nieparzyste.write(f"{liczba}\n")
    plik_parzyste.close()
    plik_nieparzyste.close()

zapis_do_pliku()
