def usuniecie_spacji_i_powtorek(zbior):
    zbior = zbior.strip()
    if zbior.startswith("{") and zbior.endswith("}"):
        zbior = zbior[1:-1].split(",")
        wynik = {element.strip() for element in zbior}
        return wynik
    else:
        return None

def main():
    wynik = ""
    wyrazenia = input("Podaj wyrazenia: ")
    operator = ""
    for operatory in ["+", "-", "*"]:
        if operatory in wyrazenia:
            operator = operatory
            break
    if operatory not in wyrazenia:
        print("Brak operatora")
        return None

    zbiory = wyrazenia.split(operator)
    if len(zbiory) != 2:
        print("Blad")
        return None

    zbior_nr1 = usuniecie_spacji_i_powtorek(zbiory[0])
    zbior_nr2 = usuniecie_spacji_i_powtorek(zbiory[1])

    if zbior_nr1 is None or zbior_nr2 is None:
        print("Brak jednego ze zbiorow")
        return None

    if operator == "+":
        wynik = zbior_nr1 | zbior_nr2
    elif operator == "-":
        wynik = zbior_nr1 - zbior_nr2
    elif operator == "*":
        wynik = zbior_nr1 & zbior_nr2
    else:
        print("Blad")
    wynik = ', '.join(f"'{element}'" for element in sorted(wynik))
    wynik_w_poprawnym_zapisie = "{" + wynik + "}"
    print(wynik_w_poprawnym_zapisie)

if __name__ == "__main__":
    main()
