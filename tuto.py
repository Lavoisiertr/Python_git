# Programme qui demande à l'utilisateur son nom et son âge
'''print('Bonjour tout le monde !')
print("Programme qui demande le nom et l'âge d'un utilisateur.")
age = int(input('Quel est votre âge ? : '))
nom = input('Quel est votre nom ? : ')
print(f"Vous vous appelez {nom} et vous avez {age} ans.")
'''

# Programme qui permet d'ajouter un élément dans une liste vide créée au préalable
'''
liste = []
liste.append('Ananas')
print(liste)
'''

# Programme qui permet de créer une liste avec la fonction range(). Utilisation des fonctions max(), min() et sum()
# l'instruction \u2764 permet d'obtenir un coeur en Python
# \n permet un retour à la ligne, \t permet de faire une tabulation vers la droite
'''
liste = list(range(10))
print(liste)
print(max(liste))
print(min(liste))
print(sum(liste))
print('a\nb')
print("J'aime le langage de programmation Python \u2764")
'''

# os est un module qui permet de gérer le système d'exploitation en manipulant(créer, supprimer, ...) les dossiers.
'''
import os 
chemin = 'Users\LAVOISIER_TR\Desktop\Module_os'
Nouveau_dossier = os.path.join(chemin, 'Mon_dossier', 'sous_dossier', 'sous_sous_dossier')
os.removedirs(Nouveau_dossier)
'''

# Le module random contient plusieurs fonctions comme randint(), randrange(), uniform(), permettant de générer des valeurs numériques aléatoires
# La fonction help() permet d'avoir de l'aide sur un élément
# la fonction dir() permet d'avoir des information sur un élément
# le module pprint contient la fonction pprint() permettant d'afficher les objets sous forme de liste
# Il ne faut jamais utiliser les fonctions qui contient __ comme par exemple __file__ etc.. car ces fonctions n'ont pas été conçu pour nous mais servent au fonctionnement de Python.
'''
import random
from pprint import pprint
print(dir(random))
help(random.Random)
pprint(dir(random)
pprint('Bonjour tout le monde !')
help(pprint)
'''

# Programme qui permet d'utiliser la boucle while
'''
while True:
    mdp = input("Entrer votre mot de passe ICI(minimum 8 caractères): ")
    longueur_mdp = "votre mot de passe est trop court !"
    if len(mdp) == 0:
         print(longueur_mdp.upper())
    elif mdp.isdigit():
        print("Votre mot de passe ne contient que des nombres !")     
    elif len(mdp) < 8:
        print(longueur_mdp.capitalize())
    else:
        print("Vous avez saisi le mot de passe récommandé, bravo !")
        break
print('FIN DU PROGRAMME !')

continuer = 'o'
while continuer == 'o':
    print('On continue...')
    continuer = input('Voulez-vous continuer ? o/n : ' )
    if continuer != 'o':
        print('FIN DU PROGRAMME. AU REVOIR!!!')
'''

# Utilisation de la notion des listes de compréhension ou compréhesion en liste ou list comprehension (en anglais)
'''       
liste = [1, 5, 7, 6, -8, -78, -6, -7845, 25, 75, -52]
nombres_positifs = []
for i in liste:
    if i > 0:
        nombres_positifs.append(i)
print('nombres_positifs = ', nombres_positifs)

nombres_positifs_2 = [i*52 for i in liste if i > 0]
print('nombres_positifs_2 = ', nombres_positifs_2)'''

# Quelques exercices résilus sur la notion des listes de compréhension
#---------------------------------------------------------------------------------#

#nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
#nombres_pairs = []
#for i in nombres:
#   if i % 2 == 0:
#    nombres_pairs.append(i)
#print(nombres_pairs)

#nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
#nombres_pairs = [i for i in nombres if i%2==0]
#print(nombres_pairs) --> [44, 4, 38]

#--------------------------------------------------------------------------------------#

#nombres = range(5)
#nombres = range(-10, 10)
#nombres_positifs = []
#for i in nombres:
#    if i >= 0:
#        nombres_positifs.append(i)
#print(nombres_positifs)

#nombres = range(5)
#nombres = range(-10, 10)
#nombres_positifs = [i for i in nombres if i >= 0]
#print(nombres_positifs)  --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#----------------------------------------------------------------------------------------#

#nombres = range(5)
#nombres_doubles = []
#for i in nombres:
#    nombres_doubles.append(i*2)
#print(nombres_doubles)

#nombres = range(5)     
#nombres_doubles = [i*2 for i in nombres]
#print(nombres_doubles) --> [0, 2, 4, 6, 8]

#------------------------------------------------------------------------------------------#

#nombres = range(10)
#nombres_inverses = []
#for i in nombres:
#    if i % 2 == 0:
#        nombres_inverses.append(i)
#    else:
#        nombres_inverses.append(-i)
#print(nombres_inverses)

#nombres = range(10)
#nombres_inverses = [i if i%2 == 0 else -i for i in nombres ]
#print(nombres_inverses)  --> [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]


# Exercice qui demande à l'utilisateur d'entrer 10 fois le nom utilisateur numéroté et commençant par 1 
'''for i in range(1, 11):
    print('Utilisateur ' + str(i))
'''

# Programme qui permet d'afficher les lettres d'un mot en l'envers
'''mot = 'Python'
for l in reversed(mot):
    print(l)'''    
 
