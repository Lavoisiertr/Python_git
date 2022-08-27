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
import sys

from wcwidth import list_versions
LISTE = []
MENU = '''"Choisissez parmi les 5 options suivantes :
      1: Ajouter un élément à la liste
      2: Retirer un élément de la liste
      3: Afficher la liste
      4: Vider la liste
      5: Quitter
      Votre choix : '''
      
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
        
        print("-" * 50)
        
        
# Programme du jeu mystère
            
            
            
    
