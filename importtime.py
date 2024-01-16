import time

class Robot:
    def __init__(self, nom):


        self.nom = nom
        self.allume = False
        self.batterie = 0
        self.vitesse = 0
        self.en_deplacement = False

    def allumer(self):

        if not self.allume:
            print(f"{self.nom} s'allume.")
            self.allume = True

    def eteindre(self):

        if self.allume:
            print(f"{self.nom} s'éteint.")
            self.allume = False

    def charger_batterie(self):

        if not self.allume:
            print("Impossible de charger la batterie => robot éteint.")
            return

        print(f"{self.nom} charge batterie.")

        for i in range(11):
            self.batterie = i * 10
            print(f"{self.nom} : Chargement {self.batterie}%")
            time.sleep(1)

        print(f"{self.nom} : Batterie 100%.")

    def enregistrer_vitesse(self, vitesse):

        if not self.allume:
            print("robot est éteint pas d'enregistrement.")
            return

        self.vitesse = vitesse

        print(f"{self.nom} : Vitesse enregistrée à {self.vitesse} km/h.")

    def obtenir_vitesse(self):

        return self.vitesse

    def arreter_deplacement(self):

        if self.en_deplacement:
            print(f"{self.nom} s'arrête.")
            self.en_deplacement = False
        else:
            print(f"{self.nom} pas en déplacement.")

    def etat_global(self):

        print(f"\nRésumé de l'état de {self.nom}:")
        print(f"  Allumé: {self.allume}")
        print(f"  Batterie: {self.batterie}%")
        print(f"  Vitesse de déplacement: {self.vitesse} km/h")
        print(f"  En déplacement: {self.en_deplacement}")



robot1 = Robot("Robot1")
robot1.allumer()
robot1.charger_batterie()
robot1.enregistrer_vitesse(20)
robot1.arreter_deplacement()
robot1.etat_global()
robot1.eteindre()