def main():
    zin = input("voer een zin in:")
    print("je zin was:" +zin)
    lengte = str(len(zin))
    getal = int(input("voer een getal in tussen 1 en " +lengte +":"))
    print (f"op positie {getal} x staat {zin[getal-1]}")

main()    