# Programme qui permet d'utiliser la boucle while 
'''
continuer = 'o'
while continuer == 'o':
    print('On continue !')
    continuer = input('Voulez-vous continuer ? o/n : ')
    if continuer == 'n' or continuer != 'n':
        print('FIN DU PROGRAMME. AUREVOIR !!!')'''
        
# Programme qui demande à l'utilisateur de saisir deux nombres
'''nom = input("Bonjour ! Quel est votre nom svp ? : ")
print(f"Bienvenue {nom}, nous allons faire un petit jeu de mathématiques")
print('')
print('*********************************************************************')
print('')
print('\t\t\tJEU DE MATHEMATIQUES')
print('')
print('*********************************************************************')
print('')
a = b = ''
while not (a.isdigit() and b.isdigit()):
    a = input("Saisir le premier nombre : ")
    b = input("Saisir le deuxième nombre : ")
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides !")
print(f"La somme entre {a} et {b} donne {int(a) + int(b)}")
print(f"La différence entre {a} et {b} donne {int(a) - int(b)}")
print(f"La multiplication de {a} par {b} donne {int(a) * int(b)}")
print(f"La division entre {a} et {b} donne {int(a) / int(b)}")
print(f"Le modulo de {a} et {b} donne {int(a) % int(b)}")
print(f"{a} puissance {b} donne {int(a) ** int(b)}")
print('')
print('Programme terminé avec SUCCES !!!')
print('')
print('*********************************************************************')
print('')
print('\t\t\t\tFIN DU JEU')
print('')
print('*********************************************************************')'''


# Programme qui permet de gérer une liste de courses
'''import sys

from wcwidth import list_versions
LISTE = []
MENU = Choisissez parmi les 5 options suivantes :
      1: Ajouter un élément à la liste
      2: Retirer un élément de la liste
      3: Afficher la liste
      4: Vider la liste
      5: Quitter
      👉 Votre choix : 
      
MENU_CHOICES = ['1', '2', '3', '4', '5']

while True:
    user_choise = ''
    while user_choise not in MENU_CHOICES:
        user_choise = input(MENU)
        if user_choise not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")
        
        if user_choise == '1': # Ajouter un élément
            item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
            LISTE.append(item)
            print(f"L'élément {item} a bien été ajouté à la liste.")
        elif user_choise == '2': # Retiter un élément
            item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
            if item in LISTE:
                LISTE.remove(item)
                print(f"L'élément {item} a bien été supprimé de la liste.")
            else:
                print(f"L'élément {item} n0est pas dans la liste.")
        elif user_choise == '3': # Afficher la liste
            if LISTE:
                print("Voici le contenu de votre liste")
                for i, item in enumerate(LISTE, 1):
                    print(f"{i}. {item}")
                else:
                    print("Votre liste ne contient aucun élément.")
        elif user_choise == '4': # Vider la liste
            LISTE.clear()
            print("La liste a été vidée de son contenu.")
        elif user_choise == '5': # Quitter
            print("A bientôt !")
            sys.exit()
        
        print("-" * 50)'''
        
        
# Programme du jeu mystère
'''from random import randint
number_to_find = randint(0, 100)
remaining_attempts = 5
print("*** Le jeu du nombre mystère ***")

# boucle principale
while remaining_attempts > 0:
    print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")
    
    # saisie de l'utilisateur
    user_choice = input("Devine le nombre : ")
    if not user_choice.isdigit(): 
        print("Veuillez entrer un nombre valide.")
        continue
    user_choice = int(user_choice)    
    if number_to_find > user_choice: # Plus grand
        print(f"Le nombre mystère est plus grand que {user_choice}")
    elif number_to_find < user_choice: # Plus petit
        print(f"Le nombre mystère est plus petit que {user_choice}")
    else: # Egal (succès)
        break
    remaining_attempts -= 1
    
    # gagné ou perdu
    if remaining_attempts == 0:
        print(f"Domage ! Le nombre mystère était {number_to_find}")
    else:
        print(f"Bravo ! Le nombre mytère était bien {number_to_find}")
        print(f"Tu as trouvé le nombre en {6 - remaining_attempts} essai")
        
    print("Fin du jeu")'''
    
# Programme qui permet d'implémenter un jeu
'''
 # Règles du jeu
Le but de ce projet est de créer un jeu de rôle de textuel dans le terminal
    * Le jeu comporte deux joueurs : vous et un ennemi.
    * Vous commencez tous les deux avec 50 points de vie.
    * Votre personnage dispose de 3 potions qui vous permettent de récupèrer des points de vie.
    * L'ennemi ne dispose d'aucune potion.
    * Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.
    * Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.
    * l'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.
    * Lorsque vous utilisez une potion, vous passez le prochain tour.
    
# Déroulé de la partie
Lorsque vous lancez le script, vous devez demander à l'utilisateur s'il souhaite attaquer ou utiliser une potion : 
"Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "
Cette phrase sera demandé à l'utilisateur au début de chaque tour.
👉 Si l'utilisateur choisi la première option (1), vous infligez des points de dégât à l'ennemi.
Ces points seront compris entre 5 et 10 et déterminés et déterminés aléatoirement par le programme.
👉 Si l'utilisateur choisi la deuxième option (2), vous prenez une potion et vous passez le tour d'après.
'''

