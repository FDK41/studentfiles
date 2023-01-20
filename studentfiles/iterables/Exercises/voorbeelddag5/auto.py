from voertuig import Voertuig

class Auto(Voertuig):
    def __init__(self, merk):
        self.kenteken = ""
        self.merk = merk
        self.snelheid = 0
        self.kilometerstand = 0
        self.bouwjaar = 0
        self.apk_keuringsdatum= 
    def rijden(self):
        self.snelheid = 50
    def stoppen(self):
        self.snelheid = 0