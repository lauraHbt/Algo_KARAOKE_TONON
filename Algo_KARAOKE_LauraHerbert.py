class Player:
    def __init__(self,nom,score):
        self.nom = nom
        self.score = score
        self.musiques = []
    def moyennejoueur(self):
        stock=[]
        for i in range(len(self.musiques)):
            if self.musiques[i] !=0:
                stock.append(self.musiques[i])
                i+=1
            else:
                i+=1
        moyenne = sum(stock)/len(stock)
        print("La moyenne du joueur " + self.nom + " est de " + str(moyenne))
    def scoreTotal(self):
        for i in range(0,len(self.musiques)):
            self.score = self.score + self.musiques[i]
        return self.score
    def meilleureScore(self):
        for i in range(len(self.musiques)):
            for j in range(1,len(self.musiques)):
                if self.musiques[i] > self.musiques[j]:
                    bestScore = self.musiques[i]
                    idScore = i
        print("Le meilleure score du joueur " + self.nom + " est de " + str(bestScore) + " sur la musique " + str(idScore))
    def pireScore(self):
        for i in range(len(self.musiques)):
            for j in range(1,len(self.musiques)):
                if self.musiques[i] < self.musiques[j]:
                    nulScore = self.musiques[i]
                    idScore = i
        print("Le meilleure score du joueur " + self.nom + " est de " + str(nulScore) + " sur la musique " + str(idScore))
    def afficheScore(self):
        print("Voila le score du joueur "+ self.nom + " qui a un score de " + str(self.score))
    def ajouteScore(self,musique,resultat):
        self.musiques.append(resultat)
        return self.musiques


class Karaoke():
    def __init__(self,nbrmusique,joueur):
        self.__nombre = nbrmusique
        self.musique = []
        self.joueur = joueur
    def musiques(self,numero,nom):
        for i in range(self.__nombre):
            self.musique.append(0)
            self.musique.append((numero,nom))
    def ajoutJoueur(self,nbr,nom):
        for i in range(nbr):
            joueur = Player(nom,0,)






nom1 = input("Le nom du joueur 1 : ")
joueur1 = Player(nom1,0)

test = Karaoke(2,1)
test.musiques(0,"bonjour")
partie1m = int(input("Partie 1, Musique :"))
partie1r = int(input("Partie 1, Résultat :"))
joueur1.ajouteScore(partie1m,partie1r)
partie2m = int(input("Partie 2, Musique :"))
partie2r = int(input("Partie 2, Résultat :"))
joueur1.ajouteScore(partie2m,partie2r)
partie3m = int(input("Partie 3, Musique :"))
partie3r = int(input("Partie 3, Résultat :"))
joueur1.ajouteScore(partie3m,partie3r)
joueur1.moyennejoueur()
joueur1.scoreTotal()
joueur1.meilleureScore()
joueur1.pireScore()
joueur1.afficheScore()


