def start_op():
    f = open("data.txt")
    inhoud = f.read()
    print(inhoud)
    f.close()

def sluit_af(waarde):
    f = open("data.txt","w")
    f.write(str(waarde))
    f.close()

def zeg(iets=''):
    print(iets)
    return 0

def main():
    start_op()
    return_waarde = zeg()
    zeg('hallo')
    zeg('hoe gaat het')
    print(return_waarde)
    sluit_af(return_waarde)


main()
