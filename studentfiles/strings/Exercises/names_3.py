# namen = []

# naam = "dummy"
# while len(naam) > 0:
#    naam = input("voer een naam in")
#    namen.append(naam)
#    if naam =="":
#        break


#print(namen)

#for naam in namen :
 #   print(naam)


f = open("../python-basics/data/1880-boys.txt")
namen  = f.read()
losse_namen = namen.split('\n')
f.close()

print(losse_namen)

# for naam in losse_namen:
#     print(naam)