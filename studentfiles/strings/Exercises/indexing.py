def main():
   # vraagt gebruiker om een zin in te voeren
   #laat zin zien
   # vraagt gebruiker om en nummer
   # vertelt gebruiker het teken op die positie
   zin=input("kies een zin")
   print("jou zin is'", zin, "'",  sep="") 
   pos = int(input("welk karakter? [enter number]"))
   print("karakter nummer", pos, "is", zin[pos])

main()

def main():
    zin = input('voer hier een zin in: ')
    print('U heeft de volgende zin ingevoerd: ', zin)
    nummer = int(input('voer hier nu een nummer tussen de 1 en de 9 in: '))
    print('Uw ingevoerde nummer, staat gelijk aan de volgende letter', (str.capitalize(zin[nummer])),'Houd er rekening mee dat Python altijd vanaf 0 op begint te tellen.')

    

main()