# Programme qui permet d'implémenter un jeu
'''import random
ENEMY_HEALTH = 50
PLAYER_HEALTH = 50
NUMBER_OF_POTIONS = 3
SKIP_TURN = False

while True:
    # jeu du joueur
    if SKIP_TURN:
        print("Vous passez votre tour...")
        SKIP_TURN = False
    else:
        user_choice = ''
        while user_choice not in ['1', '2']:
            user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        if user_choice == '1': # Attaque
            your_attack = random.randint(5, 10)
            ENEMY_HEALTH -= your_attack
            print(f"Vous avez infligé {your_attack} points de dégâts à l'ennemi ⚔️.")
        elif user_choice == '2': # Potion
            if NUMBER_OF_POTIONS > 0:
                potion_health = random.randint(15, 50)
                PLAYER_HEALTH += potion_health
                NUMBER_OF_POTIONS -= 1
                SKIP_TURN = True
                print(f"Vous récupérez {potion_health} points de vie 🩸 {NUMBER_OF_POTIONS} 💉 restantes.")
            else:
                print("Vous n'avez plus de potions...")
                continue
    if ENEMY_HEALTH <= 0:
        print("Vous avez gagné 💪.")
        break
    
    # Attaque de l'ennemi
    enemy_attack = random.randint(5, 15)
    PLAYER_HEALTH -= enemy_attack
    print(f"L'énémi vous a infligé {enemy_attack} points de dégâts ⚔️.")
    
    if PLAYER_HEALTH <= 0:
        print("Vous avez perdu 😢")
        break

    # Stats
    print(f"Il vous reste {PLAYER_HEALTH} points de vie 🩸.")
    print(f"Il reste {ENEMY_HEALTH} points de vie 🩸 à l'ennemi.")
    print("_*_" * 50)
print("*** FIN DU JEU ***")'''

# Révision sur les bases de Python --> c'est important car la répétition, c'est la mère des sciences

'''def main():
    print('Bonjour tout le monde !')
    print('Python me passionne')
    def moyenne_eleve(valeurs):
        nom = input("Quel est votre nom ? : ")
        resultat = sum(valeurs)/len(valeurs)
        print(f"La moyenne de {nom} est {resultat}")
        
        
    moyenne_eleve([14, 15, 17, 12, 14.5, 20, 18.75, 16.25])
    
    
    print("Bonjour ! Je vais calculer ta moyenne ")
    nom = input("Quel est ton nom ? : ")
    print(f"Parfait {nom}, à présent je vais te demander d'entrer tes notes.")
    note1 = float(input("Quelle est ta première note ? : "))
    note2 = float(input("Quelle est ta deuxième note ? : "))
    note3 = float(input("Quelle est ta troisième note ? : "))
    note4 = float(input("Quelle est ta quatrième note ? : "))
    note5 = float(input("Quelle est ta cinquième note ? : "))
    print(f"Merci de m'avoir fourni tes notes {nom}")
    notes = [note1, note2, note3, note4, note5]
    moyenne = sum(notes)/len(notes)
    print(f"{nom}, ta moyenne est donc Moyenne =", moyenne)'''
    
    # Exercice à faire
    # 1. Récoler la valeur du porte monnaie d'une personne
    # 2. Créer un produit qui aura pour valeur 50€
    # 3. Afficher la nouvelle valeur du porte  monnaie de la personne qui a achetée après son achat
    
    # Solution de l'exercice
    
''' print("Bonjour madame! Bienvenue dans notre supermarché !")
    
    input("Dites Bonjour également ... : ")
    
    wallet = int(input("Combien avez-vous dans votre porte-monnaie ? : "))
    
    produit = input("Merci pour votre collaboration. Quel est le produit que vous désirez ? : ")
    
    print("D'accord madame. Ce produit coûte 50€ seulement prix promo")
    
    reponse = input("Vous l'acheter ? oui ou non ? : ")
    
    if reponse == 'oui':
        print("Après achat de ce produit, il vous reste", wallet - 50, '€ madame !')
    elif reponse == 'non':
        print("Vous pouvez choisir un autre produit madame car la valeur de votre porte monnaie est toujours", wallet, "€")
    else:
        print("Je n'ai pas compris votre reponse madame.")
            
if __name__ == '__main__':
    main()
'''

# Les conditions

'''wallet = 5000

computer_price = 1200

# Vérifier si le prix de l'ordinateur est inférieur à 1000€

if computer_price < 1000:
    print("Le prix de l'ordinateur est bien inférieur à 1000€.")
else:
    print("Non, le prix de l'ordinateur est supérieur à 1000€.")'''
    
# Système de vérification de mot de passe

'''mdp = input("Entrer votre mot de passe ICI : ")

longeur_mdp = len(mdp)

if longeur_mdp <= 8:
    print("Mot de passe trop court")
else:
    print("Mot de passe valide!")'''
    

# Exercice à faire: place de cinéma
# 1. Récolter l'âge de la personne qui achète les billets "Quel est votre âge?"
# 2. Si la personne est mineur, elle devra payer 7€
# 3. Si la personne est majeur, elle devra payer 12€
# 4. Démander si la personne veut du pop-corn
# 5. Si la personne répond oui, ajouter +5€ dans le prix total à payer
# 6. Afficher le prix total à payer

# Solution de l'exercice: place de cinéma

