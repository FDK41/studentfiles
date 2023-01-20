def main():    

    vakkenlijst = {'Engels':0,'Wiskunde':0,'Algemene studies':0,'Kunst':0,'Muziek':0}

    # print(list(vakkenlijst.keys())[0])
    # vakkenlijst['Engels'] = int(input('Wat was het cijfer voor ' +list(vakkenlijst.keys())[0]+' ?'))
    # vakkenlijst[1] = int(input('Wat was het cijfer voor'vakkenlijst[1]'?'))
    # vakkenlijst[2] = int(input('Wat was het cijfer voor'vakkenlijst[2]'?'))
    # vakkenlijst[3] = int(input('Wat was het cijfer voor'vakkenlijst[3]'?'))
    # vakkenlijst[4] = int(input('Wat was het cijfer voor'vakkenlijst[4]'?'))
    
    # print(vakkenlijst)
    for vak, cijfer in vakkenlijst.items():
        print('het oorsponkelijke cijfer van', vak, 'was', cijfer )
        vakkenlijst[vak] = int(input('Voer het nieuwe cijfer in voor ' +vak+' ?'))
    
    print(vakkenlijst)


    # print(vakkenlijst)
    # for vak, cijfer in vakkenlijst.items():
    #     print(vak, cijfer)
    #     vakkenlijst[vak] = int(input('Wat was het cijfer voor ' +vak+' ?'))
    
    # print(vakkenlijst)

main()