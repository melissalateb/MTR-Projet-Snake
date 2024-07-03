import pygame
from controller import GameController

class Menu:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Menu')
        self.font = pygame.font.SysFont("bahnschrift", 35)
        self.running = True

    def draw_text(self, text, color, rect):
        label = self.font.render(text, True, color)
        self.screen.blit(label, rect)

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.draw_text('Snake Game', (255, 255, 255), (self.width // 2 - 100, self.height // 2 - 100, 200, 50))
            self.draw_text('1. Start Game', (255, 255, 255), (self.width // 2 - 100, self.height // 2 - 50, 200, 50))
            self.draw_text('2. Quit', (255, 255, 255), (self.width // 2 - 100, self.height // 2, 200, 50))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    print("Événement QUIT détecté, arrêt du jeu")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        print("Démarrage du jeu")
                        game_controller = GameController()
                        game_controller.run_game()
                        self.running = False
                    elif event.key == pygame.K_2:
                        self.running = False
                        print("Quitter le jeu")
        pygame.quit()
