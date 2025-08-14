import json
class dictionnaireMultilingue:
    def __init__(self):
        self.dictionnaire={}
        self.fichier_par_defaut='dictionnaire.json'
        self.charger_dictionnaire()
    
    def ajouter_mot(self,mot,langue,traduction):
        
        if mot not in self.dictionnaire:
            self.dictionnaire[mot]={}
        if langue not in self.dictionnaire[mot]:
            self.dictionnaire[mot][langue] = traduction
        self.dictionnaire[mot][langue]=traduction

    def supprimer_mot(self,mot):
        if mot in self.dictionnaire:
            del self.dictionnaire[mot]
            print("suppression avec succes !")
        else :
            print("pas de correspondance pour ce mot !")

    def rechercher(self,mot):
        if mot in self.dictionnaire:
            print(f"mot trouve : {mot} ")
            for langue, traduction in self.dictionnaire[mot].items():
                print(f"{langue} : {traduction}")
        else :
            print ("aucun mot trouver ")

    def traduction(self,mot,langue):
        
        if mot in self.dictionnaire and langue in self.dictionnaire[mot]:
            return self.dictionnaire[mot][langue]
        else:
            print("le mot ne se trouve pas dans le dictionnaire")
        
    def afficher_dictionnaire(self):
        print("    DICTIONNAIRES\n")
        for mot , traductions in self.dictionnaire.items():
            print(f"mot : {mot}")
            for langue , traduction in traductions.items():
                print(f"{langue} : {traduction}")
    def sauvergarder_dictionnaire(self):
        try:
            with open(self.fichier_par_defaut, 'w', encoding='utf-8') as file:
                json.dump(self.dictionnaire, file, ensure_ascii=False, indent=4)
            print(f"Dictionnaire sauvegardé avec succès dans le fichier '{self.fichier_par_defaut}'")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde : {e}")
    def charger_dictionnaire(self):
        try:
            with open(self.fichier_par_defaut, 'r', encoding='utf-8') as file:
                self.dictionnaire = json.load(file)
            print(f"Dictionnaire chargé avec succès depuis le fichier '{self.fichier_par_defaut}'")
        except FileNotFoundError:
            print(f"Fichier '{self.fichier_par_defaut}' introuvable. Un nouveau dictionnaire sera créé.")
            self.dictionnaire = {}
        except Exception as e:
            print(f"Erreur lors du chargement du dictionnaire : {e}")
            self.dictionnaire = {}
def main():
        dictionnaires=dictionnaireMultilingue()
        while True : 
            print("****Menu****\n")
            print("1. Ajouter un mot ")
            print("2. rechercher un mot ")
            print("3. traduire un mot ")
            print("4. Afficher le dictionnaire ")
            print("5. supprimer un mot  ")
            print("6. sauvegarder le dictionnaire ")
            print("7. quitter le programme ")
            print("\n")

            selection=int(input(" entrer votre choix : "))
            if selection == 1 : 
                dictionnaires.ajouter_mot(
                    mot=input("entrer un mot : "),
                    langue=input("entrer la langue : "),
                    traduction=input("entrer la traduction : ")
                )
            if selection==2 :
                dictionnaires.rechercher(
                    mot=input("entrer le mot a rechercher : ")
                )
            if selection==3 :
                dictionnaires.traduction(
                    mot=input("entrer le mot a traduire : "),
                    langue=input("entrer la langue : ")
                )
            if selection==4 :
                dictionnaires.afficher_dictionnaire()
            if selection==5 :
                dictionnaires.supprimer_mot(
                    mot=input("entrer le mot a supprimer : ")
                )

            if selection==6:
                dictionnaires.sauvergarder_dictionnaire()
            if selection==7:
                print("Au revoir !")
                break
    
if __name__=="__main__":
    main()