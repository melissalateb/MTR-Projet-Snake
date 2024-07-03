import random

class Snake:
    def __init__(self, init_length=1):
        self.body = [(0, 0)]
        self.direction = (1, 0)
        self.grow(init_length - 1)
        print(f"Initialisation du serpent : {self.body}")

    def grow(self, segments):
        for _ in range(segments):
            # Ajouter un nouveau segment à la fin du serpent
            self.body.append(self.body[-1])
        print(f"Croissance du serpent : {self.body}")

    def move(self):
        # Calcul de la nouvelle position de la tête
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        # Formule : new_head = (current_x + direction_x, current_y + direction_y)
        print(f"Nouvelle tête calculée : {new_head}")
        # Ajouter la nouvelle tête et ne supprimer le dernier segment que si le serpent n'a pas grandi
        self.body = [new_head] + self.body[:-1]
        print(f"Corps du serpent après mouvement : {self.body}")

    def change_direction(self, new_direction):
        # Changer de direction seulement si ce n'est pas directement opposé
        if (self.direction[0] * new_direction[0] == 0 and self.direction[1] * new_direction[1] == 0):
            self.direction = new_direction
            print(f"Changement de direction : {self.direction}")

    def check_collision(self):
        # Vérifie si le serpent se mord la queue, uniquement si sa taille est supérieure à 1
        if len(self.body) > 2:
            collision = self.body[0] in self.body[1:]
        else:
            collision = False
        print(f"Collision avec soi-même : {collision}")
        return collision

    def check_wall_collision(self, width, height):
        x, y = self.body[0]
        # Vérifie si la tête du serpent est en dehors des limites du jeu
        collision = not (0 <= x < width and 0 <= y < height)
        print(f"Collision avec le mur : {collision}")
        return collision

    def wrap(self, width, height):
        x, y = self.body[0]
        # Enveloppement de la tête du serpent
        x = x % width
        y = y % height
        self.body[0] = (x, y)
        print(f"Enveloppement de la tête du serpent : {self.body[0]}")

class Food:
    def __init__(self, width, height):
        self.position = (0, 0)
        self.width = width
        self.height = height
        self.spawn()
        print(f"Position initiale de la nourriture : {self.position}")

    def spawn(self):
        # Génère une nouvelle position aléatoire pour la nourriture
        self.position = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        print(f"Nouvelle position de la nourriture : {self.position}")

class GameModel:
    def __init__(self, width=40, height=30, snake_length=1):
        self.width = width
        self.height = height
        self.snake = Snake(snake_length)
        self.food = Food(width, height)
        self.score = 0

    def update(self):
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.grow(1)
            self.food.spawn()
            self.score += 1
            print(f"Le serpent a mangé la nourriture. Score : {self.score}")
        if self.snake.check_wall_collision(self.width, self.height):
            self.snake.wrap(self.width, self.height)
        if self.snake.check_collision():
            print("Fin du jeu, le serpent s'est mordu.")
            return False
        return True