'''print("BIENVENUE AU CINEMA")
age = int(input("Bonjour monsieur! Quel est votre âge ? : "))
reponse = input("Merci pour votre collaboration. Voulez-vous du pop-corn ? oui ou non ? : ")
print("Bien monsieur...")
if age >= 18:
    print("Vous êtes majeur. Vous devez donc payer 12€ pour le billet")
    prix_total = 12 
else:
    print("Vous êtes mineur. Vous devez donc payer 7€ pour le billet")
    prix_total = 7
if reponse == 'oui':
        prix_total+=5
    
print(f"Vous devez payer au total {prix_total}€")
print("Merci pour la paie et amusez vous bien monsieur!")'''

# La notion des listes en Python

'''
liste = ['Raoul', 'Amina', 'Rosine', 'Rodrigue', 'Patrick']

print(liste)

del liste[-1]

print(liste)

liste.pop(1)

print(liste)

liste.remove('Rosine')

print(liste)

liste.insert(1, 'SUCCES')

print(liste)

liste.insert(2, 'Le succes vous attend')

print(liste)

liste.insert(4, 'Vous êtes des héros')

print(liste)

from statistics import mean
from random import shuffle
from numpy import sort

notes = [15.5, 14, 18, 15, 14.25, 18.25, 20,]

resultat = mean(notes)

print("La moyenne de cet élève est tout simplement", resultat)

print(notes)

shuffle(notes)

print(notes)

notes.sort()

print(notes)

# une autre façon de créer une liste

infos = input("Entrer vos informations de la forme (email-pseudo-motdepasse) : ").split('-')

print("Voici vos informations : ", infos)

print("Bonjour {pseudo}, votre email est {email} et votre mot de passe est {mdp}.".format(pseudo=infos[1], email=infos[0], mdp=infos[2] ))'''

# Exercice à faire: Système de générateur de phrases

# 1. Demander en console une chaîne de la forme mot1/mot2/mot3/mot4/mot5/mot6/mot7...
# 2. Transformer cette chaîne en une liste
# 3. La mélanger
# 4. Si le nombre d'éléments de cette liste est inférieur à 10, alors afficher uniquement les deux premiers mots
# 5. Si le nombre d'éléments de cette liste est supérieur ou égal à 10, alors afficher les trois derniers mots

# Solution de lexercice: système de générateur de phrases

'''from random import shuffle
generateur_mots = input("Entrer une chaîne de la forme (mot1/mot2/mot3/mot4/mot5/mot6/mot7/mot8/mot9/mot10) : ").split("/")
# Affichage de la liste de mots
print(generateur_mots)
# Mélange de la liste de mots
shuffle(generateur_mots)
# Affichage encore de la liste de mots
print(generateur_mots)
print("Le nombre d'éléments de cette liste est", len(generateur_mots))
if len(generateur_mots) < 10:
    print("Les 2 premiers mots de la liste sont donc:")
    print(generateur_mots[0], generateur_mots[1])
elif len(generateur_mots) >= 10:
    print("Les 3 derniers mots de la liste sont donc:")
    print(generateur_mots[-3], generateur_mots[-2], generateur_mots[-1])'''


# Afficher un message à l'utilisateur lui demandant de saisir un entier n dans le but de calculer la factorielle

'''n = int(input("Saisir un entier de son choix : "))
# Fonction qui calcul la factorielle de cet entier, ici n
def calcul_factorielle(n):
    factorielle = 1
    for i in range(1, n+1):
        factorielle*=i
        return factorielle
# Construction du dictionnaire demandé
dictionnaire = dict({})
for i in range(1, n+1):
    dictionnaire[i] = calcul_factorielle(i)
print("Le dictionnaire des factorielle est:", dictionnaire)

dico = {5: ('1!', '2!', '3!', '4!', '5!'), 3: ('1!', '2!', '3!'), 1: ('1!')}

print(dico)'''

# Notion des boucles

'''for i in range(1, 6):
    print("Vous êtes le client n°", i)
    
a = 1
while a < 6:
    print("Vous êtes la", a, "ème femme")
    a+=1

# Itération des éléments d'une liste grâce à la boucle for
emails = ['tchoing50@gmail.com', 'lavoisiertr50@gmail.com', 'raoul3gg@gmail.com', 'programmeur550@gmail.com']
blacklist = ['raoul3gg@gmail.com']
for email in emails:
    if email in blacklist:
        print(f"Envoi interdit à {email}")
        continue # or break
    print(f"Email envoyé à {email}")'''
    
    
# Exercice à faire: jeu du juste prix

'''# 1. Choisir un nombre entre 1 et 1000
# 2. Tant que le jeu n'est pas fini, démander à l'utilisateur d'entrer un prix
# 3. S'il trouve le juste prix c'est gagné
# 4. S'il ne trouve pas le juste prix on affiche c'est moins ou c'est plus'''

# Solution de l'exercice: jeu du juste prix

'''from random import randint

just_price = randint(1, 1000)
while True:
    user_price = int(input("Choisir le juste prix : "))
    if user_price == just_price:
        print("Bravo ! Prix trouvé.")
        break
    elif user_price > just_price:
        print("C'est moins")
    else:
        print("C'est plus")
print("Fin du jeu") '''

# Notion de fonctions

