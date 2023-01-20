def main():
    # maak een lege Dictionary
    cijfers = {}
    #vul de dictionary via user
    # met vakken en het cijfer
    cijfer = int(input('voer het cijfer in voor Engels'))
    cijfers['Engels']= cijfer 
    cijfer = int(input('voer het cijfer in voor Math'))
    cijfers['Math']= cijfer 
    cijfer = int(input('voer het cijfer in voor GLobal studies'))
    cijfers['Global studies']= cijfer 
    cijfer = int(input('voer het cijfer in voor Art'))
    cijfers['Art']= cijfer 
    cijfer = int(input('voer het cijfer in voor Music'))
    cijfers['Music']= cijfer 

    #print(cijfers)
    #bereken het gemiddelde cijfer

    # de values(), sum() en len() funties
    som = (sum(cijfers.values()))
    aantal = (len(cijfers))
    print("Het gemiddelde cijfer is:",som/aantal)
main()

#English grade: 98
#Math grade: 89
#Global Studies grade: 79
#Art grade: 91
#Music grade: 84
#Your average is 88.2

