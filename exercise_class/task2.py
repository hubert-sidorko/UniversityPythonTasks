from task1 import PhoneBook

def main():
    ksiazka1 = PhoneBook("Książka nr1")
    ksiazka1.add_record("Joanna", "111111111")
    ksiazka1.add_record("Kasia", "222222222")

    ksiazka2 = PhoneBook("Książka nr2")
    ksiazka2.add_record("Jan", "333333333")

    ksiazka3 = PhoneBook("Książka nr3")

    ksiazka4 = PhoneBook("Książka nr4")
    ksiazka4.add_record("Jan", "333333333")

    ksiazka5 = PhoneBook("Książka nr5")
    ksiazka5.add_record("Jan", "33333222")

    print("Zawartość Książki 1:")
    ksiazka1.show_records()

    print("\nZawartość Książki 2:")
    ksiazka2.show_records()

    print("\nZawartość Książki 3:")
    ksiazka3.show_records()

    print("\nKsiążka 1:", ksiazka1)
    print("Książka 2:", ksiazka2)

    print("\nCzy książki Książka 1 i Książka 2 mają te same identyfikatory i rekordy?", ksiazka1 == ksiazka2)

    print("Czy książki Książka 4 i Książka 5 mają te same identyfikatory i rekordy?", ksiazka4 == ksiazka5)

    print("Czy Książka 1 ma więcej rekordów niż Książka 2?", ksiazka1 > ksiazka2)

    ksiazka2.add_record("Walery", "444444444")
    ksiazka2.add_record("Bartek", "555555555")

    print("\nNowe rekordy Książki 2:")
    ksiazka2.show_records()
    print("\nCzy Książka 1 ma więcej elementów niż Książka 2", ksiazka1 > ksiazka2)

if __name__ == "__main__":
    main()