'''year = 2022

def next_year():
    global year
    print(f"Fin de l'année {year}")
    year+=1
    print("Début de l'année {annee_suivante}".format(annee_suivante=year))
    

next_year()
next_year()
next_year()
next_year()
next_year()

def addition():
    resultat = 5 + 5
    print(f"Le résultat de 5 + 5 donne {resultat}")
    return resultat

a = addition()

b = 8

c = a + b

print(c)'''

# Exercice d'application 

'''# Créer une fonction max() qui va renvoyer le résultat le plus haut parmi deux valeurs'''

# Correction de l'exercice d'application

'''def max(a, b):
    if a > b:
        return a
    else:
        return b
    
first_value = int(input("Veuillez saisir la valeur de (a) : "))
second_value = int(input("Veuillez saisir la valeur de (b) : "))
max_value = max(first_value, second_value)
print(f"La valeur maximale entre a et b est {max_value}")'''

# Notion de récursivité --> fonction qui s'appelle elle-même

'''def add(a):
    a+=1
    print(a)
    if a < 20:
        add(a)
    
add(2)'''

# Exercice à faire

'''# Ecrire une fonction permettant de calculer le nombre de voyelles dans un mot, il sera pris en paramètre
# 1. Définir une fonction get_vowels_numbers(mot) qui va prendre en paramètre un mot
# 2. Créer un compteur de voyelles
# 3. Pour chaque lettre du mot vous vérifiez s'il s'agit d'une voyelle
# 4. Si c'est le cas on ajoute 1 au compteur
# 5. A la fin de la fonction, vous allez renvoyer le compteur pour savoir le nombre de voyelles dans ce mot.'''

# Correction de l'exercice

'''def get_vowels_numbers(mot):
    liste_voyelle = ['a', 'e', 'i', 'o', 'u', 'y']
    compteur_voyelles = 0
    for lettre in mot:
        if lettre in liste_voyelle:
            compteur_voyelles+=1
    print(f"{mot} contient {compteur_voyelles} voyelles")
    return compteur_voyelles


get_vowels_numbers("Bonjour tout le monde ")'''

# La programmation orientée OBJET en Python

'''class Voiture():
    marque = 'Peugeot'
    couleur = 'Bleue'
    
#print(f"La couleur de ma voiture est {Voiture.couleur}")
#print(f"La marque de ma voiture est {Voiture.marque}")

voiture_01 = Voiture()

print(f"J'ai à ma possession une voiture de couleur {voiture_01.couleur} et de marque {voiture_01.marque}")

Voiture.couleur = 'noir'

Voiture.marque = 'Porsche'

print(f"J'ai à ma possession une voiture de couleur {voiture_01.couleur} et de marque {voiture_01.marque}")

voiture_02 = Voiture()

voiture_01.couleur = 'Rouge'
voiture_01.marque = 'Toyota'
voiture_02.couleur = 'grise'
voiture_02.marque = 'Lamborghini'

print(f"Ma première voiture à une couleur {voiture_01.couleur} et de marque {voiture_01.marque}")
print(f"Ma deuxième voiture à une couleur {voiture_02.couleur} et de marque {voiture_02.marque}")

class Voiture():
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur
        
    def afficher_marque(self):
        print(f"Ma voiture est de marque {self.marque}")
    
    def afficher_couleur(self):
        print(f"Ma voiture est de couleur {self.couleur}")

voiture_01 = Voiture('Peugeot', 'Grise')
voiture_02 = Voiture('Lamborghini', 'noir')

voiture_01.afficher_couleur()
voiture_01.afficher_marque()
voiture_02.afficher_couleur()
voiture_02.afficher_marque()

#print(f"Voiture_01: marque --> {voiture_01.marque}, couleur --> {voiture_01.couleur}")
#rint(f"Voiture_02: marque --> {voiture_02.marque}, couleur --> {voiture_02.couleur}")

class Personnage():
    def dit(self, message):
        print(message)
        
Lavoisier_TR = Personnage()

Lavoisier_TR.dit("Bonjour tout le monde! J'apprends la POO")

from model.player import Player
from model.weapon import Weapon

knife = Weapon('couteau', 3)  
player_01 = Player('Lavoisier_TR', 10, 5)
player_02 = Player('Graven', 5, 3)

player_01.set_weapon(knife) # donne un couteau faisant 3 dégâts au joueur !


player_01.bienvenue()
player_02.bienvenue()
#print(f"{player_02.get_pseudo()}, initialement vous avez {player_02.get_helth()} points de vie.")
#player_02.damage(2)
#print(f"{player_02.get_pseudo()}, il vous reste maintenant {player_02.get_helth()} points de vie.")

print(f"DEBUT DU COMBAT")
print(f"{player_01.get_pseudo()} attaque {player_02.get_pseudo()}")
player_01.attack_player(player_02)
print(f"{player_02.get_pseudo()} a subi {player_01.get_attack()} dégâts de la part de {player_01.get_pseudo()}, il lui reste {player_02.get_helth()} points de vie.")
print("FIN DU COMBAT")'''

# Révision sur les modules en Python

'''import random

a = random.uniform(2, 5) # permet de donner des valeurs dicimales aléatoirement

print(a)'''

# Un clin d'oeil sur la Programmation Orientée Objet --> POO ou Object Oriented Programming --> OOP en anglais

