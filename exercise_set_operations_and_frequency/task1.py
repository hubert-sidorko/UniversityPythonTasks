def czestosc_wielkich_liter(text):
    slownik = {}
    ilosc_wielkich = 0
    for litera in text:
        if litera.isalpha() and litera.isupper():
            ilosc_wielkich += 1
            if litera in slownik:
                slownik[litera] += 1
            else:
                slownik[litera] = 1
    if ilosc_wielkich == 0:
        print("Brak wielkich liter w zdaniu. Sprobuj uruchomic ponownie")
    else:
        wynik = {litera: ilosc / ilosc_wielkich for litera, ilosc in sorted(slownik.items())}
        return wynik

def main():
    text = 'Lorem ipsum dolor sit amet, Consectetur adipiscing elit. Curabitur vel ante lobortis, elementum justo sed, ornare tortor. Integer volutpat ullamcorper lorem vitae aliquet. Cras ligula dolor, elementum sit amet varius a, suscipit et lacus. Ut risus dolor, consequat at semper non, facilisis ut elit. Aliquam vel ipsum vel urna ornare mattis id sed ligula. Nam et odio suscipit, feugiat est vel, mattis nunc. Donec ullamcorper ligula velit, sit amet varius odio posuere eu. Nunc interdum, leo ut laoreet tincidunt, est risus egestas libero, vel vestibulum magna dolor sed turpis. In pulvinar erat sollicitudin magna convallis varius. Pellentesque a velit lectus.'
    wynik = czestosc_wielkich_liter(text)
    print(wynik)

if __name__ == "__main__":
    main()
