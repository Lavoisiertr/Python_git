'''print('Bonjour tout le monde !')
print("Programme qui demande le nom et l'âge d'un utilisateur.")
age = int(input('Quel est votre âge ? : '))
nom = input('Quel est votre nom ? : ')
print(f"Vous vous appelez {nom} et vous avez {age} ans.")

liste = []
liste.append('Ananas')
print(liste)


liste = list(range(10))
print(liste)
print(max(liste))
print(min(liste))
print(sum(liste))
print('a\nb')
print("J'aime le langage de programmation Python \u2764")



import os 

chemin = 'Users\LAVOISIER_TR\Desktop\Module_os'

Nouveau_dossier = os.path.join(chemin, 'Mon_dossier', 'sous_dossier', 'sous_sous_dossier')

os.removedirs(Nouveau_dossier)

import random
from pprint import pprint
print(dir(random))

help(random.Random)

Il ne faut jamais utiliser les fonctions qui contient __ comme par exemple __file__ etc.. car ces fonctions n'ont pas été conçu pour nous mais servent au fonctionnement de Python.

pprint(dir(random))

pprint('Bonjour tout le monde !')

help(pprint)


from unicodedata import digit


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
        
liste = [1, 5, 7, 6, -8, -78, -6, -7845, 25, 75, -52]
nombres_positifs = []
for i in liste:
    if i > 0:
        nombres_positifs.append(i)
print('nombres_positifs = ', nombres_positifs)

nombres_positifs_2 = [i*52 for i in liste if i > 0]
print('nombres_positifs_2 = ', nombres_positifs_2)'''

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

'''mot = 'Python'
for l in reversed(mot):
    print(l)    
 
 
continuer = 'o'
while continuer == 'o':
    print('On continue !')
    continuer = input('Voulez-vous continuer ? o/n : ')
    if continuer == 'n' or continuer != 'n':
        print('FIN DU PROGRAMME. AUREVOIR !!!')'''
        
