import numpy

def rozwiaz_uklad(A, b):
    if numpy.linalg.det(A) == 0:
        raise ValueError("Wyznacznik macierzy jest równy 0, macierz A jest osobliwa. Nie można rozwiązać układu")
    Q, R = numpy.linalg.qr(A)
    y = numpy.dot(Q.T, b)
    R_inv = numpy.linalg.inv(R)
    x = numpy.dot(R_inv, y)
    return x

def main():
    A1 = numpy.array([[1, 2], [1, -1]])
    b1 = numpy.array([3, -3])
    try:
        x1 = rozwiaz_uklad(A1, b1)
        print("Rozwiązanie układu A1 * x = b1:", x1)
    except ValueError as e:
        print("Błąd:", e)

    A2 = numpy.array([[1, 2], [2, 4]])
    b2 = numpy.array([9, 18])
    try:
        x2 = rozwiaz_uklad(A2, b2)
        print("Rozwiązanie układu A2 * x = b2:", x2)
    except ValueError as e:
        print("Błąd:", e)

    A3 = numpy.array([[1, 0, -1, 0, 1], [0, 2, -1, 1, 0], [-1, 1, -1, 1, 0], [1, 2, 0, 2, 1], [2, 0, 2, 0, -1]])
    b3 = numpy.array([1, 2, 0, 6, 3])
    try:
        x3 = rozwiaz_uklad(A3, b3)
        print("Rozwiązanie układu A3 * x = b3:", x3)
    except ValueError as e:
        print("Błąd:", e)

if __name__ == "__main__":
    main()
