import os
import sys

def plik(sciezka_do_katalogu):
    if not os.path.exists(sciezka_do_katalogu):
        print("Nie istnieje taka ścieżka")
    pliki = []
    for element in os.listdir(sciezka_do_katalogu):
        pelna_sciezka = os.path.join(sciezka_do_katalogu, element)
        if os.path.isfile(pelna_sciezka):
            rozmiar = os.path.getsize(pelna_sciezka)
            pliki.append((element, rozmiar))
    return pliki

def porownanie(katalog1, katalog2):
    pliki_katalog1 = plik(katalog1)
    pliki_katalog2 = plik(katalog2)
    dict_katalog1 = {nazwa: rozmiar for nazwa, rozmiar in pliki_katalog1}
    dict_katalog2 = {nazwa: rozmiar for nazwa, rozmiar in pliki_katalog2}

    takie_same = []
    tylko_w_pierwszym = []
    tylko_w_drugim = []

    for nazwa, rozmiar in dict_katalog1.items():
        if nazwa in dict_katalog2:
            if rozmiar == dict_katalog2[nazwa]:
                takie_same.append(f"{nazwa} {rozmiar}")
            else:
                tylko_w_pierwszym.append(f"{nazwa} {rozmiar}")
    for nazwa, rozmiar in dict_katalog2.items():
        if nazwa not in dict_katalog1:
            tylko_w_drugim.append(f"{nazwa} {rozmiar}")

    with open(f"kat1_oraz_kat2.txt", "w") as wyjscie1:
        wyjscie1.write("\n".join(takie_same))

    with open(f"tylko_kat1.txt", "w") as wyjscie2:
        wyjscie2.write("\n".join(tylko_w_pierwszym))

    with open(f"tylko_kat2.txt", "w") as wyjscie3:
        wyjscie3.write("\n".join(tylko_w_drugim))
def main():
    if len(sys.argv) != 3:
        print("Błąd: Nie podano dwóch katalogów.")
        return
    katalog1 = sys.argv[1]
    katalog2 = sys.argv[2]
    porownanie(katalog1, katalog2)

if __name__ == "__main__":
    main()
