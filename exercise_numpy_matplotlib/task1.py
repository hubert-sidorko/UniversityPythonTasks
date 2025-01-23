import numpy as np
import matplotlib.pyplot as plt
import sys

def wczytywanie_danych(nazwa_pliku):
    try:
        dane = np.loadtxt(nazwa_pliku)
        if dane.shape[1] != 6:
            raise ValueError("Plik musi zawierać 6 kolumn (x, y1, y2, y3, y4, y5).")
        x = dane[:, 0]
        y1 = dane[:, 1]
        y2 = dane[:, 2]
        y3 = dane[:, 3]
        y4 = dane[:, 4]
        y5 = dane[:, 5]
        return x, y1, y2, y3, y4, y5
    except FileNotFoundError:
        print(f"Błąd: Plik '{nazwa_pliku}' nie został znaleziony.")
        sys.exit(1)
    except ValueError as e:
        print(f"Błąd: {e}")
        sys.exit(1)

def rysowanie_danych(x, y1, y2, y3, y4, y5, nazwa_pliku_wyjscie):
    plt.figure(figsize=(8, 6))
    marker_interval = 10
    plt.plot(x, y1, 'r-o', label='y1', markersize=4, linewidth=2, markevery=marker_interval)
    plt.plot(x, y2, 'g--s', label='y2', markersize=6, linewidth=2, markevery=marker_interval)
    plt.plot(x, y3, 'b-.d', label='y3', markersize=5, linewidth=2, markevery=marker_interval)
    plt.plot(x, y4, 'm:>', label='y4', markersize=7, linewidth=2, markevery=marker_interval)
    plt.plot(x, y5, 'k-x', label='y5', markersize=6, linewidth=2, markevery=marker_interval)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Wykres danych")
    plt.legend()
    plt.grid(True)
    plt.savefig(nazwa_pliku_wyjscie, format='png')
    plt.show()

def main():
    if len(sys.argv) != 3:
        print("Błąd: Należy podać dokładnie dwa argumenty.")
        print("Przykład wywołania: python3 'program.py' 'data.txt' 'wykres.png'")
        sys.exit(1)
    nazwa_pliku = sys.argv[1]
    nazwa_pliku_wyjscie = sys.argv[2]
    x, y1, y2, y3, y4, y5 = wczytywanie_danych(nazwa_pliku)
    rysowanie_danych(x, y1, y2, y3, y4, y5, nazwa_pliku_wyjscie)

if __name__ == "__main__":
    main()
