import pygame

# Couleurs
blanc = (255, 255, 255)
jaune = (255, 255, 102)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (2, 112, 21)
bleu = (50, 153, 213)
mauve = (229, 202, 255)

class GameView:
    def __init__(self, model, width=800, height=600, cell_size=20):
        # Référence au modèle de jeu
        self.model = model
        # Dimensions de la fenêtre de jeu
        self.width = width
        self.height = height
        # Taille d'une cellule (segment du serpent ou nourriture)
        self.cell_size = cell_size
        # Initialisation de la fenêtre de jeu
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake')
        # Police pour l'affichage du score
        self.font = pygame.font.SysFont("bahnschrift", 25)
        print(f"Initialisation de la vue du jeu : {self.width}x{self.height}, taille des cellules : {self.cell_size}")

    def draw(self):
        # Remplissage de l'écran avec la couleur grise
        self.screen.fill(mauve)
        # Dessin des segments du serpent
        for segment in self.model.snake.body:
            pygame.draw.ellipse(self.screen, noir, [
                segment[0] * self.cell_size, segment[1] * self.cell_size,
                self.cell_size, self.cell_size
            ])
            print(f"Affichage du segment du serpent à : {segment[0] * self.cell_size}, {segment[1] * self.cell_size}")
        # Dessin de la nourriture
        pygame.draw.ellipse(self.screen, vert, [
            self.model.food.position[0] * self.cell_size, self.model.food.position[1] * self.cell_size,
            self.cell_size, self.cell_size
        ])
        print(f"Affichage de la nourriture à : {self.model.food.position[0] * self.cell_size}, {self.model.food.position[1] * self.cell_size}")
        # Affichage du score
        score_text = self.font.render("Score: " + str(self.model.score), True, noir)
        self.screen.blit(score_text, [0, 0])
        pygame.display.flip()
        print(f"Affichage du score : {self.model.score}")

    def display_message(self, message):
        # Affichage d'un message au centre de l'écran
        font = pygame.font.SysFont("bahnschrift", 35)
        message_text = font.render(message, True, (255, 255, 255))
        self.screen.blit(message_text, [self.width // 6, self.height // 2])
        pygame.display.flip()