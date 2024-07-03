import random

class Snake:
    def __init__(self, init_length=1):
        # Initialisation du corps du serpent avec un seul segment au début
        self.body = [(0, 0)]
        # Direction initiale du serpent (vers la droite)
        self.direction = (1, 0)
        # Variable pour gérer la croissance du serpent
        self.growing = 0
        self.grow(init_length - 1)
        print(f"Initialisation du serpent : {self.body}")

    def grow(self, segments):
        # Ajout de segments supplémentaires pour la croissance du serpent
        # Ici, nous ajoutons simplement le nombre de segments à la variable growing
        self.growing += segments
        print(f"Croissance du serpent : {self.body}")

    def move(self):
        # Calcul de la nouvelle position de la tête du serpent
        # Formule : new_head = (current_x + direction_x, current_y + direction_y)
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        print(f"Nouvelle tête calculée : {new_head}")

        if self.growing > 0:
            # Si le serpent doit grandir, ajouter la nouvelle tête sans supprimer le dernier segment
            self.body = [new_head] + self.body
            self.growing -= 1
        else:
            # Sinon, ajouter la nouvelle tête et supprimer le dernier segment pour simuler le mouvement
            self.body = [new_head] + self.body[:-1]

        print(f"Corps du serpent après mouvement : {self.body}")

    def change_direction(self, new_direction):
        # Changer de direction seulement si ce n'est pas directement opposé à la direction actuelle
        # La condition vérifie que les directions ne sont pas opposées
        # Produit scalaire : self.direction[0] * new_direction[0] + self.direction[1] * new_direction[1] doit être égal à 0 pour que la direction soit valide
        if (self.direction[0] * new_direction[0] == 0 and self.direction[1] * new_direction[1] == 0):
            self.direction = new_direction
            print(f"Changement de direction : {self.direction}")

    def check_collision(self):
        # Vérifie si le serpent se mord la queue, uniquement si sa taille est supérieure à 2
        # Utilise l'opérateur "in" pour vérifier si la tête est dans le reste du corps
        if len(self.body) > 2:
            collision = self.body[0] in self.body[1:]
        else:
            collision = False
        print(f"Collision avec soi-même : {collision}")
        return collision

    def check_wall_collision(self, width, height):
        x, y = self.body[0]
        # Vérifie si la tête du serpent est en dehors des limites du jeu
        # Formule pour vérifier les limites : 0 <= x < width et 0 <= y < height
        collision = not (0 <= x < width and 0 <= y < height)
        print(f"Collision avec le mur : {collision}")
        return collision

    def wrap(self, width, height):
        x, y = self.body[0]
        # Enveloppement de la tête du serpent (téléportation de l'autre côté)
        # Formule pour envelopper : new_x = current_x % width, new_y = current_y % height
        x = x % width
        y = y % height
        self.body[0] = (x, y)
        print(f"Enveloppement de la tête du serpent : {self.body[0]}")

class Food:
    def __init__(self, width, height):
        # Initialisation des dimensions de la zone de jeu pour la nourriture
        self.position = (0, 0)
        self.width = width
        self.height = height
        self.spawn()
        print(f"Position initiale de la nourriture : {self.position}")

    def spawn(self):
        # Génère une nouvelle position aléatoire pour la nourriture
        # Utilisation de random.randint pour générer des coordonnées aléatoires
        self.position = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        print(f"Nouvelle position de la nourriture : {self.position}")

class GameModel:
    def __init__(self, width=40, height=30, snake_length=1):
        # Initialisation des dimensions du jeu
        self.width = width
        self.height = height
        # Initialisation du serpent avec la longueur spécifiée
        self.snake = Snake(snake_length)
        # Initialisation de la nourriture
        self.food = Food(width, height)
        # Initialisation du score
        self.score = 0

    def update(self):
        # Déplacement du serpent
        self.snake.move()
        # Vérification si le serpent mange la nourriture
        if self.snake.body[0] == self.food.position:
            # Croissance du serpent
            self.snake.grow(1)
            # Apparition d'une nouvelle nourriture
            self.food.spawn()
            # Incrémentation du score
            self.score += 1
            print(f"Le serpent a mangé la nourriture. Score : {self.score}")
        # Vérification des collisions avec les murs
        if self.snake.check_wall_collision(self.width, self.height):
            self.snake.wrap(self.width, self.height)
        # Vérification des collisions avec le corps du serpent
        if self.snake.check_collision():
            print("Fin du jeu, le serpent s'est mordu.")
            return False
        return True
