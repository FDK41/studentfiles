def main():

    zin = input("kies een zin")
    print("jou zin is",zin, "'",sep="")
    pos = int(input("welk karakter? [enter number]"))-1
    print("karakter nummer", pos, "is", zin[pos])

main()




#Choose a phrase: Hello, world!
#Your phrase is 'Hello, world!'
#Which character? [Enter number] 4
#Character 4 is o