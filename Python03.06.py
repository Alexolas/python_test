"""
Rahmen: Rahmengröße, Rahmennummer, Herstellungsmaterial (Stahl, Carbon, Aluminium"), Firma, Art, Preis, Farbe, Herstellungsjahr
"""
class Fahrradrahmen:
    rahmengröße=40
    rahmennummer="x"
    material="Stahl"
    firma="Pegasus"
    art="Mountainbike"
    preis=100
    farbe="rot"
    herstellungsjahr=2016
    
    def fahrradrahmeninfo(self):
        print("Fahrradrahmeninformationen:")
        print("die Rahmengröße ist {}".format(self.rahmengröße))
        print("die Rahmennummer ist unbekannt und daher {}".format(self.rahmennummer))
        print("Material: {}".format(self.material))
        print("Firma: {}".format(self.firma))
        print("Art {}".format(self.art))
        print("Preis: {}".format(self.preis))
        print("die Farbe des Rahmens ist {}".format(self.farbe))
        print("Herstellungsjahr: {}".format(self.herstellungsjahr))

class Fahrradlampen:
    firma="Pegasus"
    herstellungsjahr=2017
    lichtfarbe_vorne="gelb"
    lichtfarbe_hinten="rot"
    dynamo="angeschlossen"
    batterien="keine"
    schäden="keine"
    material="Plastik"
    
    def fahrradlampeninfo(self):
        print("Fahrradlampeninformationen:")
        print("Firma: {}".format(self.firma))
        print("Herstellungsjahr: {}".format(self.herstellungsjahr))
        print("die Lichtfarbe vorne ist {}".format(self.lichtfarbe_vorne))
        print("die Lichtfarbe hinten ist {}".format(self.lichtfarbe_hinten))
        print("ein Dynamo ist {}".format(self.dynamo))
        print("die Lampen haben {} Batterien".format(self.batterien))
        print("Schäden: {}".format(self.schäden))
        print("Material: {}".format(self.material))


"""
Rahmengröße, Firma, Rahmennummer, Name, Herstellungsjahr, Art, Schäden, Besitzer, Preis

 Lenker, Speichen, Fahrradständer, Reifen, Sitz, Gepäckträger, Rahmen, Bremse, Dynamo, Schrauben, Räder, Gangschaltung, Lampen(Vorderlicht, Rücklicht), Ketten- oder Nabenschaltung, Farbe
"""
class Fahrrad:
    firma="Pegasus"
    name="rotes Fahrrad"
    schäden="Kratzer"
    preis=600
    besitzer="Nicolas"
    herstellungsjahr=2016
    art="Mountainbike"
    rahmen=Fahrradrahmen()
    lampen=Fahrradlampen()
    
    def fahrradinfo(self):
        print("Fahrradinformationen:")
        print("Firma: {} aus Deutschland\n".format(self.firma))
        self.rahmen.fahrradrahmeninfo()
        print("\nName: {}".format(self.name))
        print("die Schäden sind {} im Lack".format(self.schäden))
        print("der Preis betrug {}€".format(self.preis))
        print("sein Besitzer ist {}".format(self.besitzer))
        print("es wurde {} hergestellt".format(self.herstellungsjahr))
        print("es ist ein {}\n".format(self.art))
        self.lampen.fahrradlampeninfo()
        
class Fabrik1:
    def fahrradhersteller1(self,nummer):
        rad=Fahrrad()
        rad.name=rad.name+" Nr."+str(nummer)
        return rad

fabrik1=Fabrik1()
print("Wieviele Fahrräder möchtest du herstellen?")
y=input()
while y.isalpha()==True:
    print("Bitte gebe ein Zahl ein.")
    y=input()

for x in range(1,int(y)+1):
    bike=fabrik1.fahrradhersteller1(x)
    print("---------------------------------")
    bike.fahrradinfo()
    print("---------------------------------")
