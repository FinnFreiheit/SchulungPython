'''

Aufgabe:
Erstellt Klassen für Tiere

Basisklasse - Tiere - Beine, Farbe, Lebensraum, Alter,..
Abgeleitete Klasse:

    - Säugetier
    - Reptilien
    - Fische
    - Vögel

'''

class Tier:

    def __init__(self,Beine,Farbe,Lebensraum,Alter):
        self.beine = Beine
        self.farbe = Farbe
        self.Lebensraum = Lebensraum
        self.alter = Alter

class Saugetier(Tier):

    def __init__(self, Beine, Farbe, Lebensraum, Alter, Fell):
        super().__init__(Beine, Farbe, Lebensraum, Alter)
        self.fell = Fell

        