'''class Personne:
    def __init__(self, nom = '', age = 0):
        self.nom = nom
        self.age = age
        print(f"Constructeur personne: {nom}, {age} ans.")
        
    def se_presenter(self):
        self.demander_nom()
        if self.age == 0:
            print(f"Bonjour je m'appelle {self.nom}.")
        else:
            print(f"Bonjour je m'appelle {self.nom}, j'ai {self.age} ans.")
            if self.est_majeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
           
    def est_majeur(self):
        return self.age >= 18
    
    def demander_nom(self):
        if self.nom == '':
            self.nom = input('Quel est votre nom ? : ')
    
    def demander_age(self):
       if self.age == 0:
            self.age = int(input("Quel est votre âge ? : "))


personne1 = Personne('Jean', 30)
personne2 = Personne('Paul', 15)
personne3 = Personne()
personne1.se_presenter()
#print(f"Est majeur : {personne1.est_majeur()}")
personne2.se_presenter()
#print(f"Est majeur : {personne2.est_majeur()}")
personne3.se_presenter()'''

# Amélioration du code précédent

'''class Personne:
    def __init__(self, nom = '', age = 0):
        self.nom = nom
        self.age = age
        print(f"Constructeur personne: {nom}, {age} ans.")
        
    def se_presenter(self):
        self.demander_nom()
        infos_personne = f"Bonjour je m'appelle {self.nom}"
        if self.age != 0:
            infos_personne+=f", j'ai {self.age} ans."
        print(infos_personne)
        if self.age!=0:    
            if self.est_majeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
           
    def est_majeur(self):
        return self.age >= 18
    
    def demander_nom(self):
        if self.nom == '':
            self.nom = input('Quel est votre nom ? : ')
    
    def demander_age(self):
       if self.age == 0:
            self.age = int(input("Quel est votre âge ? : "))


personne1 = Personne('Jean', 30)
personne2 = Personne('Paul', 15)
personne3 = Personne()
personne1.se_presenter()
personne2.se_presenter()
personne3.se_presenter()'''

# POO EXERCICE DE MISE EN SITUATION 1

'''# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        if self.genre:
            print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
            print("Genre : Masculin")
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
            print()
        else:
            print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
            print("Genre : Feminin")
            if self.EstMajeur():
                print("Je suis majeure")
            else:
                print("Je suis mineure")
            print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25)
personne1.SePresenter()

personne2 = Personne("Emilie", 17)
personne2.SePresenter()'''

# POO CORRECTION DE L'EXERCICE DE MISE EN SITUATION 1

# genre
#   False : Femme
#   True  : Homme

'''class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        genre_str = 'Masculin' if self.genre else 'Feminin'
        e_optionnel = '' if self.genre else 'e' 
        if self.EstMajeur():
            print("Je suis majeur" + e_optionnel) 
        else:
            print("Je suis mineur" + e_optionnel)    
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25, True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17, False)
personne2.SePresenter()'''

# POO EXERCICE DE MISE EN SITUATION 2

'''class Personne:
    def __init__(self, nom: str):
        self.nom = nom   # crée une variable d'instance : nom
        print("Constructeur personne " + self.nom)

    def SePresenter(self, age: int):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(age) + " ans")
        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")
        print()

    def EstMajeur(self):
        return age >= 18

personne1 = Personne("Jean")
personne1.SePresenter(25)

personne1 = Personne("Emilie")
personne1.SePresenter(17)'''

# POO CORRECTION EXERCICE DE MISE EN SITUATION 2

'''class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        
        
        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25)
personne1.SePresenter()

personne2 = Personne("Emilie", 17)
personne2.SePresenter()'''

# POO EXERCICE DE MISE EN SITUATION 3

# ---
'''class Chat:
    def __int__(self):
        self.nom = "inconnu"

    def SePresenter(self, nom_facultatif=""):
        self.nom = nom_facultatif
        print("Bonjour, je suis un chat et je m'appelle " + self.nom)

# ---
class Personne:
    def __int__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je suis une personne et je m'appelle " + self.nom)

# ---
chat1 = Chat()
chat1.SePresenter()  # Bonjour, je suis un chat et je m'appelle inconnu

chat2 = Chat("Garfield")
chat2.SePresenter()  # Bonjour, je suis un chat et je m'appelle Garfield

personne = Personne("Jean")
Personne.SePresenter()  # Bonjour, je suis une personne et je m'appelle Jean'''

# POO CORRECTION EXERCICE DE MISE EN SITUATION 3

# ---
'''class Chat:
    def __init__(self, nom: str = ''):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je suis un chat et je m'appelle " + self.nom)

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je suis une personne et je m'appelle " + self.nom)

# ---
chat1 = Chat('Inconnu')
chat1.SePresenter()  # Bonjour, je suis un chat et je m'appelle inconnu

chat2 = Chat("Garfield")
chat2.SePresenter()  # Bonjour, je suis un chat et je m'appelle Garfield

personne = Personne("Jean")
personne.SePresenter()  # Bonjour, je suis une personne et je m'appelle Jean'''

# Liste d'objets

#---DEFINITION---

