import random
import logging

class Snake:
    def __init__(self, init_length=1):
        self.body = [(0, 0)]
        self.direction = (1, 0)
        self.growing = 0
        self.grow(init_length - 1)
        logging.info(f"Initialisation du serpent : {self.body}")

    def grow(self, segments):
        self.growing += segments
        logging.info(f"Croissance du serpent : {self.body}")

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        logging.debug(f"Nouvelle tête calculée : {new_head}")

        if self.growing > 0:
            self.body = [new_head] + self.body
            self.growing -= 1
        else:
            self.body = [new_head] + self.body[:-1]

        logging.debug(f"Corps du serpent après mouvement : {self.body}")

    def change_direction(self, new_direction):
        # Vérifier que le serpent ne peut pas se diriger dans la direction opposée immédiate
        if (self.direction[0] * new_direction[0] == 0 and self.direction[1] * new_direction[1] == 0):
            self.direction = new_direction
            logging.info(f"Changement de direction : {self.direction}")

    def check_collision(self):
        # Vérifier la collision avec soi-même
        if len(self.body) > 2:
            collision = self.body[0] in self.body[1:]
        else:
            collision = False
        logging.debug(f"Collision avec soi-même : {collision}")
        return collision

    def check_wall_collision(self, width, height):
        # Vérifier la collision avec les murs
        x, y = self.body[0]
        collision = not (0 <= x < width and 0 <= y < height)
        logging.debug(f"Collision avec le mur : {collision}")
        return collision

class Food:
    def __init__(self, width, height):
        self.position = (0, 0)
        self.width = width
        self.height = height
        self.spawn()
        logging.info(f"Position initiale de la nourriture : {self.position}")

    def spawn(self):
        # Positionner la nourriture à un endroit aléatoire
        self.position = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
        logging.info(f"Nouvelle position de la nourriture : {self.position}")

class GameModel:
    def __init__(self, width=40, height=30, snake_length=1):
        self.width = width
        self.height = height
        self.snake = Snake(snake_length)
        self.food = Food(width, height)
        self.score = 0

    def update(self):
        self.snake.move()
        # Vérifier si le serpent a mangé la nourriture
        if self.snake.body[0] == self.food.position:
            self.snake.grow(1)
            self.food.spawn()
            self.score += 1
            logging.info(f"Le serpent a mangé la nourriture. Score : {self.score}")
        # Vérifier les collisions avec les murs et soi-même
        if self.snake.check_wall_collision(self.width, self.height):
            logging.info("Fin du jeu, le serpent a heurté le mur.")
            return False
        if self.snake.check_collision():
            logging.info("Fin du jeu, le serpent s'est mordu.")
            return False
        return True
