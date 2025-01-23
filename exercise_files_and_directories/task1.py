import sys

def dane_studentow(plik_wejscie):
    studenci = {}
    with open(plik_wejscie, 'r') as plik:
        for linia in plik:
            dane = linia.strip().split(',')
            imie = dane[0]
            nazwisko = dane[1]
            numer_indeksu = int(dane[2])
            oceny = list(map(int, dane[3:]))
            studenci[numer_indeksu] = {'imię': imie, 'nazwisko': nazwisko, 'oceny': oceny}
    return studenci

def srednie(studenci, plik_wyjscie):
    with open(plik_wyjscie, 'w') as plik:
        for numer_indeksu, dane in studenci.items():
            oceny = dane['oceny']
            srednia = sum(oceny) / len(oceny) if oceny else 0
            plik.write(f"{numer_indeksu},{dane['nazwisko']},{srednia:.2f}\n")

def main():
    if len(sys.argv) != 3:
        print("Błąd plików")
        return
    plik_wejscie = sys.argv[1]
    plik_wyjscie = sys.argv[2]
    studenci = dane_studentow(plik_wejscie)
    srednie(studenci, plik_wyjscie)
    print(f"Średnie zostały zapisane do pliku {plik_wyjscie}")

if __name__ == "__main__":
    main()
