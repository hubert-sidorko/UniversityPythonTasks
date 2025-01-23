def palindrom(tekst):
    tekst = tekst.lower()
    tekst = "".join(znak for znak in tekst if (znak.isalnum() or znak == " "))
    ile_wyrazow = len(tekst.split())
    tekst = tekst.replace(" ", "")
    if tekst == tekst[::-1]:
        return (True, ile_wyrazow)
    else:
        return (False, ile_wyrazow)

def main():
    print(palindrom("Madam I’m Adam"))

if __name__ == "__main__":
    main()
