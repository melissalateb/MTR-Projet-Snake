import random

class Snake:
    def __init__(self, init_length=1):
        self.body = [(0, 0)]
        self.direction = (1, 0)
        self.growing = 0
        self.grow(init_length - 1)
        print(f"Initialisation du serpent : {self.body}")

    def grow(self, segments):
        self.growing += segments
        print(f"Croissance du serpent : {self.body}")

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        print(f"Nouvelle tête calculée : {new_head}")

        if self.growing > 0:
            self.body = [new_head] + self.body
            self.growing -= 1
        else:
            self.body = [new_head] + self.body[:-1]

        print(f"Corps du serpent après mouvement : {self.body}")

    def change_direction(self, new_direction):
        if (self.direction[0] * new_direction[0] == 0 and self.direction[1] * new_direction[1] == 0):
            self.direction = new_direction
            print(f"Changement de direction : {self.direction}")

    def check_collision(self):
        if len(self.body) > 2:
            collision = self.body[0] in self.body[1:]
        else:
            collision = False
        print(f"Collision avec soi-même : {collision}")
        return collision

    def check_wall_collision(self, width, height):
        x, y = self.body[0]
        collision = not (0 <= x < width and 0 <= y < height)
        print(f"Collision avec le mur : {collision}")
        return collision

class Food:
    def __init__(self, width, height):
        self.position = (0, 0)
        self.width = width
        self.height = height
        self.spawn()
        print(f"Position initiale de la nourriture : {self.position}")

    def spawn(self):
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
            print("Fin du jeu, le serpent a heurté le mur.")
            return False
        if self.snake.check_collision():
            print("Fin du jeu, le serpent s'est mordu.")
            return False
        return True

