N = 37
for i in range(2, N//2 + 1):
    if N % i == 0:
        print("Liczba nie jest pierwsza")
        break
else:
    print("Liczba jest pierwsza")
