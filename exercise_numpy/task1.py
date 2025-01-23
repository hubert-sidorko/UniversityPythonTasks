import numpy

def oblicz_e(N):
    if not isinstance(N, int) or N <= 0:
        raise ValueError("N musi być liczbą całkowitą większą od zera")

    n = numpy.arange(1, N + 1)
    ciag = numpy.power(1 + 1 / n, n)
    e = numpy.e
    roznica = numpy.abs(ciag - e)
    return ciag, roznica

def main(N):
    try:
        ciag, roznica = oblicz_e(N)
        return ciag, roznica
    except ValueError as e:
        return f"Błąd: {e}"

if __name__ == "__main__":
    N = 2
    wyniki = main(N)
    if isinstance(wyniki, tuple):
        ciag, roznica = wyniki
        print("Element ciągu i jego różnica do liczby e:")
        for i in range(N):
            if ciag[i].is_integer():
                print(f"{int(ciag[i])} {roznica[i]}")
            else:
                print(f"{ciag[i]} {roznica[i]}")
    else:
        print(wyniki)
