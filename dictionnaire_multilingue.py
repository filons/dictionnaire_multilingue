
class dictionnaireMultilingue:
    def __init__(self):
        self.dictionnaire={}
    
    def ajouter_mot(self,mot,langue,traduction):
        
        if mot not in self.dictionnaire:
            self.dictionnaire[mot]={}
        else :
            self.dictionnaire[mot][langue]=traduction

    def supprimer_mot(self,mot):
        
        if mot in self.dictionnaire:
            del self.dictionnaire[mot]
            print("suppression avec succes !")
        else :
            print("pas de correspondance pour ce mot !")

    def rechercher(self,mot):
        if mot in self.dictionnaire:
            return print(f"mot trouve : {mot} ")
        else :
            print ("aucun mot trouver ")

    def traduction(self,mot,langue):
        
        if mot in self.dictionnaire and langue in self.dictionnaire[mot]:
            return self.dictionnaire[mot][langue]
        else:
            print("le mot de se trouve pas dans le dictionnaire")
        
    def afficher_dictionnaire(self):
        print("    DICTIONNAIRES\n")
        for mot , traductions in self.dictionnaire.items():
            print(f"mot : {mot}")
            for langue , traduction in traductions.items():
                print(f"{langue} : {traduction}")
    
def main():
        dictionnaires=dictionnaireMultilingue()
        while True : 
            print("Menu\n")
            print("1. Ajouter un mot ")
            print("2. rechercher un mot ")
            print("3. traduire un mot ")
            print("4. Afficher le dictionnaire ")
            print("5. supprimer un mot  ")
            print("6. quitter ")

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
                break
    
if __name__=="__main__":
    main()