''' class Personne:
    def __init__(self, nom = '', age = 0):
        self.nom = nom
        self.age = age
        print(f"Constructeur personne: {nom}, {age} ans.")
        
    def se_presenter(self):
        self.demander_nom()
        infos_personne = f"Bonjour je m'appelle {self.nom}"
        if self.age != 0:
            infos_personne+=f", j'ai {self.age} ans."
        print(infos_personne)
        if self.age!=0:    
            if self.est_majeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
           
    def est_majeur(self):
        return self.age >= 18
    
    def demander_nom(self):
        if self.nom == '':
            self.nom = input('Quel est votre nom ? : ')
    
    def demander_age(self):
       if self.age == 0:
            self.age = int(input("Quel est votre âge ? : "))

#---UTILISATION---

# personne1 = Personne('Jean', 30)
# personne2 = Personne('Paul', 15)    # Création des personnes à partir de la classe Personne()

liste_personnes = (Personne('Jean', 30), Personne('Paul', 15), Personne())

for personnes in liste_personnes:
    personnes.se_presenter()

# liste_personnes = (personne1, personne2)

# personne3 = Personne()
# personne4 = Personne(age=20)
# personne1.se_presenter()
# personne2.se_presenter()   # Méthodes d'instance
# personne3.se_presenter()
# personne4.se_presenter() '''

# POO EXERCICE DE MISE EN SITUATION 4

# ---
''' class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
noms = []
noms.append(input("nom de la personne 1 : "))
noms.append(input("nom de la personne 2 : "))
noms.append(input("nom de la personne 3 : "))

l = []

for nom in noms:
    l.append(Personne(nom))

for p in l:
    print(p.SePresenter()) '''

# POO CORRECTION EXERCICE DE MISE EN SITUATION 4

# ---
''' class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
nombre_personnes = 3
noms = []
for i in range(nombre_personnes):
    noms.append(input("nom de la personne " + str(i+1) + " : "))

liste_personnes = []

for nom in noms:
    liste_personnes.append(Personne(nom))
    

for personne in liste_personnes:
    personne.SePresenter() '''
    
# Variables de classe

'''class Personne:
    def __init__(self, nom = '', age = 0):
        self.nom = nom
        self.age = age
        print(f"Constructeur personne: {nom}, {age} ans.")
        
    def se_presenter(self):
        self.demander_nom()
        infos_personne = f"Bonjour je m'appelle {self.nom}"
        if self.age != 0:
            infos_personne+=f", j'ai {self.age} ans."
        print(infos_personne)
        if self.age!=0:    
            if self.est_majeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
           
    def est_majeur(self):
        return self.age >= 18
    
    def demander_nom(self):
        if self.nom == '':
            self.nom = input('Quel est votre nom ? : ')
    
    def demander_age(self):
       if self.age == 0:
            self.age = int(input("Quel est votre âge ? : "))

#---UTILISATION---

# personne1 = Personne('Jean', 30)
# personne2 = Personne('Paul', 15)    # Création des personnes à partir de la classe Personne()

liste_personnes = (Personne('Jean', 30),
                   Personne('Paul', 15),
                   Personne('Zoé', 20))

for personnes in liste_personnes:
    personnes.se_presenter()'''
    
# liste_personnes = (personne1, personne2)

# personne3 = Personne()
# personne4 = Personne(age=20)
# personne1.se_presenter()
# personne2.se_presenter()   # Méthodes d'instance
# personne3.se_presenter()
# personne4.se_presenter() 

# POO in Python

''' class Student:
    school_name = 'Lavoisier programmer'
    def __init__(self, name = 'No name', matriculate = 'No matriculate', number = 'No number'):
        self.name = name
        self.matriculate = matriculate
        self.number = number    
        
    # Il existe deux sous méthodes de la méthode d'instance : les geteurs ou accesseurs et les seteurs ou mutateurs 
    
    def get_name(self):
        return self.name
    
    def get_matriculate(self):
        return self.matriculate
    
    def get_number(self):
        return self.number
    
    def set_matriculate(self, value):
        self.matriculate = value
        
    # Méthode de classe
    @classmethod  # On appelle ça les décodeurs
    def get_schoolName(cls):
        return cls.school_name
    
    # Méthode statique
    #@staticmethod       # On appelle ça les décodeurs
    #def infos():
    #    print("Cet étudiant aime le langage de programmation Python.")
    
    # Méthode d'instance
        
    def info_student(self):
        print(f"Student of N°{self.get_number()} his name is {self.get_name()} and his registration number is {self.get_matriculate()}. School name is {Student.get_schoolName()}")
    
    

student_1 = Student('Lavoisier', 'CMR001', 1)
student_2 = Student('Donald', 'CMR002', 2)
student_3 = Student('Graven', 'CMR004', 3)
student_4 = Student()

student_3.set_matriculate('CMR003')
student_1.info_student()
student_2.info_student()
student_3.info_student()
student_4.info_student() '''

# OUTER AND INNER CLASS --> CLASSES EXTERIEUR ET INTERIEUR

