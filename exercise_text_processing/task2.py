def usuwanie(wyraz):
    for i in range(len(wyraz)-1, -1, -1):
        if wyraz[i].isalnum():
            break
        else:
            wyraz = wyraz[:-1]
    return wyraz

def zamiana(wyraz):
    wyraz = usuwanie(wyraz)
    wyraz = wyraz.capitalize()
    if wyraz and wyraz[-1] != ".":
        wyraz += "."
    return wyraz

def zdania(tekst):
    tekst = tekst.split(".")
    przetworzone_zdania = [zamiana(wyraz.strip()) for wyraz in tekst if wyraz.strip()]
    return " ".join(przetworzone_zdania)

def main():
    wynik = zdania("poszła Ola do przedszkola. zapomniała parasola . A parasol był popsuty, połamane wszystkie druty .w.")
    print(wynik)

if __name__ == "__main__":
    main()
