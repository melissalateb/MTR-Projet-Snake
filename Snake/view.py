import pygame

# Couleurs
blanc = (255, 255, 255)
jaune = (255, 255, 102)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (0, 255, 0)
bleu = (50, 153, 213)
gris = (169, 169, 169)

class GameView:
    def __init__(self, model, width=800, height=600, cell_size=20):
        self.model = model
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake')
        self.font = pygame.font.SysFont("bahnschrift", 25)
        print(f"Initialisation de la vue du jeu : {self.width}x{self.height}, taille des cellules : {self.cell_size}")

    def draw(self):
        self.screen.fill(gris)
        for segment in self.model.snake.body:
            pygame.draw.ellipse(self.screen, noir, [
                segment[0] * self.cell_size, segment[1] * self.cell_size,
                self.cell_size, self.cell_size
            ])
            print(f"Affichage du segment du serpent à : {segment[0] * self.cell_size}, {segment[1] * self.cell_size}")
        pygame.draw.ellipse(self.screen, vert, [
            self.model.food.position[0] * self.cell_size, self.model.food.position[1] * self.cell_size,
            self.cell_size, self.cell_size
        ])
        print(f"Affichage de la nourriture à : {self.model.food.position[0] * self.cell_size}, {self.model.food.position[1] * self.cell_size}")
        score_text = self.font.render("Score: " + str(self.model.score), True, noir)
        self.screen.blit(score_text, [0, 0])
        pygame.display.flip()
        print(f"Affichage du score : {self.model.score}")
