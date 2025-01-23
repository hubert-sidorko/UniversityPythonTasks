import os

def wyniki_plik(plik):
    with open(plik, "r") as dane:
        liczby = [int(wiersz.strip()) for wiersz in dane if wiersz.strip().isdigit()]
        if liczby:
            ilosc = len(liczby)
            suma = sum(liczby)
            srednia_aryt = suma / ilosc
        return ilosc, suma, srednia_aryt

def przetworz_pliki(plik1, plik2):
    wynik_plik1 = wyniki_plik(plik1)
    wynik_plik2 = wyniki_plik(plik2)
    return wynik_plik1, wynik_plik2

def main():
    folder = "liczby_folder"
    if not os.path.exists(folder):
        print(f"Folder {folder} nie istnieje!")
        return

    pliki_w_folderze = os.listdir(folder)

    even_file = os.path.join(folder, "even.txt")
    odd_file = os.path.join(folder, "odd.txt")

    if "even.txt" in pliki_w_folderze and "odd.txt" in pliki_w_folderze:
        wynik_plik1, wynik_plik2 = przetworz_pliki(even_file, odd_file)

        print(f"Plik 1: {even_file}")
        print(f"Ilosc: {wynik_plik1[0]}, Suma: {wynik_plik1[1]}, Srednia: {wynik_plik1[2]:.2f}")

        print(f"Plik 2: {odd_file}")
        print(f"Ilosc: {wynik_plik2[0]}, Suma: {wynik_plik2[1]}, Srednia: {wynik_plik2[2]:.2f}")
    else:
        print("Brakuje plików 'even.txt' lub 'odd.txt' w folderze.")

if __name__ == "__main__":
    main()
