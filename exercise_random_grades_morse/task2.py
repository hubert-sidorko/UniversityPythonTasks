morse_code = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
               'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
               'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
               'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
               'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..' }

def tekst_na_morsa(tekst):
    wynik = []
    for znak in tekst.upper():
        if znak in morse_code:
            wynik.append(morse_code[znak])
        else:
            wynik.append("!")
    return wynik

print(tekst_na_morsa("ala ma kota"))
