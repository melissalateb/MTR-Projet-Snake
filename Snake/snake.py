# import pygame
# import time
# import random

# # Initialiser pygame
# pygame.init()

# # Couleurs
# blanc = (255, 255, 255)
# jaune = (255, 255, 102)
# noir = (0, 0, 0)
# rouge = (213, 50, 80)
# vert = (0, 255, 0)
# bleu = (50, 153, 213)
# gris = (169, 169, 169)

# # Dimensions de l'écran
# largeur_ecran = 800
# hauteur_ecran = 600

# # Création de l'écran
# ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
# pygame.display.set_caption('Snake')  # Correction ici

# horloge = pygame.time.Clock()

# # Taille du serpent
# taille_serpent = 20
# vitesse_serpent = 15

# # Style de la police
# style_police = pygame.font.SysFont("bahnschrift", 25)
# style_score = pygame.font.SysFont("comicsansms", 35)

# def score(score):
#     valeur = style_score.render("Score: " + str(score), True, noir)
#     ecran.blit(valeur, [0, 0])

# def notre_serpent(taille_serpent, liste_serpent):
#     for x in liste_serpent:
#         pygame.draw.ellipse(ecran, noir, [x[0], x[1], taille_serpent, taille_serpent])

# def message(msg, couleur, position):
#     mesg = style_police.render(msg, True, couleur)
#     ecran.blit(mesg, position)

# def bouton(msg, x, y, largeur, hauteur, couleur_inactive, couleur_active, action=None):
#     souris = pygame.mouse.get_pos()
#     clique = pygame.mouse.get_pressed()

#     if x + largeur > souris[0] > x and y + hauteur > souris[1] > y:
#         pygame.draw.rect(ecran, couleur_active, (x, y, largeur, hauteur))
#         if clique[0] == 1 and action is not None:
#             action()
#     else:
#         pygame.draw.rect(ecran, couleur_inactive, (x, y, largeur, hauteur))

#     petit_texte = pygame.font.SysFont("comicsansms", 20)
#     texte_surface = petit_texte.render(msg, True, noir)
#     texte_rect = texte_surface.get_rect(center=((x + (largeur / 2)), (y + (hauteur / 2))))
#     ecran.blit(texte_surface, texte_rect)

# def quitter_jeu():
#     pygame.quit()
#     quit()

# def jeu():
#     game_over = False
#     game_close = False

#     x1 = largeur_ecran / 2
#     y1 = hauteur_ecran / 2

#     x1_change = 0
#     y1_change = 0

#     liste_serpent = []
#     longueur_serpent = 1

#     nourriturex = round(random.randrange(0, largeur_ecran - taille_serpent) / 20.0) * 20.0
#     nourriturey = round(random.randrange(0, hauteur_ecran - taille_serpent) / 20.0) * 20.0

#     while not game_over:

#         while game_close == True:
#             ecran.fill(bleu)
#             message("Vous avez perdu!", rouge, [largeur_ecran / 4, hauteur_ecran / 4])
#             message("Appuyez sur C pour continuer ou Q pour quitter", noir, [largeur_ecran / 4, hauteur_ecran / 3])
#             score(longueur_serpent - 1)
#             pygame.display.update()

#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         jeu()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -taille_serpent
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = taille_serpent
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -taille_serpent
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = taille_serpent
#                     x1_change = 0

#         # Traversée des murs
#         if x1 >= largeur_ecran:
#             x1 = 0
#         elif x1 < 0:
#             x1 = largeur_ecran - taille_serpent
#         if y1 >= hauteur_ecran:
#             y1 = 0
#         elif y1 < 0:
#             y1 = hauteur_ecran - taille_serpent

#         x1 += x1_change
#         y1 += y1_change
#         ecran.fill(gris)
#         pygame.draw.ellipse(ecran, vert, [nourriturex, nourriturey, taille_serpent, taille_serpent])
#         tete_serpent = []
#         tete_serpent.append(x1)
#         tete_serpent.append(y1)
#         liste_serpent.append(tete_serpent)
#         if len(liste_serpent) > longueur_serpent:
#             del liste_serpent[0]

#         for x in liste_serpent[:-1]:
#             if x == tete_serpent:
#                 game_close = True

#         notre_serpent(taille_serpent, liste_serpent)
#         score(longueur_serpent - 1)

#         pygame.display.update()

#         if x1 == nourriturex and y1 == nourriturey:
#             nourriturex = round(random.randrange(0, largeur_ecran - taille_serpent) / 20.0) * 20.0
#             nourriturey = round(random.randrange(0, hauteur_ecran - taille_serpent) / 20.0) * 20.0
#             longueur_serpent += 1

#         horloge.tick(vitesse_serpent)

#     pygame.quit()
#     quit()

# def ecran_d_accueil():
#     accueil = True

#     while accueil:
#         ecran.fill(blanc)
#         message("Bienvenue dans Snake!", noir, [largeur_ecran / 4, hauteur_ecran / 4])
#         message("Appuyez sur P pour jouer ou Q pour quitter", noir, [largeur_ecran / 4, hauteur_ecran / 3])

#         bouton("Jouer", 150, 450, 100, 50, vert, jaune, jeu)
#         bouton("Quitter", 550, 450, 100, 50, rouge, jaune, quitter_jeu)

#         pygame.display.update()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 accueil = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_p:
#                     jeu()
#                 if event.key == pygame.K_q:
#                     accueil = False

#     pygame.quit()
#     quit()

# ecran_d_accueil()
