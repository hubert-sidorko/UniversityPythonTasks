import numpy as np
import matplotlib.pyplot as plt
import sys

def rysuj_krzywa_lissajous(A, B, a, b, delta):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label=f"A={A}, B={B}, a={a}, b={b}, δ={delta}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Krzywa Lissajous")
    plt.legend()
    plt.grid(True)
    plt.autoscale(enable=True, axis='both', tight=True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-max(A, B), max(A, B))
    plt.ylim(-max(A, B), max(A, B))
    plt.show()
    plt.tight_layout()
    plt.show()

def main():
    if len(sys.argv) != 6:
        print("Błąd: Należy podać dokładnie 5 argumentów:")
        print("Przykład wywołania: 'python3' 'program.py' A B a b delta")
        sys.exit(1)
    try:
        A = float(sys.argv[1])
        B = float(sys.argv[2])
        a = float(sys.argv[3])
        b = float(sys.argv[4])
        delta = float(sys.argv[5])
    except ValueError:
        print("Błąd: Wszystkie parametry muszą być liczbami zmiennoprzecinkowymi.")
        sys.exit(1)
    rysuj_krzywa_lissajous(A, B, a, b, delta)

if __name__ == "__main__":
    main()