'''class Student: # Outer Class
    school_name = 'Lavoisier programmer'
    def __init__(self, name = 'No name', matriculate = 'No matriculate', number = 'No number'):
        self.name = name
        self.matriculate = matriculate
        self.number = number
        self.Computer_outerClass = self.Computer_innerClass
        
    # Il existe deux sous méthodes de la méthode d'instance : les geteurs ou accesseurs et les seteurs ou mutateurs 
    
    def get_name(self):
        return self.name
    
    def get_matriculate(self):
        return self.matriculate
    
    def get_number(self):
        return self.number
    
    def set_matriculate(self, value):
        self.matriculate = value
        
    # Méthode de classe
    @classmethod  # On appelle ça les décodeurs
    def get_schoolName(cls):
        return cls.school_name
    
    # Méthode statique
    #@staticmethod       # On appelle ça les décodeurs
    #def infos():
    #    print("Cet étudiant aime le langage de programmation Python.")
    
    # Méthode d'instance
        
    def info_student(self):
        print(f"Student of N°{self.get_number()} his name is {self.get_name()} and his registration number is {self.get_matriculate()}. School name is {Student.get_schoolName()}")
    
    class Computer_innerClass:  # Inner Class
        def __init__(self, RAM, CPU, Mark, name):
            self.RAM = RAM
            self.CPU = CPU
            self.Mark = Mark
            self.name = name
            
        def get_RAM(self):
            return self.RAM
        
        def get_CPU(self):
            return self.CPU
        
        def get_Mark(self):
            return self.Mark
          
        def configuration(self):
            print(f"La machine appartenant à l'étudiant {Student.get_name(self)} possède les caractéristiques suivantes: \n\tRAM : {self.get_RAM()} \n\tCPU : {self.get_CPU()} \n\tMark : {self.get_Mark()}")
       
            
student_1 = Student('Lavoisier', 'CMR001', 1)
student_2 = Student('Donald', 'CMR002', 2)

student_1.Computer_innerClass(4, 2.9, 'Lenovo', student_1.get_name()).configuration()
student_2.Computer_outerClass(2, 1.5, 'Easus', student_2.get_name()).configuration()'''

# INHERITANCE IN OOP --> HERITAGE EN POO
# Il existe plusieurs types d'héritage à savoir : 
# B --> A : single inheritance ou héritage simple en français
# C --> B --> A : multilevel ou héritage à plusieurs niveaux en français
# C --> B && C --> A : multiple inheritance ou héritage multiple en français

'''class A:
    def feature_1(self):
        print('inside class A')
        

class B(A):
    def feature_2(self):
        print('inside class B')


class C(B):
    def feature_3(self):
        print('inside class C')
        
a = A()
b = B()
c = C()
# a.feature_1()
# b.feature_1()
# c.feature_3()
c.feature_2()
c.feature_1()
c.feature_3()'''

# ENCAPSULATION EN POO

'''class Eleve:
    def __init__(self, nom: str, age: int):
        self.__nom = nom
        self.__age = age
        
    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age
    
    def set_nom(self, value):
        self.__nom = value
        
    def set_age(self, value):
        self.__age = value
        
    def se_presenter(self):
        print(f"Bonjour tout le monde! Je m'appelle {self.get_nom()}, j'ai {self.get_age()} ans.")
    
    

eleve_1= Eleve('Lavoisier', 29)
eleve_2= Eleve('Graven', 25)

eleve_1.se_presenter()
eleve_2.se_presenter()'''

# Polymorphisme en Python
# poly = many = plusieurs
# morph = form = formes

# "If it looks like a duck, swims like a duck and quacks like a duck, then it probably is a duck" --> "S'il est comme un canard, nage comme un canard et cri comme un canard, probablement il est un canard."

# Nous allons voir 4 concepts concernant le polymorphisme en Python :
# 1. Duck typing --> Utilisation d'une méthode venant de plusieurs classes et ayant le même nom
# 2. Operator overloading --> Surcharge des opérateurs
# 3. Method overloading --> Surcharge des méthodes
# 4. Method overriding --> Méthode primordiale

## --> DUCK TYPING == Une méthode venant de plusieurs classes avec un nom identique

'''class Visual_studio_code:
    def execute(self):
        print('Edition\nDébogage\nColoration syntaxique')
        
class Pycharm:
    def execute(self):
         print('Python est un langage multiparadigme')
         
class Python:
    def execute(self):
        print('Python est un langage interprété.')


class Laptop:
    def code(self, ide):
        ide.execute()


ide = Visual_studio_code() #Python() #Pycharm()
laptop_1 = Laptop()

laptop_1.code(ide)'''

## --> OPERATOR OVERLOADING == Surcharge des opérateurs (Union des objets)

'''a = 5.2
b = 8.2

print(a+b)
print(float.__add__(a,b))

class Student:
    def __init__(self, moyenne_1, moyenne_2):
        self.moyenne_1 = moyenne_1
        self.moyenne_2 = moyenne_2
        
    def __add__(self, other):
        r1 = self.moyenne_1 + other.moyenne_1
        r2 = self.moyenne_2 + other.moyenne_2
        student_3 = Student(r1, r2)
        return student_3 
        
        
student_1 = Student(12, 18)
student_2 = Student(12, 19)
student_3 = student_1 + student_2  
print(student_3.moyenne_1, student_3.moyenne_2)'''

## --> METHOD OVERLOADING == Surcharge des méthodes

'''def addition(a=None, b=None, c=None):
    if a!=None and b!=None and c!=None:
        somme = a + b + c
    elif a!=None and b!=None:
        somme = a + b
    elif a!=None and c!=None:
        somme = a + c
    elif b!=None and c!=None:
        somme = b + c
    else:
        somme = a
        
    return somme
        
print(addition(12, 18, 58))'''

## --> METHOD OVERRIDING == Méthode primordiale

'''class Desktop:
    def show(self):
        print('Je suis un ordinateur de bureau !')
        
class Laptop(Desktop):
    def show(self):
        print('Je suis un ordinateur portable !')

dekstop_1 = Desktop()
laptop_1 = Laptop()
laptop_1.show()
dekstop_1.show()'''




