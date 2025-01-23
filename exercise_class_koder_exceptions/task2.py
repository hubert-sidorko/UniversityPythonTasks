from task1 import Koder

def main():
    dict_encode = {'a': 'j', 'ą': 'k', 'b': 'l', 'c': 'ł', 'ć': 'm', 'd': 'n', 'e': 'ń', 'ę': 'o', 'f': 'ó',
                   'g': 'p', 'h': 'r', 'i': 's', 'j': 'ś', 'k': 't', 'l': 'u', 'ł': 'w', 'm': 'x', 'n': 'y', 'ń': 'z',
                   'o': 'ź', 'ó': 'ż', 'p': 'a', 'r': 'ą', 's': 'b', 'ś': 'c', 't': 'ć', 'u': 'd', 'w': 'e', 'x': 'ę',
                   'y': 'f', 'z': 'g', 'ź': 'h', 'ż': 'i'}

    koder = Koder(dict_encode)

    try:
        tekst = input("Podaj wiadomość do zakodowania: ")
        tekst = tekst.lower()
        tekst = ''.join([litera for litera in tekst if litera not in [' ', ',', '.']])

        zakodowany = koder.zakoduj(tekst)
        print(f"\nZakodowana wiadomość: {''.join(zakodowany)}")

        odkodowany = koder.odkoduj(zakodowany)
        print(f"Odkodowana wiadomość: {''.join(odkodowany)}")

        print("\nStatystyki znaków w zakodowanej wiadomości:")
        print(koder.statystyki(zakodowany))

        print("Statystyki znaków w odkodowanej wiadomości:")
        print(koder.statystyki(odkodowany))

    except KeyError as error:
        print(f"Błąd: {error}")

    except Exception as error:
        print(f"Błąd: {error}")

    finally:
        print("\nWesołych Świąt!")
        print("--- Zakończenie działania ---")

if __name__ == "__main__":
    main()
